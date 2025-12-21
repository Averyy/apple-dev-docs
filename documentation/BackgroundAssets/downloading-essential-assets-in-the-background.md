# Downloading essential assets in the background

**Framework**: Background Assets

Fetch the assets your app requires before its first launch using an app extension and the Background Assets framework.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 18.4+
- visionOS 2.4+
- Xcode 15.0+

#### Overview

> **Note**: This sample code project is associated with WWDC23 session 10108: [`What’s new in Background Assets`](https://developer.apple.comhttps://developer.apple.com/wwdc23/10108/).

##### Configure the Sample Code Project

Before you run the sample code project in Xcode:

- Configure the WWDC Sessions and WWDC Sessions Background Assets Extension targets to use your Developer team for signing.
- See [`Assign a project to a team`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev23aab79b4).

## See Also

- [Configuring an unmanaged Background Assets project](configuring-an-unmanaged-background-assets-project.md)
  Manage and download individual assets yourself by configuring your app and extension targets.
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

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/downloading-essential-assets-in-the-background)*