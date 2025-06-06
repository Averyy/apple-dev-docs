# CVBuffer Attribute Keys

**Framework**: Core Video

The attributes associated with Core Video buffers.

#### Overview

These attributes let you set multiple attachments at the time of buffer creation, rather than having to call [`CVBufferSetAttachment(_:_:_:_:)`](cvbuffersetattachment(_:_:_:_:).md) for each attachment.

## Topics

### Constants
- [let kCVBufferPropagatedAttachmentsKey: CFString](kcvbufferpropagatedattachmentskey.md)
  Attachments that should be copied when using the [`CVBufferPropagateAttachments(_:_:)`](cvbufferpropagateattachments(_:_:).md) function (type `CFDictionary`, containing a list of attachments as key-value pairs).
- [let kCVBufferNonPropagatedAttachmentsKey: CFString](kcvbuffernonpropagatedattachmentskey.md)
  Attachments that should not be copied when using the [`CVBufferPropagateAttachments(_:_:)`](cvbufferpropagateattachments(_:_:).md) function (type `CFDictionary`, containing a list of attachments as key-value pairs).

## See Also

- [CVBuffer Attachment Keys](cvbuffer-attachment-keys.md)
  The attachment types for a Core Video buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffer-attribute-keys)*