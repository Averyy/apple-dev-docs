# NSTextAttachmentContainer

**Framework**: UIKit  
**Kind**: protocol

A set of methods that defines the interface to text attachment objects from a layout manager.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSTextAttachmentContainer : NSObjectProtocol
```

## Topics

### Getting the bounds
- [func attachmentBounds(for: NSTextContainer?, proposedLineFragment: CGRect, glyphPosition: CGPoint, characterIndex: Int) -> CGRect](nstextattachmentcontainer/attachmentbounds(for:proposedlinefragment:glyphposition:characterindex:).md)
  Returns the layout bounds of the text attachment to the layout manager.
### Getting the image
- [func image(forBounds: CGRect, textContainer: NSTextContainer?, characterIndex: Int) -> UIImage?](nstextattachmentcontainer/image(forbounds:textcontainer:characterindex:).md)
  Returns the image object that the layout manager renders in the specified image bounds rectangle inside the text container.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSTextAttachment](nstextattachment.md)

## See Also

- [class NSTextAttachment](nstextattachment.md)
  The values for the attachment characteristics of attributed strings and related objects.
- [class NSTextAttachmentViewProvider](nstextattachmentviewprovider.md)
  A container object that associates a text attachment at a particular document location with a view object.
- [class NSAdaptiveImageGlyph](nsadaptiveimageglyph.md)
  A data object for an emoji-like image that can appear in attributed text.
- [protocol NSTextAttachmentLayout](nstextattachmentlayout.md)
  A set of methods that defines the interface to attachment objects from a text layout manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachmentcontainer)*