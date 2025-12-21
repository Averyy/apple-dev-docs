# depthData

**Framework**: AVFoundation  
**Kind**: property

The depth data captured at this synchronization point.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var depthData: AVDepthData { get }
```

#### Discussion

If the [`depthDataWasDropped`](avcapturesynchronizeddepthdata/depthdatawasdropped.md) property is [`true`](https://developer.apple.com/documentation/Swift/true), this [`AVDepthData`](avdepthdata.md) object does not contain a depth map (instead, it contains only metadata).

This value is equivalent to that provided by the [`depthDataOutput(_:didOutput:timestamp:connection:)`](avcapturedepthdataoutputdelegate/depthdataoutput(_:didoutput:timestamp:connection:).md) or [`depthDataOutput(_:didDrop:timestamp:connection:reason:)`](avcapturedepthdataoutputdelegate/depthdataoutput(_:diddrop:timestamp:connection:reason:).md) delegate method when using a depth capture output without a data output synchronizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddepthdata/depthdata)*