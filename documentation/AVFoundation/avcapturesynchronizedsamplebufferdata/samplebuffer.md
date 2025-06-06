# sampleBuffer

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
var sampleBuffer: CMSampleBuffer { get }
```

#### Discussion

Note that if the [`sampleBufferWasDropped`](avcapturesynchronizedsamplebufferdata/samplebufferwasdropped.md) property is [`true`](https://developer.apple.com/documentation/swift/true), this [`CMSampleBuffer`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer) object does not contain pixel data (instead, it contains only metadata).

This value is equivalent to that provided by the [`captureOutput(_:didOutput:from:)`](avcapturevideodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:).md) or [`captureOutput(_:didDrop:from:)`](avcapturevideodataoutputsamplebufferdelegate/captureoutput(_:diddrop:from:).md) delegate method when using a video data output without a data output synchronizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizedsamplebufferdata/samplebuffer)*