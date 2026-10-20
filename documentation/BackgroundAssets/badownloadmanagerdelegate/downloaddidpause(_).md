# downloadDidPause(_:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Informs the delegate about a paused asset download.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
optional func downloadDidPause(_ download: BADownload)
```

```objc
- (void) downloadDidPause:(BADownload *) download;
```

## Parameters

- `download`: The paused asset download.

## See Also

### Reacting to download events
- [func downloadDidBegin(BADownload)](./downloaddidbegin%28_%29.md)
  Informs the delegate about a started asset download.
- [func download(BADownload, didReceive: URLAuthenticationChallenge, completionHandler: (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)](./download%28_,didreceive,completionhandler%29.md)
  Tells the delegate to resolve the specified URL authentication challenge.
- [func download(BADownload, didWriteBytes: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64)](./download%28_,didwritebytes,totalbyteswritten,totalbytesexpectedtowrite%29.md)
  Informs the delegate about the progress of the specified asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanagerdelegate/downloaddidpause(_:))*