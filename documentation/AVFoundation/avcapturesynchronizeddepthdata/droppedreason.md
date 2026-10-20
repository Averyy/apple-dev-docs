# droppedReason

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A value indicating why the capture output failed to deliver depth data, if applicable.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var droppedReason: AVCaptureOutput.DataDroppedReason { get }
```

```objc
@property (readonly) AVCaptureOutputDataDroppedReason droppedReason;
```

## See Also

### Handling dropped data
- [var depthDataWasDropped: Bool](./depthdatawasdropped.md)
  A Boolean value indicating whether depth data was discarded between capture and processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddepthdata/droppedreason)*