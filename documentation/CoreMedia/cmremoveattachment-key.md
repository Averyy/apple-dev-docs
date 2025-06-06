# CMRemoveAttachment(_:key:)

**Framework**: Core Media  
**Kind**: func

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

#### Discussion

If the attachment exists, the function removes the attachment and decrements the retain count. Given a [`CVBuffer`](https://developer.apple.com/documentation/CoreVideo/CVBuffer), `CMRemoveAttachment` is equivalent to `CVBufferRemoveAttachment`.

## Parameters

- `target`: The   containing the attachment to remove.
- `key`: Key in the form of a Core Foundation string identifying the desired attachment.

## See Also

- [func CMGetAttachment(CMAttachmentBearer, key: CFString, attachmentModeOut: UnsafeMutablePointer<CMAttachmentMode>?) -> CFTypeRef?](cmgetattachment(_:key:attachmentmodeout:).md)
  Returns an attachment from an attachment bearer object.
- [func CMCopyDictionaryOfAttachments(allocator: CFAllocator?, target: CMAttachmentBearer, attachmentMode: CMAttachmentMode) -> CFDictionary?](cmcopydictionaryofattachments(allocator:target:attachmentmode:).md)
  Returns a dictionary of all attachments for an attachment bearer object.
- [func CMSetAttachment(CMAttachmentBearer, key: CFString, value: CFTypeRef?, attachmentMode: CMAttachmentMode)](cmsetattachment(_:key:value:attachmentmode:).md)
  Sets or adds an attachment to an attachment bearer object.
- [func CMSetAttachments(CMAttachmentBearer, attachments: CFDictionary, attachmentMode: CMAttachmentMode)](cmsetattachments(_:attachments:attachmentmode:).md)
  Sets a dictionary of attachments on an attachment bearer object.
- [func CMRemoveAllAttachments(CMAttachmentBearer)](cmremoveallattachments(_:).md)
  Removes all attachments from an attachment bearer object.
- [func CMPropagateAttachments(CMAttachmentBearer, destination: CMAttachmentBearer)](cmpropagateattachments(_:destination:).md)
  Copies all propagable attachments from one attachment bearer object to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmremoveattachment(_:key:))*