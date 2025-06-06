# CVBuffer

**Framework**: Core Video

An abstract base class that defines how to interact with data buffers.

#### Overview

A [`CVBuffer`](cvbuffer.md) serves as an abstract base class that defines how to interact with buffers of data. A buffer object can hold video, audio, or possibly other types of data. All the other buffer types within the Core Video framework, such as [`CVImageBuffer`](cvimagebuffer-q40.md) and [`CVPixelBuffer`](cvpixelbuffer-q2e.md), derive from [`CVBuffer`](cvbuffer.md). You can use the [`CVBuffer`](cvbuffer.md) programming interface on any Core Video buffer.

## Topics

### Working with attachments
- [func CVBufferHasAttachment(CVBuffer, CFString) -> Bool](cvbufferhasattachment(_:_:).md)
  Returns a Boolean value that indicates whether a Core Video buffer contains a specified attachment.
- [func CVBufferCopyAttachment(CVBuffer, CFString, UnsafeMutablePointer<CVAttachmentMode>?) -> CFTypeRef?](cvbuffercopyattachment(_:_:_:).md)
  Returns a copy of an attachment from a Core Video buffer.
- [func CVBufferCopyAttachments(CVBuffer, CVAttachmentMode) -> CFDictionary?](cvbuffercopyattachments(_:_:).md)
  Returns a copy of all attachments from a Core Video buffer.
- [func CVBufferSetAttachment(CVBuffer, CFString, CFTypeRef, CVAttachmentMode)](cvbuffersetattachment(_:_:_:_:).md)
  Sets or adds an attachment to a Core Video buffer.
- [func CVBufferSetAttachments(CVBuffer, CFDictionary, CVAttachmentMode)](cvbuffersetattachments(_:_:_:).md)
  Sets a dictionary of attachments on a Core Video buffer.
- [func CVBufferPropagateAttachments(CVBuffer, CVBuffer)](cvbufferpropagateattachments(_:_:).md)
  Copies all attachments that Core Video can propagate from one buffer to another.
- [func CVBufferRemoveAttachment(CVBuffer, CFString)](cvbufferremoveattachment(_:_:).md)
  Removes the attachment you specify from a Core Video buffer.
- [func CVBufferRemoveAllAttachments(CVBuffer)](cvbufferremoveallattachments(_:).md)
  Removes all attachments from a Core Video buffer.
- [func CVBufferGetAttachment(CVBuffer, CFString, UnsafeMutablePointer<CVAttachmentMode>?) -> Unmanaged<CFTypeRef>?](cvbuffergetattachment(_:_:_:).md)
  Retrieves a specific attachment of a Core Video buffer.
- [func CVBufferGetAttachments(CVBuffer, CVAttachmentMode) -> CFDictionary?](cvbuffergetattachments(_:_:).md)
  Retrieves all attachments of a Core Video buffer.
### Data types
- [class CVBuffer](cvbuffer.md)
  A reference to a Core Video buffer.
- [enum CVAttachmentMode](cvattachmentmode.md)
  The propagation modes of a Core Video buffer attachment.
### Constants
- [CVBuffer Attribute Keys](cvbuffer-attribute-keys.md)
  The attributes associated with Core Video buffers.
- [CVBuffer Attachment Keys](cvbuffer-attachment-keys.md)
  The attachment types for a Core Video buffer.

## See Also

- [Core Video Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Intro/CVProg_Intro.html#//apple_ref/doc/uid/TP40001536)
- [CVImageBuffer](cvimagebuffer-q40.md)
  An interface for managing different types of image data.
- [CVPixelBuffer](cvpixelbuffer-q2e.md)
  An image buffer that holds pixels in main memory.
- [CVPixelBufferPool](cvpixelbufferpool-77o.md)
  A utility object for managing a recyclable set of pixel buffer objects.
- [CVPixelFormatDescription](cvpixelformatdescription.md)
  An API that provides functions and types for defining custom pixel formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffer-nfm)*