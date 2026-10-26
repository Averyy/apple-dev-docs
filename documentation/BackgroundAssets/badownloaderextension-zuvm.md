# BADownloaderExtension

**Framework**: Background Assets  
**Kind**: protocol  
**Role**: Protocol

An interface for reacting to app life-cycle events and processing concluded asset downloads while your app isn’t running.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```objc
@protocol BADownloaderExtension <NSObject>
```

## Topics

### Processing downloads
- [- backgroundDownload:didReceiveChallenge:completionHandler:](./badownloaderextension-zuvm/backgrounddownload_didreceivechallenge_completionhandler_.md)
- [- backgroundDownload:finishedWithFileURL:](./badownloaderextension-zuvm/backgrounddownload_finishedwithfileurl_.md)
- [- backgroundDownload:failedWithError:](./badownloaderextension-zuvm/backgrounddownload_failedwitherror_.md)
### Checking for asset updates
- [- downloadsForRequest:manifestURL:extensionInfo:](./badownloaderextension-zuvm/downloadsforrequest_manifesturl_extensioninfo_.md)
- [enum BAContentRequest](./bacontentrequest.md)
  A type that indicates the purpose of a content download request.
- [class BAAppExtensionInfo](./baappextensioninfo.md)
### Reacting to extension events
- [- extensionWillTerminate](./badownloaderextension-zuvm/extensionwillterminate.md)
  Informs the extension that its allotted execution time is over and the system is about to stop the process.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [BAManagedDownloaderExtension](./bamanageddownloaderextension.md)

## See Also

### Unmanaged asset downloads
- [Configuring an unmanaged Background Assets project](./configuring-an-unmanaged-background-assets-project.md)
  Manage and download individual assets yourself by configuring your app and extension targets.
- [BAManifestURL](../BundleResources/information-property-list/bamanifesturl.md)
  The location URL of the app’s manifest file that contains the names and sizes of assets.
- [BAInitialDownloadRestrictions](../BundleResources/information-property-list/bainitialdownloadrestrictions.md)
  The restrictions that apply to the set of assets that download immediately after app installation.
- [BAEssentialMaxInstallSize](../BundleResources/information-property-list/baessentialmaxinstallsize.md)
  The combined, maximum size of the essential assets that the system downloads before it launches your app in bytes.
- [BAMaxInstallSize](../BundleResources/information-property-list/bamaxinstallsize.md)
  The combined, maximum size, in bytes, of the non-essential assets that download immediately after app installation.
- [class BADownloadManager](./badownloadmanager.md)
  An object that manages the queue of scheduled asset downloads.
- [class BAURLDownload](./baurldownload.md)
  An object that represents a remote asset to download.
- [class BADownload](./badownload.md)
  An object that represents an in-progress or concluded asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-zuvm)*