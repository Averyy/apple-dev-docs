# CVBufferSetAttachments(_:_:_:)

**Framework**: Core Video  
**Kind**: func

Sets a dictionary of attachments on a Core Video buffer.

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
func CVBufferSetAttachments(_ buffer: CVBuffer, _ theAttachments: CFDictionary, _ attachmentMode: CVAttachmentMode)
```

#### Discussion

This is a convenience function that calls [`CVBufferSetAttachment(_:_:_:_:)`](cvbuffersetattachment(_:_:_:_:).md) for each key-value pair in the given dictionary. All key-value pairs must be in the root level of the dictionary.

## Parameters

- `buffer`: The buffer on which to set the attachments.
- `theAttachments`: The dictionary of the attachments to set.
- `attachmentMode`: The attachment mode for this attachment. See   for possible values. Any given attachment key may exist in only one mode at a time.

## See Also

- [func CVBufferHasAttachment(CVBuffer, CFString) -> Bool](cvbufferhasattachment(_:_:).md)
  Returns a Boolean value that indicates whether a Core Video buffer contains a specified attachment.
- [func CVBufferCopyAttachment(CVBuffer, CFString, UnsafeMutablePointer<CVAttachmentMode>?) -> CFTypeRef?](cvbuffercopyattachment(_:_:_:).md)
  Returns a copy of an attachment from a Core Video buffer.
- [func CVBufferCopyAttachments(CVBuffer, CVAttachmentMode) -> CFDictionary?](cvbuffercopyattachments(_:_:).md)
  Returns a copy of all attachments from a Core Video buffer.
- [func CVBufferSetAttachment(CVBuffer, CFString, CFTypeRef, CVAttachmentMode)](cvbuffersetattachment(_:_:_:_:).md)
  Sets or adds an attachment to a Core Video buffer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffersetattachments(_:_:_:))*