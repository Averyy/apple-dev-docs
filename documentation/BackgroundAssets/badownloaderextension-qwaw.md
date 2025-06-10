# BADownloaderExtension

**Framework**: Background Assets  
**Kind**: protocol

An interface for reacting to app life-cycle events and processing concluded asset downloads while your app isn’t running.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
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

- [class BADownloadManager](badownloadmanager.md)
  An object that manages the queue of scheduled asset downloads.
- [protocol BADownloaderExtensionConfiguration](badownloaderextensionconfiguration.md)
- [Downloading essential assets in the background](downloading-essential-assets-in-the-background.md)
  Fetch the assets your app requires before its first launch using an app extension and the Background Assets framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw)*