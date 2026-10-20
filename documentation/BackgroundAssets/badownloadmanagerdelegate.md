# BADownloadManagerDelegate

**Framework**: Background Assets  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol BADownloadManagerDelegate <NSObject>
```

## Topics

### Reacting to download events
- [func downloadDidBegin(BADownload)](./badownloadmanagerdelegate/downloaddidbegin%28_%29.md)
  Informs the delegate about a started asset download.
- [func download(BADownload, didReceive: URLAuthenticationChallenge, completionHandler: (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)](./badownloadmanagerdelegate/download%28_,didreceive,completionhandler%29.md)
  Tells the delegate to resolve the specified URL authentication challenge.
- [func download(BADownload, didWriteBytes: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64)](./badownloadmanagerdelegate/download%28_,didwritebytes,totalbyteswritten,totalbytesexpectedtowrite%29.md)
  Informs the delegate about the progress of the specified asset download.
- [func downloadDidPause(BADownload)](./badownloadmanagerdelegate/downloaddidpause%28_%29.md)
  Informs the delegate about a paused asset download.
### Processing concluded downloads
- [func download(BADownload, finishedWithFileURL: URL)](./badownloadmanagerdelegate/download%28_,finishedwithfileurl%29.md)
  Informs the delegate about a finished asset download and provides the on-disk location.
- [func download(BADownload, failedWithError: any Error)](./badownloadmanagerdelegate/download%28_,failedwitherror%29.md)
  Informs the delegate about a failed asset download.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Monitoring downloads
- [var delegate: (any BADownloadManagerDelegate)?](./badownloadmanager/delegate.md)
  The download manager’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanagerdelegate)*