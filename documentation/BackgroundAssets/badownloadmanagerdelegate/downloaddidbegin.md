# downloadDidBegin(_:)

**Framework**: Background Assets  
**Kind**: method

Informs the delegate about a started asset download.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
optional func downloadDidBegin(_ download: BADownload)
```

## Parameters

- `download`: The started asset download.

## See Also

- [func download(BADownload, didReceive: URLAuthenticationChallenge, completionHandler: (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)](badownloadmanagerdelegate/download(_:didreceive:completionhandler:).md)
  Tells the delegate to resolve the specified URL authentication challenge.
- [func download(BADownload, didWriteBytes: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64)](badownloadmanagerdelegate/download(_:didwritebytes:totalbyteswritten:totalbytesexpectedtowrite:).md)
  Informs the delegate about the progress of the specified asset download.
- [func downloadDidPause(BADownload)](badownloadmanagerdelegate/downloaddidpause(_:).md)
  Informs the delegate about a paused asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanagerdelegate/downloaddidbegin(_:))*