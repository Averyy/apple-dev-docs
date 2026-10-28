# CMRemoveAttachment(_:key:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Removes a specific attachment from an attachment bearer object.

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
func CMRemoveAttachment(_ target: CMAttachmentBearer, key: CFString)
```

```c
extern void CMRemoveAttachment(CMAttachmentBearerRef target, CFStringRef key);
```

## Discussion

If the attachment exists, the function removes the attachment and decrements the retain count. Given a [`CVBuffer`](../CoreVideo/cvbuffer.md), `CMRemoveAttachment` is equivalent to `CVBufferRemoveAttachment`.

## Parameters

- `target`: The `CMAttachmentBearer` containing the attachment to remove.
- `key`: Key in the form of a Core Foundation string identifying the desired attachment.

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
- [func CMRemoveAllAttachments(CMAttachmentBearer)](./cmremoveallattachments%28_%29.md)
  Removes all attachments from an attachment bearer object.
- [func CMPropagateAttachments(CMAttachmentBearer, destination: CMAttachmentBearer)](./cmpropagateattachments%28_,destination%29.md)
  Copies all propagable attachments from one attachment bearer object to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmremoveattachment(_:key:))*