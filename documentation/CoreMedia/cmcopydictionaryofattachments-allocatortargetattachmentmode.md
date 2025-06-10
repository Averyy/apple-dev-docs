# CMCopyDictionaryOfAttachments(allocator:target:attachmentMode:)

**Framework**: Core Media  
**Kind**: func

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

#### Return Value

A Core Foundation dictionary with all attachments identified by their keys. If no attachment is present, the dictionary is empty. Returns `NULL` for an invalid attachment mode.

#### Discussion

`CMCopyDictionaryOfAttachments` is a convenience call that returns all attachments with their corresponding keys in a new [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary). Given a `CVBufferRef`, `CMCopyDictionaryOfAttachments` is similar to `CVBufferGetAttachments`, except that the `CFDictionary` that `CMCopyDictionaryOfAttachments` returns isn’t updated for later changes to the attachments.

## Parameters

- `allocator`: Allocator for the new dictionary; pass   or   to use the default allocator.
- `target`: Specifies the   whose attachments you want to obtain.
- `attachmentMode`: The mode of the attachments you want to obtain. See   for possible values.

## See Also

- [func CMGetAttachment(CMAttachmentBearer, key: CFString, attachmentModeOut: UnsafeMutablePointer<CMAttachmentMode>?) -> CFTypeRef?](cmgetattachment(_:key:attachmentmodeout:).md)
  Returns an attachment from an attachment bearer object.
- [func CMSetAttachment(CMAttachmentBearer, key: CFString, value: CFTypeRef?, attachmentMode: CMAttachmentMode)](cmsetattachment(_:key:value:attachmentmode:).md)
  Sets or adds an attachment to an attachment bearer object.
- [func CMSetAttachments(CMAttachmentBearer, attachments: CFDictionary, attachmentMode: CMAttachmentMode)](cmsetattachments(_:attachments:attachmentmode:).md)
  Sets a dictionary of attachments on an attachment bearer object.
- [func CMRemoveAttachment(CMAttachmentBearer, key: CFString)](cmremoveattachment(_:key:).md)
  Removes a specific attachment from an attachment bearer object.
- [func CMRemoveAllAttachments(CMAttachmentBearer)](cmremoveallattachments(_:).md)
  Removes all attachments from an attachment bearer object.
- [func CMPropagateAttachments(CMAttachmentBearer, destination: CMAttachmentBearer)](cmpropagateattachments(_:destination:).md)
  Copies all propagable attachments from one attachment bearer object to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmcopydictionaryofattachments(allocator:target:attachmentmode:))*