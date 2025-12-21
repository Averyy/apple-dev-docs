# CMTaggedBuffer

**Framework**: Core Media  
**Kind**: struct

An instance of a media buffer containing metadata tags.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct CMTaggedBuffer
```

## Topics

### Creating Tagged Buffers
- [init(tags: [CMTag], buffer: CMTaggedBuffer.Buffer)](cmtaggedbuffer/init(tags:buffer:).md)
  Creates a new tagged buffer from tags and an existing media buffer.
- [init(tags: [CMTag], sampleBuffer: CMSampleBuffer)](cmtaggedbuffer/init(tags:samplebuffer:).md)
  Creates a new tagged buffer from tags and an existing sample buffer.
- [init(tags: [CMTag], pixelBuffer: CVPixelBuffer)](cmtaggedbuffer/init(tags:pixelbuffer:).md)
  Creates a new tagged buffer from tags and an existing pixel buffer.
### Inspecting Data
- [let tags: [CMTag]](cmtaggedbuffer/tags.md)
  The tags for this buffer.
- [let buffer: CMTaggedBuffer.Buffer](cmtaggedbuffer/buffer-swift.property.md)
  The underlying buffer containing media data.
### Buffer Wrappers
- [CMTaggedBuffer.Buffer](cmtaggedbuffer/buffer-swift.enum.md)
  A wrapper type for the underlying buffer of a tagged buffer.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

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
- [struct CMMutableDataBlockBuffer](cmmutabledatablockbuffer.md)
  A block buffer that provides read-write access to a range of bytes.
- [struct CMReadOnlyDataBlockBuffer](cmreadonlydatablockbuffer.md)
  A block buffer that provides read-only access to the a range of bytes.
- [struct CMReadySampleBuffer](cmreadysamplebuffer.md)
  Buffer carrying readily available samples of media data.
- [struct CMSampleDataReference](cmsampledatareference.md)
  References sample data in at a URL.
- [struct CMTaggedDynamicBuffer](cmtaggeddynamicbuffer.md)
  Contains a collection of tags associated with a read-only media buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffer)*