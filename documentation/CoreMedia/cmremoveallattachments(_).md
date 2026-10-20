# CMRemoveAllAttachments(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Removes all attachments from an attachment bearer object.

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
func CMRemoveAllAttachments(_ target: CMAttachmentBearer)
```

```c
extern void CMRemoveAllAttachments(CMAttachmentBearerRef target);
```

#### Discussion

While `CMRemoveAttachment` removes a specific attachment identified by a key, `CMRemoveAllAttachments` removes all attachments of a `CMAttachmentBearer` and decrements their retain counts.  Given a [`CVBuffer`](../CoreVideo/cvbuffer.md), `CMRemoveAllAttachments` is equivalent to `CVBufferRemoveAllAttachments`.

## Parameters

- `target`: The `CMAttachmentBearer` whose attachment you want to remove.

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
- [func CMPropagateAttachments(CMAttachmentBearer, destination: CMAttachmentBearer)](./cmpropagateattachments%28_,destination%29.md)
  Copies all propagable attachments from one attachment bearer object to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmremoveallattachments(_:))*