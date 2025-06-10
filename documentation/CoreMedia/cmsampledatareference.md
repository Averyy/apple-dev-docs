# CMSampleDataReference

**Framework**: Core Media  
**Kind**: struct

References sample data in at a URL.

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
struct CMSampleDataReference
```

#### Overview

The size of the data is provided as [`totalSampleSize`](cmreadysamplebuffer/totalsamplesize.md).

## Topics

### Initializers
- [init(containerLocation: URL, byteOffset: Int)](cmsampledatareference/init(containerlocation:byteoffset:).md)
### Instance Properties
- [var byteOffset: Int](cmsampledatareference/byteoffset.md)
  Offset of the sample data in the container.
- [var containerLocation: URL](cmsampledatareference/containerlocation.md)
  Container of the sample data.

## Relationships

### Conforms To
- [CMSampleBuffer.Content](cmsamplebuffer/content.md)
- [CMSampleBuffer.ContentWithFormatDescription](cmsamplebuffer/contentwithformatdescription.md)
- [CMSampleBuffer.MultiSampleContent](cmsamplebuffer/multisamplecontent.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsampledatareference)*