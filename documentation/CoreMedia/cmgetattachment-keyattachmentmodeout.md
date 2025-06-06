# CMGetAttachment(_:key:attachmentModeOut:)

**Framework**: Core Media  
**Kind**: func

Returns an attachment from an attachment bearer object.

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
func CMGetAttachment(_ target: CMAttachmentBearer, key: CFString, attachmentModeOut: UnsafeMutablePointer<CMAttachmentMode>?) -> CFTypeRef?
```

#### Return Value

The requested attachment object or `NULL` if not found.

#### Discussion

You can attach any Core Foundation object to a `CMAttachmentBearer` to store additional information. `CMGetAttachment` retrieves an attachment identified by a key. Given a [`CVBuffer`](https://developer.apple.com/documentation/CoreVideo/CVBuffer), `CMGetAttachment` is equivalent to [`CVBufferCopyAttachment(_:_:_:)`](https://developer.apple.com/documentation/CoreVideo/CVBufferCopyAttachment(_:_:_:)).

## Parameters

- `target`: Specifies the   whose attachment you want to retrieve.
- `key`: Key in the form of a   identifying the desired attachment.
- `attachmentModeOut`: On output,   points to the mode of the attachment. See  for possible values. May be  .

## See Also

- [func CMCopyDictionaryOfAttachments(allocator: CFAllocator?, target: CMAttachmentBearer, attachmentMode: CMAttachmentMode) -> CFDictionary?](cmcopydictionaryofattachments(allocator:target:attachmentmode:).md)
  Returns a dictionary of all attachments for an attachment bearer object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmgetattachment(_:key:attachmentmodeout:))*