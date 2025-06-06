# CMSetAttachments(_:attachments:attachmentMode:)

**Framework**: Core Media  
**Kind**: func

Sets a dictionary of attachments on an attachment bearer object.

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
func CMSetAttachments(_ target: CMAttachmentBearer, attachments theAttachments: CFDictionary, attachmentMode: CMAttachmentMode)
```

#### Discussion

`CMSetAttachments` is a convenience call that in turn calls `CMSetAttachment` for each key and value in the given dictionary. All key value pairs must be in the root level of the dictionary.  Given a [`CVBuffer`](https://developer.apple.com/documentation/CoreVideo/CVBuffer), `CMSetAttachments` is equivalent to `CVBufferSetAttachments`.

## Parameters

- `target`: The target   to set the attachment to.
- `theAttachments`: The attachments to set, in the form of a Core Foundation dictionary.
- `attachmentMode`: Specifies the attachment mode for this attachment. A particular attachment key can only exist in a single mode at a time.

## See Also

- [func CMGetAttachment(CMAttachmentBearer, key: CFString, attachmentModeOut: UnsafeMutablePointer<CMAttachmentMode>?) -> CFTypeRef?](cmgetattachment(_:key:attachmentmodeout:).md)
  Returns an attachment from an attachment bearer object.
- [func CMCopyDictionaryOfAttachments(allocator: CFAllocator?, target: CMAttachmentBearer, attachmentMode: CMAttachmentMode) -> CFDictionary?](cmcopydictionaryofattachments(allocator:target:attachmentmode:).md)
  Returns a dictionary of all attachments for an attachment bearer object.
- [func CMSetAttachment(CMAttachmentBearer, key: CFString, value: CFTypeRef?, attachmentMode: CMAttachmentMode)](cmsetattachment(_:key:value:attachmentmode:).md)
  Sets or adds an attachment to an attachment bearer object.
- [func CMRemoveAttachment(CMAttachmentBearer, key: CFString)](cmremoveattachment(_:key:).md)
  Removes a specific attachment from an attachment bearer object.
- [func CMRemoveAllAttachments(CMAttachmentBearer)](cmremoveallattachments(_:).md)
  Removes all attachments from an attachment bearer object.
- [func CMPropagateAttachments(CMAttachmentBearer, destination: CMAttachmentBearer)](cmpropagateattachments(_:destination:).md)
  Copies all propagable attachments from one attachment bearer object to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsetattachments(_:attachments:attachmentmode:))*