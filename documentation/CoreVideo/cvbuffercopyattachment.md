# CVBufferCopyAttachment(_:_:_:)

**Framework**: Core Video  
**Kind**: func

Returns a copy of an attachment from a Core Video buffer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func CVBufferCopyAttachment(_ buffer: CVBuffer, _ key: CFString, _ attachmentMode: UnsafeMutablePointer<CVAttachmentMode>?) -> CFTypeRef?
```

#### Return Value

The requested attachment, or `nil` if no attachment for the specified key exists.

#### Discussion

This function returns a retained attachment value, which you need to release when you’re done with it.

## Parameters

- `buffer`: A buffer with an attachment to copy.
- `key`: A string that identifies the attachment, which can be of any  doc://com.apple.documentation/documentation/corefoundation/cftype . See   and   for predefined values.
- `attachmentMode`: On output, this value points to the mode of the attachment. See   for possible values. This value is   if the buffer doesn’t define an attachment mode.

## See Also

- [func CVBufferHasAttachment(CVBuffer, CFString) -> Bool](cvbufferhasattachment(_:_:).md)
  Returns a Boolean value that indicates whether a Core Video buffer contains a specified attachment.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffercopyattachment(_:_:_:))*