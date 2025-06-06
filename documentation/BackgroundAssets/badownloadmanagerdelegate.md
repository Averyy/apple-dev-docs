# BADownloadManagerDelegate

**Framework**: Background Assets  
**Kind**: protocol

An interface for reacting to asset download events and processing concluded downloads.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
protocol BADownloadManagerDelegate : NSObjectProtocol
```

## Topics

### Reacting to download events
- [func downloadDidBegin(BADownload)](badownloadmanagerdelegate/downloaddidbegin(_:).md)
  Informs the delegate about a started asset download.
- [func download(BADownload, didReceive: URLAuthenticationChallenge, completionHandler: (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)](badownloadmanagerdelegate/download(_:didreceive:completionhandler:).md)
  Tells the delegate to resolve the specified URL authentication challenge.
- [func download(BADownload, didWriteBytes: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64)](badownloadmanagerdelegate/download(_:didwritebytes:totalbyteswritten:totalbytesexpectedtowrite:).md)
  Informs the delegate about the progress of the specified asset download.
- [func downloadDidPause(BADownload)](badownloadmanagerdelegate/downloaddidpause(_:).md)
  Informs the delegate about a paused asset download.
### Processing concluded downloads
- [func download(BADownload, finishedWithFileURL: URL)](badownloadmanagerdelegate/download(_:finishedwithfileurl:).md)
  Informs the delegate about a finished asset download and provides the on-disk location.
- [func download(BADownload, failedWithError: any Error)](badownloadmanagerdelegate/download(_:failedwitherror:).md)
  Informs the delegate about a failed asset download.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any BADownloadManagerDelegate)?](badownloadmanager/delegate.md)
  The download manager’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanagerdelegate)*