# backgroundDownload(_:failedWithError:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
func backgroundDownload(_ failedDownload: BADownload, failedWithError error: any Error)
```

## Default Implementations

### BADownloaderExtension Implementations
- [func backgroundDownload(BADownload, failedWithError: any Error)](./backgrounddownload%28_,failedwitherror%29-5geag.md)
  Handles a failed download.
- [func backgroundDownload(BADownload, failedWithError: any Error)](./backgrounddownload%28_,failedwitherror%29-9erie.md)
  This method is called when a download has failed but there is no `BADownloadManager` delegate to handle the completion event. When a download has failed, this method will be invoked. If a download fails you may reschedule it with `BADownloadManager`.

## See Also

### Processing downloads
- [func backgroundDownload(BADownload, didReceive: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)](./backgrounddownload%28_,didreceive%29.md)
- [func backgroundDownload(BADownload, finishedWithFileURL: URL)](./backgrounddownload%28_,finishedwithfileurl%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw/backgrounddownload(_:failedwitherror:))*