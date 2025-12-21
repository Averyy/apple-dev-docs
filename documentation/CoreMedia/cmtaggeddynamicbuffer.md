# CMTaggedDynamicBuffer

**Framework**: Core Media  
**Kind**: struct

Contains a collection of tags associated with a read-only media buffer.

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
struct CMTaggedDynamicBuffer
```

## Topics

### Initializers
- [init(tags: [CMTag], content: CVReadOnlyPixelBuffer)](cmtaggeddynamicbuffer/init(tags:content:)-1hscu.md)
- [init(tags: [CMTag], content: CMTaggedDynamicBuffer.Content)](cmtaggeddynamicbuffer/init(tags:content:)-1ttie.md)
- [init(tags: [CMTag], content: CMReadySampleBuffer<CVReadOnlyPixelBuffer>)](cmtaggeddynamicbuffer/init(tags:content:)-5jtjt.md)
- [init(tags: [CMTag], content: CMReadySampleBuffer<CMReadOnlyDataBlockBuffer>)](cmtaggeddynamicbuffer/init(tags:content:)-5xcim.md)
- [init(unsafeBuffer: sending CMTaggedBuffer)](cmtaggeddynamicbuffer/init(unsafebuffer:).md)
### Instance Properties
- [var content: CMTaggedDynamicBuffer.Content](cmtaggeddynamicbuffer/content-swift.property.md)
  Buffer containing media.
- [var tags: [CMTag]](cmtaggeddynamicbuffer/tags.md)
  Tags associated with the content.
### Instance Methods
- [func withUnsafeTaggedBuffer<R>((CMTaggedBuffer) throws -> sending R) rethrows -> sending R](cmtaggeddynamicbuffer/withunsafetaggedbuffer(_:).md)
### Enumerations
- [CMTaggedDynamicBuffer.Content](cmtaggeddynamicbuffer/content-swift.enum.md)
  A read-only buffer associated with the tags.

## Relationships

### Conforms To
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
- [struct CMSampleDataReference](cmsampledatareference.md)
  References sample data in at a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggeddynamicbuffer)*