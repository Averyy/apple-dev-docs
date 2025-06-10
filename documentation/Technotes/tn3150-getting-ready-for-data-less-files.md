# TN3150: Getting ready for dataless files

**Framework**: Technotes

Understand dataless files and how to minimize the performance impact as the system materializes them.

#### Overview

In a modern file system, a file’s content may not be available locally on the device. A file that contains only metadata is known as a  file. The file’s content typically resides on a remote server and is available to people or apps, transparently, when they access the file.

For example, a person can create a dataless file in iCloud Drive on iOS by selecting a file in the Files app and choosing the Remove Download menu item. That action removes the file’s contents from the local device and frees the used storage space. Later, when a person taps the same file, or an app accesses it, the system redownloads the file’s content and makes it available again — a process known as materialization. File providers typically support dataless files. For more information, see [`Synchronizing the File Provider Extension`](https://developer.apple.com/documentation/FileProvider/synchronizing-the-file-provider-extension).

Materializing a dataless file can take time if the file is large or there are poor network conditions. In such a scenario, the app may become unresponsive. If an app’s main queue remains unresponsive for a long time, the system may terminate the app and trigger a watchdog crash. See [`Addressing watchdog terminations`](https://developer.apple.com/documentation/Xcode/addressing-watchdog-terminations) for details.

#### Understand the Impact of File Materialization

Dataless files reduce the amount of storage space a file typically consumes, but accessing a dataless file causes the system to materialize the file. This can take a long time, creating a poor user experience in apps that aren’t ready for it.

This typically affects apps that store files in their own [`url(forUbiquityContainerIdentifier:)`](https://developer.apple.com/documentation/Foundation/FileManager/url(forUbiquityContainerIdentifier:)) or access files from network file providers like iCloud Drive. Common symptoms are:

- Slower frame rates and jitters when someone scrolls a user interface that loads data from one or more files
- Spins or hangs when performing file system operations
- Time-out errors (`ETIMEDOUT`) when invoking file system APIs
- A watchdog termination where the crash report includes reference to the materialization process

Examples of actions that may result in one or more of these symptoms are enumerating a directory’s contents and checking whether a file exists using [`fileExists(atPath:)`](https://developer.apple.com/documentation/Foundation/FileManager/fileExists(atPath:)).

If you app encounters one of these symptoms, use Instruments to profile your app and identify the contributing API calls. For example, the following trace shows an app using [`contentsOfDirectory(atPath:)`](https://developer.apple.com/documentation/Foundation/FileManager/contentsOfDirectory(atPath:)) to retrieve all paths in a directory, and the `apfs_materialize_dataless_file_ext` symbol in the last frame corresponds to the materialization process:

```None
 1000 -[NSFileManager contentsOfDirectoryAtPath:error:] + 36 (Foundation + 416570) [0x7ff81ca4fb3a]
 1000 _NSDirectoryContentsFromCFURLEnumeratorError + 466 (Foundation + 417600) [0x7ff81ca4ff40]
 1000 _URLEnumeratorGetNextURL + 176 (CoreServicesInternal + 51302) [0x7ff81e465866]
 1000 _GetDirectoryURLs(_CFURLEnumerator*) + 1223 (CoreServicesInternal + 57378) [0x7ff81e467022]
 1000 DirEnumRead + 432 (CoreServicesInternal + 58064) [0x7ff81e4672d0]
 1000 getattrlistbulk + 10 (libsystem_kernel.dylib + 17338) [0x7ff81baed3ba]
 *1000 hndl_unix_scall64 + 22 (kernel + 57910) [0xffffff800021e236]
 *1000 unix_syscall64 + 507 (kernel + 7833867) [0xffffff800098890b]
 *1000 getattrlistbulk + 1570 (kernel + 3070210) [0xffffff80004fd902]
 *1000 apfs_vnop_getattrlistbulk + 272 (apfs + 394110) [0xffffff800356837e]
 *1000 apfs_materialize_dataless_file_ext + 160 (apfs + 738928) [0xffffff80035bc670]
```

#### Prepare Your App for Dataless File Access

The system, or a person using the device, can make dataless files whenever they determine it’s appropriate, and your app needs to be ready to handle them. Specifically, avoid unnecessarily materializing dataless files and, when your app requires access to a file’s contents, perform that work asynchronously off the main thread. For more information, see [`Improving performance and stability when accessing the file system`](https://developer.apple.com/documentation/Foundation/improving-performance-and-stability-when-accessing-the-file-system).

[`UIDocument`](https://developer.apple.com/documentation/UIKit/UIDocument) and [`NSDocument`](https://developer.apple.com/documentation/AppKit/NSDocument) automatically access the file system in a coordinated and asynchronous manner. If your app uses those classes to read and write files (and document packages), it will automatically do the right thing with dataless files. (The system still materializes the intermediate folders, if they themselves are dataless.)

If your app or framework uses low-level POSIX APIs to access the file system and you’re unable to migrate to the preferred methods, consider the following two options:

- Check if a file is dataless and then only access it in a safe context. To do the check, call `stat` or `getattrlist` and examine if `SF_DATALESS` is present in `stat.st_flags`. Be aware that `stat` and `getattrlist` both trigger the materialization of any intermediate folders in the file’s path, if they themselves are dataless.

```c
struct stat fileStat;
if (stat(yourFilePath, &fileStat) == 0) {
    if ((fileStat.st_flags & SF_DATALESS) > 0) {
        // The file is dataless.
    } else {
        // The file isn't dataless.
        // SF_DATALESS is a feature of APFS;
        // don't assume IO is local here because network IO can happen on NFS.
    }
}
```

- Opt-out of dataless file materialization on a per-thread (or per-process) basis. Call `setiopolicy_np` with `IOPOL_MATERIALIZE_DATALESS_FILES_OFF` as the `iotype` parameter, and `IOPOL_SCOPE_THREAD` or `IOPOL_SCOPE_PROCESS` as the `scope`. If you choose this option, handle any EDEADLK errors that arise when accessing dataless files.

```c
int iopolicy = getiopolicy_np(IOPOL_TYPE_VFS_MATERIALIZE_DATALESS_FILES, IOPOL_SCOPE_THREAD);
if (iopolicy >= 0) {
    if (setiopolicy_np(IOPOL_TYPE_VFS_MATERIALIZE_DATALESS_FILES, IOPOL_SCOPE_THREAD, IOPOL_MATERIALIZE_DATALESS_FILES_OFF) == 0) {
        // Do your work here.
        // Detect the EDEADLK error and handle the I/O failure when accessing dataless files.
    }
    // Restore the iopolicy.
    setiopolicy_np(IOPOL_TYPE_VFS_MATERIALIZE_DATALESS_FILES, IOPOL_SCOPE_THREAD, iopolicy);
}
```

For more information about the functions and constants in the above code, see their man pages. [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages) covers how to read man pages.

#### Revision History

-  First published.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3150-getting-ready-for-data-less-files)*