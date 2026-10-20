# CVBufferSetAttachment(_:_:_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

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

```c
extern void CVBufferSetAttachment(CVBufferRef buffer, CFStringRef key, CFTypeRef value, CVAttachmentMode attachmentMode);
```

#### Discussion

You can attach any Core Foundation object to a Core Video buffer to store additional information.

If it doesn’t exist for the buffer object, the system adds a new attachment. If the key does exist, the system replaces the existing attachment. In both cases, the system increases the retain count of the attachment.

You can also set attachments when creating a buffer by specifying them in the [`kCVBufferPropagatedAttachmentsKey`](./kcvbufferpropagatedattachmentskey.md) or [`kCVBufferNonPropagatedAttachmentsKey`](./kcvbuffernonpropagatedattachmentskey.md) attributes.

To retrieve attachments, use the [`CVBufferGetAttachment(_:_:_:)`](./cvbuffergetattachment%28_,_,_%29.md) or [`CVBufferGetAttachments(_:_:)`](./cvbuffergetattachments%28_,_%29.md) functions.

## Parameters

- `buffer`: The buffer on which to add or set an attachment.
- `key`: A string that identifies the attachment, which can be of any [`CFTypeRef`](../CoreFoundation/cftyperef.md). See [CVBuffer Attachment Keys](./cvbuffer-attachment-keys.md) and [Image Buffer Attachment Keys](./image-buffer-attachment-keys.md) for predefined values.
- `value`: The attachment in the form of a Core Foundation object. If this parameter is `NULL`, the function returns an error.
- `attachmentMode`: The attachment mode for this attachment. See [`CVAttachmentMode`](./cvattachmentmode.md) for possible values. Any given attachment key may exist in only one mode at a time.

## See Also

### Working with attachments
- [func CVBufferHasAttachment(CVBuffer, CFString) -> Bool](./cvbufferhasattachment%28_,_%29.md)
  Returns a Boolean value that indicates whether a Core Video buffer contains a specified attachment.
- [func CVBufferCopyAttachment(CVBuffer, CFString, UnsafeMutablePointer<CVAttachmentMode>?) -> CFTypeRef?](./cvbuffercopyattachment%28_,_,_%29.md)
  Returns a copy of an attachment from a Core Video buffer.
- [func CVBufferCopyAttachments(CVBuffer, CVAttachmentMode) -> CFDictionary?](./cvbuffercopyattachments%28_,_%29.md)
  Returns a copy of all attachments from a Core Video buffer.
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
- [func CVBufferGetAttachments(CVBuffer, CVAttachmentMode) -> CFDictionary?](./cvbuffergetattachments%28_,_%29.md)
  Retrieves all attachments of a Core Video buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffersetattachment(_:_:_:_:))*