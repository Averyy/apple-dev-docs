# CMSampleBuffer.TimingPerSample

**Framework**: Core Media  
**Kind**: enum  
**Role**: Enumeration

Specifies timing of each sample in a sample buffer.

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
enum TimingPerSample
```

## Topics

### Enumeration Cases
- [CMSampleBuffer.TimingPerSample.distinct(_:)](./timingpersample/distinct%28_%29.md)
  Each sample has distinct timing.
- [CMSampleBuffer.TimingPerSample.sequential(startingAt:)](./timingpersample/sequential%28startingat%29.md)
  All samples are adjacent to each other and have the same duration.
### Type Methods
- [static func sequential(presentationTimeOfFirstSample: CMTime, uniformDuration: CMTime, decodeTimeOfFirstSample: CMTime) -> CMSampleBuffer.TimingPerSample](./timingpersample/sequential%28presentationtimeoffirstsample,uniformduration,decodetimeoffirstsample%29.md)
  All samples are adjacent to each other and have the same duration.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/timingpersample)*