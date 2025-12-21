# BADownloaderExtensionConfiguration

**Framework**: Background Assets  
**Kind**: protocol

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency protocol BADownloaderExtensionConfiguration : AppExtensionConfiguration
```

## Relationships

### Inherits From
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [class BADownloadManager](badownloadmanager.md)
  An object that manages the queue of scheduled asset downloads.
- [protocol BADownloaderExtension](badownloaderextension-qwaw.md)
  An interface for reacting to app life-cycle events and processing concluded asset downloads while your app isn’t running.
- [class BAURLDownload](baurldownload.md)
  An object that represents a remote asset to download.
- [class BADownload](badownload.md)
  An object that represents an in-progress or concluded asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextensionconfiguration)*