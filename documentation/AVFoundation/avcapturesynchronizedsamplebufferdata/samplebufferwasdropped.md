# sampleBufferWasDropped

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether sample buffers were discarded between capture and processing.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var sampleBufferWasDropped: Bool { get }
```

```objc
@property (readonly) BOOL sampleBufferWasDropped;
```

#### Discussion

If this value is [`true`](../../Swift/true.md), sample buffers were captured for this synchronization point but could not be delivered. This situation differs from that where no sample buffer capture for the synchronization timestamp occurs. In that case, there is no [`AVCaptureSynchronizedSampleBufferData`](../avcapturesynchronizedsamplebufferdata.md) object present in the [`AVCaptureSynchronizedDataCollection`](../avcapturesynchronizeddatacollection.md) object delivered to your delegate method.

## See Also

### Handling dropped data
- [var droppedReason: AVCaptureOutput.DataDroppedReason](./droppedreason.md)
  A value indicating why the capture output failed to deliver sample buffers, if applicable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizedsamplebufferdata/samplebufferwasdropped)*