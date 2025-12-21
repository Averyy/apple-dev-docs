# CMSampleDataReference

**Framework**: Core Media  
**Kind**: struct

References sample data in at a URL.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

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

## See Also

- [CMSampleBuffer](cmsamplebuffer-api.md)
  An object that contains zero or more media samples of a uniform media type.
- [CMBlockBuffer](cmblockbuffer-api.md)
  An object the system uses to move blocks of memory through a processing system.
- [CMTaggedBufferGroup](cmtaggedbuffergroup.md)
  Objective-C types and interfaces for working with Core Media tagged buffer groups.
- [CMFormatDescription](cmformatdescription-api.md)
  A media format descriptor that describes the samples in a sample buffer.
- [CMAttachment](cmattachment-api.md)
  Add supporting metadata to sample buffers.
- [struct CMTaggedBuffer](cmtaggedbuffer.md)
  An instance of a media buffer containing metadata tags.
- [struct CMMutableDataBlockBuffer](cmmutabledatablockbuffer.md)
  A block buffer that provides read-write access to a range of bytes.
- [struct CMReadOnlyDataBlockBuffer](cmreadonlydatablockbuffer.md)
  A block buffer that provides read-only access to the a range of bytes.
- [struct CMReadySampleBuffer](cmreadysamplebuffer.md)
  Buffer carrying readily available samples of media data.
- [struct CMTaggedDynamicBuffer](cmtaggeddynamicbuffer.md)
  Contains a collection of tags associated with a read-only media buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsampledatareference)*