# CVBufferSetAttachment(_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Sets or adds an attachment to a Core Video buffer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CVBufferSetAttachment(_ buffer: CVBuffer, _ key: CFString, _ value: CFTypeRef, _ attachmentMode: CVAttachmentMode)
```

#### Discussion

You can attach any Core Foundation object to a Core Video buffer to store additional information.

If it doesn’t exist for the buffer object, the system adds a new attachment. If the key does exist, the system replaces the existing attachment. In both cases, the system increases the retain count of the attachment.

You can also set attachments when creating a buffer by specifying them in the [`kCVBufferPropagatedAttachmentsKey`](kcvbufferpropagatedattachmentskey.md) or [`kCVBufferNonPropagatedAttachmentsKey`](kcvbuffernonpropagatedattachmentskey.md) attributes.

To retrieve attachments, use the [`CVBufferGetAttachment(_:_:_:)`](cvbuffergetattachment(_:_:_:).md) or [`CVBufferGetAttachments(_:_:)`](cvbuffergetattachments(_:_:).md) functions.

## Parameters

- `buffer`: The buffer on which to add or set an attachment.
- `key`: A string that identifies the attachment, which can be of any  doc://com.apple.documentation/documentation/corefoundation/cftype . See   and   for predefined values.
- `value`: The attachment in the form of a Core Foundation object. If this parameter is  , the function returns an error.
- `attachmentMode`: The attachment mode for this attachment. See   for possible values. Any given attachment key may exist in only one mode at a time.

## See Also

- [func CVBufferHasAttachment(CVBuffer, CFString) -> Bool](cvbufferhasattachment(_:_:).md)
  Returns a Boolean value that indicates whether a Core Video buffer contains a specified attachment.
- [func CVBufferCopyAttachment(CVBuffer, CFString, UnsafeMutablePointer<CVAttachmentMode>?) -> CFTypeRef?](cvbuffercopyattachment(_:_:_:).md)
  Returns a copy of an attachment from a Core Video buffer.
- [func CVBufferCopyAttachments(CVBuffer, CVAttachmentMode) -> CFDictionary?](cvbuffercopyattachments(_:_:).md)
  Returns a copy of all attachments from a Core Video buffer.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffersetattachment(_:_:_:_:))*