# CMSetAttachment(_:key:value:attachmentMode:)

**Framework**: Core Media  
**Kind**: func

Sets or adds an attachment to an attachment bearer object.

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
func CMSetAttachment(_ target: CMAttachmentBearer, key: CFString, value: CFTypeRef?, attachmentMode: CMAttachmentMode)
```

#### Discussion

You can attach any Core Foundation object to a `CMAttachmentBearer` object to store additional information. `CMSetAttachment` stores an attachment identified by a key. If the key doesn’t currently exist for the `CMAttachmentBearer` object when you call this function, the function adds the new attachment. If the key does exist, the function replaces the existing attachment. In both cases the function increments the retain count of the attachment. The value can be any `CFType` but a `NULL` value results in an error. Given a [`CVBuffer`](https://developer.apple.com/documentation/CoreVideo/CVBuffer), `CMSetAttachment` is equivalent to `CVBufferSetAttachment`.

## Parameters

- `target`: The   object on which to add or set attachments.
- `key`: A   key identifying the desired attachment.
- `value`: A Core Foundation object attachment. If this parameter is  , the function returns an error.
- `attachmentMode`: Specifies the attachment mode for this attachment. Any given attachment key may exist in only one mode at a time.

## See Also

- [func CMGetAttachment(CMAttachmentBearer, key: CFString, attachmentModeOut: UnsafeMutablePointer<CMAttachmentMode>?) -> CFTypeRef?](cmgetattachment(_:key:attachmentmodeout:).md)
  Returns an attachment from an attachment bearer object.
- [func CMCopyDictionaryOfAttachments(allocator: CFAllocator?, target: CMAttachmentBearer, attachmentMode: CMAttachmentMode) -> sending CFDictionary?](cmcopydictionaryofattachments(allocator:target:attachmentmode:).md)
  Returns a dictionary of all attachments for an attachment bearer object.
- [func CMSetAttachments(CMAttachmentBearer, attachments: CFDictionary, attachmentMode: CMAttachmentMode)](cmsetattachments(_:attachments:attachmentmode:).md)
  Sets a dictionary of attachments on an attachment bearer object.
- [func CMRemoveAttachment(CMAttachmentBearer, key: CFString)](cmremoveattachment(_:key:).md)
  Removes a specific attachment from an attachment bearer object.
- [func CMRemoveAllAttachments(CMAttachmentBearer)](cmremoveallattachments(_:).md)
  Removes all attachments from an attachment bearer object.
- [func CMPropagateAttachments(CMAttachmentBearer, destination: CMAttachmentBearer)](cmpropagateattachments(_:destination:).md)
  Copies all propagable attachments from one attachment bearer object to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsetattachment(_:key:value:attachmentmode:))*