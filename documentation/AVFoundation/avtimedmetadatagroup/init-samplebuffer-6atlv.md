# init(sampleBuffer:)

**Framework**: AVFoundation  
**Kind**: init

Creates a timed metadata group with a sample buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
convenience init?(sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>)
```

#### Return Value

An instance of `AVTimedMetadataGroup`.

## Parameters

- `sampleBuffer`: A   with media type  .

## See Also

- [init(items: [AVMetadataItem], timeRange: CMTimeRange)](avtimedmetadatagroup/init(items:timerange:).md)
  Creates a timed metadata group initialized with the given metadata items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/init(samplebuffer:)-6atlv)*