# CMSampleBuffer.TimingPerSample

**Framework**: Core Media  
**Kind**: enum

Specifies timing of each sample in a sample buffer.

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
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/timingpersample)*