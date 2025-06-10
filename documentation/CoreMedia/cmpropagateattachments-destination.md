# CMPropagateAttachments(_:destination:)

**Framework**: Core Media  
**Kind**: func

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

#### Discussion

`CMPropagateAttachments` is a convenience call that copies all attachments with a mode of `kCMAttachmentMode_ShouldPropagate` from one buffer to another.  Given a [`CVBuffer`](https://developer.apple.com/documentation/CoreVideo/CVBuffer), `CMPropagateAttachments` is equivalent to `CVBufferPropagateAttachments`.

## Parameters

- `source`:   to copy attachments from.
- `destination`:   to copy attachments to.

## See Also

- [func CMGetAttachment(CMAttachmentBearer, key: CFString, attachmentModeOut: UnsafeMutablePointer<CMAttachmentMode>?) -> CFTypeRef?](cmgetattachment(_:key:attachmentmodeout:).md)
  Returns an attachment from an attachment bearer object.
- [func CMCopyDictionaryOfAttachments(allocator: CFAllocator?, target: CMAttachmentBearer, attachmentMode: CMAttachmentMode) -> sending CFDictionary?](cmcopydictionaryofattachments(allocator:target:attachmentmode:).md)
  Returns a dictionary of all attachments for an attachment bearer object.
- [func CMSetAttachment(CMAttachmentBearer, key: CFString, value: CFTypeRef?, attachmentMode: CMAttachmentMode)](cmsetattachment(_:key:value:attachmentmode:).md)
  Sets or adds an attachment to an attachment bearer object.
- [func CMSetAttachments(CMAttachmentBearer, attachments: CFDictionary, attachmentMode: CMAttachmentMode)](cmsetattachments(_:attachments:attachmentmode:).md)
  Sets a dictionary of attachments on an attachment bearer object.
- [func CMRemoveAttachment(CMAttachmentBearer, key: CFString)](cmremoveattachment(_:key:).md)
  Removes a specific attachment from an attachment bearer object.
- [func CMRemoveAllAttachments(CMAttachmentBearer)](cmremoveallattachments(_:).md)
  Removes all attachments from an attachment bearer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmpropagateattachments(_:destination:))*