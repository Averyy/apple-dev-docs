# CMSampleBuffer.SampleProperties

**Framework**: Core Media  
**Kind**: struct

Information about a sample in the sample buffer.

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
struct SampleProperties
```

#### Overview

Each sample buffer holds a [`CMSampleBuffer.SamplePropertiesCollection`](cmsamplebuffer/samplepropertiescollection.md) which provides this sample information for each sample in the sample buffer.

## Topics

### Initializers
- [init(size: Int?, timing: CMSampleTimingInfo, attachments: CMSampleBuffer.SampleAttachments)](cmsamplebuffer/sampleproperties/init(size:timing:attachments:).md)
### Instance Properties
- [var attachments: CMSampleBuffer.SampleAttachments](cmsamplebuffer/sampleproperties/attachments.md)
  Attachments of the sample.
- [var size: Int?](cmsamplebuffer/sampleproperties/size.md)
  Size in bytes of the sample.
- [var timing: CMSampleTimingInfo](cmsamplebuffer/sampleproperties/timing.md)
  Timing information of the sample.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleproperties)*