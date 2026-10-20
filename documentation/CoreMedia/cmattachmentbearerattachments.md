# CMAttachmentBearerAttachments

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

A structure that contains attachments.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct CMAttachmentBearerAttachments
```

## Topics

### Inspecting Attachments
- [var propagated: [String : Any]](./cmattachmentbearerattachments/propagated.md)
  A dictionary of attachments to copy when propagating attachments from one object to another.
- [var nonPropagated: [String : Any]](./cmattachmentbearerattachments/nonpropagated.md)
  A dictionary of attachments to not copy when propagating attachments from one object to another.
### Accessing Attachments
- [subscript(String) -> CMAttachmentBearerAttachments.Value?](./cmattachmentbearerattachments/subscript%28_%29-8uau0.md)
  Gets the value associated with the specified attachment.
- [subscript(CMSampleBuffer.AttachmentKey) -> CMAttachmentBearerAttachments.Value?](./cmattachmentbearerattachments/subscript%28_%29-74jgw.md)
  Gets the value associated with the specified attachment key.
- [CMAttachmentBearerAttachments.Value](./cmattachmentbearerattachments/value.md)
  An enumeration of attachment values.
### Managing Attachments
- [func merge([String : Any], mode: CMAttachmentBearerAttachments.Mode)](./cmattachmentbearerattachments/merge%28_,mode%29.md)
  Sets a collection of attachments on the object.
- [CMAttachmentBearerAttachments.Mode](./cmattachmentbearerattachments/mode.md)
  An enumeration that defines the available attachment modes.
- [func removeAll()](./cmattachmentbearerattachments/removeall%28%29.md)
  Removes all attachments from this object.

## See Also

### Processing Attachments
- [var attachments: CMAttachmentBearerAttachments](./cmattachmentbearerprotocol/attachments.md)
  All attachments for this object.
- [func propagateAttachments<T>(to: T)](./cmattachmentbearerprotocol/propagateattachments%28to%29.md)
  Copies all propagable attachments from one attachment bearer object to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmattachmentbearerattachments)*