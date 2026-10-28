# CVBufferRemoveAllAttachments(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Removes all attachments from a Core Video buffer.

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
func CVBufferRemoveAllAttachments(_ buffer: CVBuffer)
```

```c
extern void CVBufferRemoveAllAttachments(CVBufferRef buffer);
```

## Discussion

This function removes all attachments from a buffer and decrements their reference counts.

## Parameters

- `buffer`: The buffer whose attachments you want to remove.

## See Also

### Working with attachments
- [func CVBufferHasAttachment(CVBuffer, CFString) -> Bool](./cvbufferhasattachment%28_,_%29.md)
  Returns a Boolean value that indicates whether a Core Video buffer contains a specified attachment.
- [func CVBufferCopyAttachment(CVBuffer, CFString, UnsafeMutablePointer<CVAttachmentMode>?) -> CFTypeRef?](./cvbuffercopyattachment%28_,_,_%29.md)
  Returns a copy of an attachment from a Core Video buffer.
- [func CVBufferCopyAttachments(CVBuffer, CVAttachmentMode) -> CFDictionary?](./cvbuffercopyattachments%28_,_%29.md)
  Returns a copy of all attachments from a Core Video buffer.
- [func CVBufferSetAttachment(CVBuffer, CFString, CFTypeRef, CVAttachmentMode)](./cvbuffersetattachment%28_,_,_,_%29.md)
  Sets or adds an attachment to a Core Video buffer.
- [func CVBufferSetAttachments(CVBuffer, CFDictionary, CVAttachmentMode)](./cvbuffersetattachments%28_,_,_%29.md)
  Sets a dictionary of attachments on a Core Video buffer.
- [func CVBufferPropagateAttachments(CVBuffer, CVBuffer)](./cvbufferpropagateattachments%28_,_%29.md)
  Copies all attachments that Core Video can propagate from one buffer to another.
- [func CVBufferRemoveAttachment(CVBuffer, CFString)](./cvbufferremoveattachment%28_,_%29.md)
  Removes the attachment you specify from a Core Video buffer.
- [func CVBufferGetAttachment(CVBuffer, CFString, UnsafeMutablePointer<CVAttachmentMode>?) -> Unmanaged<CFTypeRef>?](./cvbuffergetattachment%28_,_,_%29.md)
  Retrieves a specific attachment of a Core Video buffer.
- [func CVBufferGetAttachments(CVBuffer, CVAttachmentMode) -> CFDictionary?](./cvbuffergetattachments%28_,_%29.md)
  Retrieves all attachments of a Core Video buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbufferremoveallattachments(_:))*