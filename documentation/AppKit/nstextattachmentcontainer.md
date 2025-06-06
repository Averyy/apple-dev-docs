# NSTextAttachmentContainer

**Framework**: AppKit  
**Kind**: protocol

A set of methods that defines the interface to text attachment objects from a layout manager.

**Availability**:
- macOS 10.11+

## Declaration

```swift
protocol NSTextAttachmentContainer : NSObjectProtocol
```

## Topics

### Getting the bounds
- [func attachmentBounds(for: NSTextContainer?, proposedLineFragment: CGRect, glyphPosition: CGPoint, characterIndex: Int) -> CGRect](nstextattachmentcontainer/attachmentbounds(for:proposedlinefragment:glyphposition:characterindex:).md)
  Returns the layout bounds of the text attachment to the layout manager.
### Getting the image
- [func image(forBounds: CGRect, textContainer: NSTextContainer?, characterIndex: Int) -> NSImage?](nstextattachmentcontainer/image(forbounds:textcontainer:characterindex:).md)
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
- [class NSTextAttachmentCell](nstextattachmentcell-swift.class.md)
  An object that implements the functionality of the text attachment cell protocol.
- [protocol NSTextAttachmentCellProtocol](nstextattachmentcellprotocol.md)
  A set of methods that declares the interface for objects that draw text attachment icons and handle mouse events on their icons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcontainer)*