# CVBufferHasAttachment(_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a Core Video buffer contains a specified attachment.

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
func CVBufferHasAttachment(_ buffer: CVBuffer, _ key: CFString) -> Bool
```

```c
extern Boolean CVBufferHasAttachment(CVBufferRef buffer, CFStringRef key);
```

#### Return Value

[`true`](../Swift/true.md) if the buffer contains the attachment; otherwise, [`false`](../Swift/false.md).

## Parameters

- `buffer`: A Core Video buffer to query.
- `key`: A string that identifies the attachment, which can be of any [`CFTypeRef`](../CoreFoundation/cftyperef.md).

## See Also

### Working with attachments
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
- [func CVBufferGetAttachments(CVBuffer, CVAttachmentMode) -> CFDictionary?](./cvbuffergetattachments%28_,_%29.md)
  Retrieves all attachments of a Core Video buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbufferhasattachment(_:_:))*