# CMGetAttachment(_:key:attachmentModeOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern CFTypeRefCMGetAttachment(CMAttachmentBearerRef target, CFStringRef key, CMAttachmentMode *attachmentModeOut);
```

#### Return Value

The requested attachment object or `NULL` if not found.

#### Discussion

You can attach any Core Foundation object to a `CMAttachmentBearer` to store additional information. `CMGetAttachment` retrieves an attachment identified by a key. Given a [`CVBuffer`](../CoreVideo/cvbuffer.md), `CMGetAttachment` is equivalent to [`CVBufferCopyAttachment(_:_:_:)`](../CoreVideo/cvbuffercopyattachment%28_,_,_%29.md).

## Parameters

- `target`: Specifies the `CMAttachmentBearer` whose attachment you want to retrieve.
- `key`: Key in the form of a `CFString` identifying the desired attachment.
- `attachmentModeOut`: On output, `attachmentMode` points to the mode of the attachment. See [`CMAttachmentMode`](./cmattachmentmode.md)for possible values. May be `NULL`.

## See Also

### Processing Attachments
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
- [func CMPropagateAttachments(CMAttachmentBearer, destination: CMAttachmentBearer)](./cmpropagateattachments%28_,destination%29.md)
  Copies all propagable attachments from one attachment bearer object to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmgetattachment(_:key:attachmentmodeout:))*