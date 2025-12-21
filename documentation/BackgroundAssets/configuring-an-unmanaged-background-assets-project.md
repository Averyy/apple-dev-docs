# Configuring an unmanaged Background Assets project

**Framework**: Background Assets

Manage and download individual assets yourself by configuring your app and extension targets.

#### Overview

To opt out of Managed Background Assets, add a Self-Hosted, Unmanaged extension target to your project, configure the App Groups capability for both the app and extension target, and add some Background Asset keys to the app’s information property list. Then the system notifies your extension when system events occur so that your extension can initiate downloads.

> **Note**: For information about Apple-Hosted Background Assets, see [`Downloading Apple-hosted asset packs`](downloading-apple-hosted-asset-packs.md).

The system launches the extension during the first install and subsequent updates, before a person launches the app, and periodically in the background when the app isn’t running. The sequence of events is:

1. A person installs or updates your app on the device.
2. The system prevents the app from launching and begins downloading your manifest file using the URL you provide.
3. During the manifest download, the system reports progress to the App Store.
4. When the download completes, the system launches your app extension, sending it a content request with the location of the manifest file on disk.
5. The extension uses the manifest file, which should contains the asset URLs and file sizes, to return a set of download requests to the system.
6. The system pauses, or terminates, the extension and begins the downloads.
7. When the downloads complete, the system notifies the extension and allows the app to launch.

The flow for periodic content requests is identical to the app install and updates, except the system determines when periodic events occur, depending on a person’s usage and their system settings. For example, the system factors in whether a person enables the Low Power Mode and Background App Refresh settings.

> **Note**: It’s your responsibility to create manifest files for your self-hosted, unmanaged assets (using your format of choice) that your code parses to get the URLs and file sizes to the system.

##### Add a Self Hosted Unmanaged Extension to Your Project

Choose New > Target, select the Background Download template under Application Extension, and click Next. In the dialog, enter a product name, choose Self-Hosted, Unmanaged as the extension type, and click Finish. In the next dialog, click Activate to use the extension scheme Xcode creates.

If you don’t have an Xcode project for your app, first create one from an Application template under the platform you support, such as iOS or macOS. For more information, see [`Creating an Xcode project for an app`](https://developer.apple.com/documentation/Xcode/creating-an-xcode-project-for-an-app).

##### Add the App Groups Capability

Add your app and extension targets to the same app group so that they can communicate and share data.

Add the App Groups capability to both your app and extension target. For macOS apps, also add the App Sandbox capability to both targets. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

Then, add both targets to the same app group. In the project editor, select the app target, and then add a unique ID for the group under App Groups on the Signing & Capabilities pane. Xcode automatically selects the new group ID. Select the extension target, then go to App Groups, click Refresh, and select the same group ID.

The app and extension are now in the same app group and can share the asset files. For more information on configuring app groups, and additional steps for macOS apps, see [`Configuring app groups`](https://developer.apple.com/documentation/Xcode/configuring-app-groups).

##### Add Required Information Property List Keys

Configure Background Assets for your app target by setting information property list keys. In the project editor, select the app target and click the Info tab. Then, add the following keys to the information property list file:

For more examples of these information property list keys, see the [`Downloading essential assets in the background`](downloading-essential-assets-in-the-background.md) sample code project. For more information on editing the information property list file, see [`Managing your app’s information property list values`](https://developer.apple.com/documentation/BundleResources/managing-your-app-s-information-property-list).

## See Also

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
- [class BADownloadManager](badownloadmanager.md)
  An object that manages the queue of scheduled asset downloads.
- [protocol BADownloaderExtension](badownloaderextension-qwaw.md)
  An interface for reacting to app life-cycle events and processing concluded asset downloads while your app isn’t running.
- [protocol BADownloaderExtensionConfiguration](badownloaderextensionconfiguration.md)
- [class BAURLDownload](baurldownload.md)
  An object that represents a remote asset to download.
- [class BADownload](badownload.md)
  An object that represents an in-progress or concluded asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/configuring-an-unmanaged-background-assets-project)*