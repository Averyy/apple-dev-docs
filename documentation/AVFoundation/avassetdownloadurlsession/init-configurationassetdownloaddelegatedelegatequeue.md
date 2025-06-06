# init(configuration:assetDownloadDelegate:delegateQueue:)

**Framework**: AVFoundation  
**Kind**: init

Creates a URL session to download assets.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(configuration: URLSessionConfiguration, assetDownloadDelegate delegate: (any AVAssetDownloadDelegate)?, delegateQueue: OperationQueue?)
```

#### Return Value

A new download session.

## Parameters

- `configuration`: The configuration for this download session. The configuration you provide must be a   configuration or the system raises an exception.
- `delegate`: The delegate object to handle asset download progress updates and other session related events.
- `delegateQueue`: The queue to receive delegate callbacks on. If you specify  , the system provides a serial queue.

## See Also

- [protocol AVAssetDownloadDelegate](avassetdownloaddelegate.md)
  A protocol that defines the methods to implement to respond to asset-download events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/init(configuration:assetdownloaddelegate:delegatequeue:))*