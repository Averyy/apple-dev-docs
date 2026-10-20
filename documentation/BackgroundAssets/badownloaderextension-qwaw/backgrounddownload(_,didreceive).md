# backgroundDownload(_:didReceive:)

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
func backgroundDownload(_ download: BADownload, didReceive challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)
```

## Default Implementations

### BADownloaderExtension Implementations
- [func backgroundDownload(BADownload, didReceive: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)](./backgrounddownload%28_,didreceive%29-5vjx7.md)
  Download is about to begin but requires an authentication challenge to continue.
- [func backgroundDownload(BADownload, didReceive: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)](./backgrounddownload%28_,didreceive%29-7qfcp.md)
  Handles an authentication challenge.

## See Also

### Processing downloads
- [func backgroundDownload(BADownload, finishedWithFileURL: URL)](./backgrounddownload%28_,finishedwithfileurl%29.md)
- [func backgroundDownload(BADownload, failedWithError: any Error)](./backgrounddownload%28_,failedwitherror%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw/backgrounddownload(_:didreceive:))*