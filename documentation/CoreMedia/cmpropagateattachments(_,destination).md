# CMPropagateAttachments(_:destination:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Copies all propagable attachments from one attachment bearer object to another.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMPropagateAttachments(_ source: CMAttachmentBearer, destination: CMAttachmentBearer)
```

```c
extern void CMPropagateAttachments(CMAttachmentBearerRef source, CMAttachmentBearerRef destination);
```

#### Discussion

`CMPropagateAttachments` is a convenience call that copies all attachments with a mode of `kCMAttachmentMode_ShouldPropagate` from one buffer to another.  Given a [`CVBuffer`](../CoreVideo/cvbuffer.md), `CMPropagateAttachments` is equivalent to `CVBufferPropagateAttachments`.

## Parameters

- `source`: `CMAttachmentBearer` to copy attachments from.
- `destination`: `CMAttachmentBearer` to copy attachments to.

## See Also

### Processing Attachments
- [func CMGetAttachment(CMAttachmentBearer, key: CFString, attachmentModeOut: UnsafeMutablePointer<CMAttachmentMode>?) -> CFTypeRef?](./cmgetattachment%28_,key,attachmentmodeout%29.md)
  Returns an attachment from an attachment bearer object.
- [func CMCopyDictionaryOfAttachments(allocator: CFAllocator?, target: CMAttachmentBearer, attachmentMode: CMAttachmentMode) -> sending CFDictionary?](./cmcopydictionaryofattachments%28allocator,target,attachmentmode%29.md)
  Returns a dictionary of all attachments for an attachment bearer object.
- [func CMSetAttachment(CMAttachmentBearer, key: CFString, value: CFTypeRef?, attachmentMode: CMAttachmentMode)](./cmsetattachment%28_,key,value,attachmentmode%29.md)
  Sets or adds an attachment to an attachment bearer object.
- [func CMSetAttachments(CMAttachmentBearer, attachments: CFDictionary, attachmentMode: CMAttachmentMode)](./cmsetattachments%28_,attachments,attachmentmode%29.md)
  Sets a dictionary of attachments on an attachment bearer object.
- [func CMRemoveAttachment(CMAttachmentBearer, key: CFString)](./cmremoveattachment%28_,key%29.md)
  Removes a specific attachment from an attachment bearer object.
- [func CMRemoveAllAttachments(CMAttachmentBearer)](./cmremoveallattachments%28_%29.md)
  Removes all attachments from an attachment bearer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmpropagateattachments(_:destination:))*