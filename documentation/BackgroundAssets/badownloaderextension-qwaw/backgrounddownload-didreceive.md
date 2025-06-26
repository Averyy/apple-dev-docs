# backgroundDownload(_:didReceive:)

**Framework**: Background Assets  
**Kind**: method  
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

## See Also

- [func backgroundDownload(BADownload, finishedWithFileURL: URL)](badownloaderextension-qwaw/backgrounddownload(_:finishedwithfileurl:).md)
- [func backgroundDownload(BADownload, failedWithError: any Error)](badownloaderextension-qwaw/backgrounddownload(_:failedwitherror:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw/backgrounddownload(_:didreceive:))*