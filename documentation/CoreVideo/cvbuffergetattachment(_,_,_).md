# CVBufferGetAttachment(_:_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Retrieves a specific attachment of a Core Video buffer.

**Availability**:
- iOS 4.0+ - Deprecated in 15.0 (renamed: CVBufferCopyAttachment(_:_:_:))
- iPadOS 4.0+ - Deprecated in 15.0 (renamed: CVBufferCopyAttachment(_:_:_:))
- Mac Catalyst 13.1+ - Deprecated in 15.0 (renamed: CVBufferCopyAttachment(_:_:_:))
- macOS 10.4+ - Deprecated in 12.0 (renamed: CVBufferCopyAttachment(_:_:_:))
- tvOS 9.0+ - Deprecated in 15.0 (renamed: CVBufferCopyAttachment(_:_:_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: CVBufferCopyAttachment(_:_:_:))
- watchOS 4.0+ - Deprecated in 8.0 (renamed: CVBufferCopyAttachment(_:_:_:))

> **Deprecated**: Use [`CVBufferCopyAttachment(_:_:_:)`](./cvbuffercopyattachment%28_,_,_%29.md) instead.

## Declaration

```swift
func CVBufferGetAttachment(_ buffer: CVBuffer, _ key: CFString, _ attachmentMode: UnsafeMutablePointer<CVAttachmentMode>?) -> Unmanaged<CFTypeRef>?
```

```c
extern CFTypeRefCVBufferGetAttachment(CVBufferRef buffer, CFStringRef key, CVAttachmentMode *attachmentMode);
```

## Return Value

The specified attachment, if it exists.

## Parameters

- `buffer`: The buffer whose attachment you want to retrieve.
- `key`: A string that identifies the attachment, which can be of any [`CFTypeRef`](../CoreFoundation/cftyperef.md). See [CVBuffer Attachment Keys](./cvbuffer-attachment-keys.md) and [Image Buffer Attachment Keys](./image-buffer-attachment-keys.md) for predefined values.
- `attachmentMode`: On output, this value points to the mode of the attachment. See [`CVAttachmentMode`](./cvattachmentmode.md) for possible values. This value is [`nil`](../ObjectiveC/nil-227m0.md) if the buffer doesn’t define an attachment mode.

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
- [func CVBufferGetAttachments(CVBuffer, CVAttachmentMode) -> CFDictionary?](./cvbuffergetattachments%28_,_%29.md)
  Retrieves all attachments of a Core Video buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffergetattachment(_:_:_:))*