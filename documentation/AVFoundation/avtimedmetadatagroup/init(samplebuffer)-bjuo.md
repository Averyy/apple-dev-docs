# init(sampleBuffer:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use init(sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) instead

## Declaration

```swift
init?(sampleBuffer: CMSampleBuffer)
```

```objc
- (instancetype) initWithSampleBuffer:(CMSampleBufferRef) sampleBuffer;
```

## Return Value

An instance of AVTimedMetadataGroup.

## Discussion

Initializes an instance of AVTimedMetadataGroup with a sample buffer.

## Parameters

- `sampleBuffer`: A CMSampleBuffer with media type kCMMediaType_Metadata.

## See Also

### Creating a timed metadata group
- [convenience init?(sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>)](./init%28samplebuffer%29-6atlv.md)
  Creates a timed metadata group with a sample buffer.
- [init(items: [AVMetadataItem], timeRange: CMTimeRange)](./init%28items,timerange%29.md)
  Creates a timed metadata group initialized with the given metadata items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/init(samplebuffer:)-bjuo)*