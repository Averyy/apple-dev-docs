# CMCopyDictionaryOfAttachments(allocator:target:attachmentMode:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns a dictionary of all attachments for an attachment bearer object.

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
func CMCopyDictionaryOfAttachments(allocator: CFAllocator?, target: CMAttachmentBearer, attachmentMode: CMAttachmentMode) -> sending CFDictionary?
```

```c
extern CFDictionaryRefCMCopyDictionaryOfAttachments(CFAllocatorRef allocator, CMAttachmentBearerRef target, CMAttachmentMode attachmentMode);
```

## Return Value

A Core Foundation dictionary with all attachments identified by their keys. If no attachment is present, the dictionary is empty. Returns `NULL` for an invalid attachment mode.

## Discussion

`CMCopyDictionaryOfAttachments` is a convenience call that returns all attachments with their corresponding keys in a new [`CFDictionary`](../CoreFoundation/cfdictionary.md). Given a `CVBufferRef`, `CMCopyDictionaryOfAttachments` is similar to `CVBufferGetAttachments`, except that the `CFDictionary` that `CMCopyDictionaryOfAttachments` returns isn’t updated for later changes to the attachments.

## Parameters

- `allocator`: Allocator for the new dictionary; pass [`kCFAllocatorDefault`](../CoreFoundation/kcfallocatordefault.md) or `NULL` to use the default allocator.
- `target`: Specifies the [`CMAttachmentBearer`](./cmattachmentbearer.md) whose attachments you want to obtain.
- `attachmentMode`: The mode of the attachments you want to obtain. See [`CMAttachmentMode`](./cmattachmentmode.md) for possible values.

## See Also

### Processing Attachments
- [func CMGetAttachment(CMAttachmentBearer, key: CFString, attachmentModeOut: UnsafeMutablePointer<CMAttachmentMode>?) -> CFTypeRef?](./cmgetattachment%28_,key,attachmentmodeout%29.md)
  Returns an attachment from an attachment bearer object.
- [func CMSetAttachment(CMAttachmentBearer, key: CFString, value: CFTypeRef?, attachmentMode: CMAttachmentMode)](./cmsetattachment%28_,key,value,attachmentmode%29.md)
  Sets or adds an attachment to an attachment bearer object.
- [func CMSetAttachments(CMAttachmentBearer, attachments: CFDictionary, attachmentMode: CMAttachmentMode)](./cmsetattachments%28_,attachments,attachmentmode%29.md)
  Sets a dictionary of attachments on an attachment bearer object.
- [func CMRemoveAttachment(CMAttachmentBearer, key: CFString)](./cmremoveattachment%28_,key%29.md)
  Removes a specific attachment from an attachment bearer object.
- [func CMRemoveAllAttachments(CMAttachmentBearer)](./cmremoveallattachments%28_%29.md)
  Removes all attachments from an attachment bearer object.
- [func CMPropagateAttachments(CMAttachmentBearer, destination: CMAttachmentBearer)](./cmpropagateattachments%28_,destination%29.md)
  Copies all propagable attachments from one attachment bearer object to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmcopydictionaryofattachments(allocator:target:attachmentmode:))*