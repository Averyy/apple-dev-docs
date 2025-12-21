# BADownloaderExtension

**Framework**: Background Assets  
**Kind**: protocol

An interface for reacting to app life-cycle events and processing concluded asset downloads while your app isn’t running.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
protocol BADownloaderExtension : AppExtension
```

## Topics

### Processing downloads
- [func backgroundDownload(BADownload, didReceive: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)](badownloaderextension-qwaw/backgrounddownload(_:didreceive:).md)
- [func backgroundDownload(BADownload, finishedWithFileURL: URL)](badownloaderextension-qwaw/backgrounddownload(_:finishedwithfileurl:).md)
- [func backgroundDownload(BADownload, failedWithError: any Error)](badownloaderextension-qwaw/backgrounddownload(_:failedwitherror:).md)
### Checking for asset updates
- [func downloads(for: BAContentRequest, manifestURL: URL, extensionInfo: BAAppExtensionInfo) -> Set<BADownload>](badownloaderextension-qwaw/downloads(for:manifesturl:extensioninfo:).md)
- [enum BAContentRequest](bacontentrequest.md)
- [class BAAppExtensionInfo](baappextensioninfo.md)
### Reacting to extension events
- [func extensionWillTerminate()](badownloaderextension-qwaw/extensionwillterminate-236ac.md)
### Instance Methods
- [func extensionWillTerminate()](badownloaderextension-qwaw/extensionwillterminate.md)
  This method may be called shortly before the extension is terminated.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
### Inherited By
- [ManagedDownloaderExtension](manageddownloaderextension.md)

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
- [protocol BADownloaderExtensionConfiguration](badownloaderextensionconfiguration.md)
- [class BAURLDownload](baurldownload.md)
  An object that represents a remote asset to download.
- [class BADownload](badownload.md)
  An object that represents an in-progress or concluded asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw)*