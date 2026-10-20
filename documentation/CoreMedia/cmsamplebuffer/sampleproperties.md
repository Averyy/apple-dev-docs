# CMSampleBuffer.SampleProperties

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

Information about a sample in the sample buffer.

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
struct SampleProperties
```

#### Overview

Each sample buffer holds a [`CMSampleBuffer.SamplePropertiesCollection`](./samplepropertiescollection.md) which provides this sample information for each sample in the sample buffer.

## Topics

### Initializers
- [init(size: Int?, timing: CMSampleTimingInfo, attachments: CMSampleBuffer.SampleAttachments)](./sampleproperties/init%28size,timing,attachments%29.md)
### Instance Properties
- [var attachments: CMSampleBuffer.SampleAttachments](./sampleproperties/attachments.md)
  Attachments of the sample.
- [var size: Int?](./sampleproperties/size.md)
  Size in bytes of the sample.
- [var timing: CMSampleTimingInfo](./sampleproperties/timing.md)
  Timing information of the sample.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleproperties)*