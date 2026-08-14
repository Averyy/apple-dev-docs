# CMSampleBuffer.TimingPerSample

**Framework**: Core Media  
**Kind**: enum

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
- [CMSampleBuffer.TimingPerSample.distinct(_:)](cmsamplebuffer/timingpersample/distinct(_:).md)
  Each sample has distinct timing.
- [CMSampleBuffer.TimingPerSample.sequential(startingAt:)](cmsamplebuffer/timingpersample/sequential(startingat:).md)
  All samples are adjacent to each other and have the same duration.
### Type Methods
- [static func sequential(presentationTimeOfFirstSample: CMTime, uniformDuration: CMTime, decodeTimeOfFirstSample: CMTime) -> CMSampleBuffer.TimingPerSample](cmsamplebuffer/timingpersample/sequential(presentationtimeoffirstsample:uniformduration:decodetimeoffirstsample:).md)
  All samples are adjacent to each other and have the same duration.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/timingpersample)*