# depthDataWasDropped

**Framework**: AVFoundation  
**Kind**: property

A Boolean value indicating whether depth data was discarded between capture and processing.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var depthDataWasDropped: Bool { get }
```

#### Discussion

If this value is [`true`](https://developer.apple.com/documentation/Swift/true), depth data was captured for this synchronization point but could not be delivered. This situation differs from that where no depth data capture for the synchronization timestamp occurs. In that case, there is no [`AVCaptureSynchronizedDepthData`](avcapturesynchronizeddepthdata.md) object present in the [`AVCaptureSynchronizedDataCollection`](avcapturesynchronizeddatacollection.md) object delivered to your delegate method.

## See Also

- [var droppedReason: AVCaptureOutput.DataDroppedReason](avcapturesynchronizeddepthdata/droppedreason.md)
  A value indicating why the capture output failed to deliver depth data, if applicable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddepthdata/depthdatawasdropped)*