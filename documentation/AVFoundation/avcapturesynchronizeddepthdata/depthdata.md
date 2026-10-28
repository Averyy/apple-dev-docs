# depthData

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) AVDepthData * depthData;
```

## Discussion

If the [`depthDataWasDropped`](./depthdatawasdropped.md) property is [`true`](../../Swift/true.md), this [`AVDepthData`](../avdepthdata.md) object does not contain a depth map (instead, it contains only metadata).

This value is equivalent to that provided by the [`depthDataOutput(_:didOutput:timestamp:connection:)`](../avcapturedepthdataoutputdelegate/depthdataoutput%28_,didoutput,timestamp,connection%29.md) or [`depthDataOutput(_:didDrop:timestamp:connection:reason:)`](../avcapturedepthdataoutputdelegate/depthdataoutput%28_,diddrop,timestamp,connection,reason%29.md) delegate method when using a depth capture output without a data output synchronizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddepthdata/depthdata)*