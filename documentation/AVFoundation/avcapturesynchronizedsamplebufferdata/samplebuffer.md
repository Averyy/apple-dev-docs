# sampleBuffer

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
var sampleBuffer: CMSampleBuffer { get }
```

```objc
@property (readonly) CMSampleBufferRef sampleBuffer;
```

#### Discussion

Note that if the [`sampleBufferWasDropped`](./samplebufferwasdropped.md) property is [`true`](../../Swift/true.md), this [`CMSampleBuffer`](../../CoreMedia/cmsamplebuffer.md) object does not contain pixel data (instead, it contains only metadata).

This value is equivalent to that provided by the [`captureOutput(_:didOutput:from:)`](../avcapturevideodataoutputsamplebufferdelegate/captureoutput%28_,didoutput,from%29.md) or [`captureOutput(_:didDrop:from:)`](../avcapturevideodataoutputsamplebufferdelegate/captureoutput%28_,diddrop,from%29.md) delegate method when using a video data output without a data output synchronizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizedsamplebufferdata/samplebuffer)*