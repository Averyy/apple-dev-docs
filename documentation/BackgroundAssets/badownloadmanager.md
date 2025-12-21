# BADownloadManager

**Framework**: Background Assets  
**Kind**: class

An object that manages the queue of scheduled asset downloads.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
class BADownloadManager
```

#### Overview

Use [`BADownloadManager`](badownloadmanager.md) to schedule and cancel asset downloads, monitor their progress, and access the queue of pending downloads. You don’t create instances of this class directly; instead, use the [`shared`](badownloadmanager/shared.md) property to access the framework’s singleton that it shares between your app and the app’s extension. Because the download manager is a shared resource, prevent race conditions by using the [`withExclusiveControl(_:)`](badownloadmanager/withexclusivecontrol(_:).md) and [`withExclusiveControl(beforeDate:perform:)`](badownloadmanager/withexclusivecontrol(beforedate:perform:).md) methods to assume absolute control of the manager before you schedule asset downloads or manipulate those already in the manager’s queue. To respond to asset download events and process concluded downloads, create a type that conforms to the [`BADownloadManagerDelegate`](badownloadmanagerdelegate.md) protocol and assign an instance of it to the download manager’s [`delegate`](badownloadmanager/delegate.md) property.

The following example shows how to create an asset download, acquire exclusive control of the shared download manager, and then use the manager to schedule the download:

```swift
let url = URL(string: "https://cdn.example.com/level-resources.zip")!
let request = URLRequest(url: url)
let identifier = "group.com.example.my-game"

// Create an asset download.
let download = BAURLDownload(identifier: "level-resources",
                             request: request,
                             applicationGroupIdentifier: identifier)

// Access the shared download manager.
let manager = BADownloadManager.shared

// Assign the manager's delegate so the framework can notify
// the app of asset download events.
manager.delegate = self

do {
    // Attempt to acquire exclusive control of the manager.
    manager.withExclusiveControl { error in
        // Return immediately if that attempt fails.
        if let error {
            print(error.localizedDescription)
            return
        }
        
        // Use the manager to schedule the asset download.
        try manager.schedule(download)
    }
} catch {
    // Handle the error.
    print(error.localizedDescription)
}

```

## Topics

### Accessing the download manager
- [class var shared: BADownloadManager](badownloadmanager/shared.md)
  The download manager that both the app and the extension share.
### Managing downloads
- [func scheduleDownload(BADownload) throws](badownloadmanager/scheduledownload(_:).md)
  Schedules an asset download to execute in the background at a nonspecific time in the future.
- [func startForegroundDownload(BADownload) throws](badownloadmanager/startforegrounddownload(_:).md)
  Schedules an asset download that executes immediately in the foreground.
- [func cancel(BADownload) throws](badownloadmanager/cancel(_:).md)
  Cancels an asset download.
### Monitoring downloads
- [var delegate: (any BADownloadManagerDelegate)?](badownloadmanager/delegate.md)
  The download manager’s delegate.
- [protocol BADownloadManagerDelegate](badownloadmanagerdelegate.md)
  An interface for reacting to asset download events and processing concluded downloads.
### Fetching in-progress downloads
- [func fetchCurrentDownloads() throws -> [BADownload]](badownloadmanager/fetchcurrentdownloads.md)
- [func fetchCurrentDownloads(completionHandler: ([BADownload], (any Error)?) -> Void)](badownloadmanager/fetchcurrentdownloads(completionhandler:).md)
  Fetches the contents of the manager’s download queue.
### Synchronizing manager access
- [func withExclusiveControl((Bool, (any Error)?) -> Void)](badownloadmanager/withexclusivecontrol(_:).md)
  Attempts to acquire immediate, exclusive access to the download manager.
- [func withExclusiveControl(beforeDate: Date, perform: (Bool, (any Error)?) -> Void)](badownloadmanager/withexclusivecontrol(beforedate:perform:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Configuring an unmanaged Background Assets project](configuring-an-unmanaged-background-assets-project.md)
  Manage and download individual assets yourself by configuring your app and extension targets.
- [Downloading essential assets in the background](downloading-essential-assets-in-the-background.md)
  Fetch the assets your app requires before its first launch using an app extension and the Background Assets framework.
- [BAManifestURL](../BundleResources/Information-Property-List/BAManifestURL.md)
  The location URL of the app’s manifest file that contains the names and sizes of assets.
- [BAInitialDownloadRestrictions](../BundleResources/Information-Property-List/BAInitialDownloadRestrictions.md)
  The restrictions that apply to the set of assets that download immediately after app installation.
- [BAEssentialMaxInstallSize](../BundleResources/Information-Property-List/BAEssentialMaxInstallSize.md)
  The combined, maximum size of the essential assets that the system downloads before it launches your app in bytes.
- [BAMaxInstallSize](../BundleResources/Information-Property-List/BAMaxInstallSize.md)
  The combined, maximum size, in bytes, of the non-essential assets that download immediately after app installation.
- [protocol BADownloaderExtension](badownloaderextension-qwaw.md)
  An interface for reacting to app life-cycle events and processing concluded asset downloads while your app isn’t running.
- [protocol BADownloaderExtensionConfiguration](badownloaderextensionconfiguration.md)
- [class BAURLDownload](baurldownload.md)
  An object that represents a remote asset to download.
- [class BADownload](badownload.md)
  An object that represents an in-progress or concluded asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager)*