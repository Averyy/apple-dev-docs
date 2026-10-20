# init(sampleBuffer:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a timed metadata group with a sample buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
convenience init?(sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>)
```

#### Return Value

An instance of `AVTimedMetadataGroup`.

## Parameters

- `sampleBuffer`: A [`CMReadySampleBuffer`](../../CoreMedia/cmreadysamplebuffer.md) with media type [`kCMMediaType_Metadata`](../../CoreMedia/kcmmediatype_metadata.md).

## See Also

### Creating a timed metadata group
- [init(items: [AVMetadataItem], timeRange: CMTimeRange)](./init%28items,timerange%29.md)
  Creates a timed metadata group initialized with the given metadata items.
- [init?(sampleBuffer: CMSampleBuffer)](./init%28samplebuffer%29-bjuo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/init(samplebuffer:)-6atlv)*