# CVBufferGetAttachments(_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Retrieves all attachments of a Core Video buffer.

**Availability**:
- iOS 4.0+ - Deprecated in 15.0 (renamed: CVBufferCopyAttachments(_:_:))
- iPadOS 4.0+ - Deprecated in 15.0 (renamed: CVBufferCopyAttachments(_:_:))
- Mac Catalyst 13.1+ - Deprecated in 15.0 (renamed: CVBufferCopyAttachments(_:_:))
- macOS 10.4+ - Deprecated in 12.0 (renamed: CVBufferCopyAttachments(_:_:))
- tvOS 9.0+ - Deprecated in 15.0 (renamed: CVBufferCopyAttachments(_:_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: CVBufferCopyAttachments(_:_:))
- watchOS 4.0+ - Deprecated in 8.0 (renamed: CVBufferCopyAttachments(_:_:))

> **Deprecated**: Use [`CVBufferCopyAttachments(_:_:)`](./cvbuffercopyattachments%28_,_%29.md) instead.

## Declaration

```swift
func CVBufferGetAttachments(_ buffer: CVBuffer, _ attachmentMode: CVAttachmentMode) -> CFDictionary?
```

```c
extern CFDictionaryRefCVBufferGetAttachments(CVBufferRef buffer, CVAttachmentMode attachmentMode);
```

## Return Value

A Core Foundation dictionary with all attachments identified by keys, or [`nil`](../ObjectiveC/nil-227m0.md) if the attachment mode is invalid. The dictionary is empty if the buffer has no attachments.

## Parameters

- `buffer`: The buffer whose attachments you want to retrieve.
- `attachmentMode`: The mode of the attachments you want to retrieve. See [`CVAttachmentMode`](./cvattachmentmode.md) for possible values.

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
- [func CVBufferRemoveAllAttachments(CVBuffer)](./cvbufferremoveallattachments%28_%29.md)
  Removes all attachments from a Core Video buffer.
- [func CVBufferGetAttachment(CVBuffer, CFString, UnsafeMutablePointer<CVAttachmentMode>?) -> Unmanaged<CFTypeRef>?](./cvbuffergetattachment%28_,_,_%29.md)
  Retrieves a specific attachment of a Core Video buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffergetattachments(_:_:))*