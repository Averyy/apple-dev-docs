# urlSession(_:assetDownloadTask:didReceive:)

**Framework**: AVFoundation  
**Kind**: method

Sent when a download task receives an AVMetricEvent.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 28.0+ (Beta)

## Declaration

```swift
optional func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, didReceive metricEvent: AVMetricEvent)
```

## Parameters

- `session`: The NSURLSession corresponding to this AVAssetDownloadTask.
- `assetDownloadTask`: The asset download task.
- `metricEvent`: The metric event received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didreceive:))*