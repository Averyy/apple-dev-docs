# merge(_:mode:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Sets a collection of attachments on the object.

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
func merge(_ attachments: [String : Any], mode: CMAttachmentBearerAttachments.Mode)
```

## Parameters

- `attachments`: The attachments to set on this object.
- `mode`: The mode with which to add the attachments.

## See Also

### Managing Attachments
- [CMAttachmentBearerAttachments.Mode](./mode.md)
  An enumeration that defines the available attachment modes.
- [func removeAll()](./removeall%28%29.md)
  Removes all attachments from this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmattachmentbearerattachments/merge(_:mode:))*