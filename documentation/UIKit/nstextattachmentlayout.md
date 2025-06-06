# NSTextAttachmentLayout

**Framework**: UIKit  
**Kind**: protocol

A set of methods that defines the interface to attachment objects from a text layout manager.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
protocol NSTextAttachmentLayout : NSObjectProtocol
```

#### Overview

`The NSTextAttachmentLayout` protocol is the interface for working with attachment objects with an [`NSTextAttachmentViewProvider`](nstextattachmentviewprovider.md) using a [`NSTextLayoutManager`](nstextlayoutmanager.md) in macOS 12 and iOS 15 and later.

## Topics

### Determining the characteristics of an attachment
- [func attachmentBounds(for: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?, proposedLineFragment: CGRect, position: CGPoint) -> CGRect](nstextattachmentlayout/attachmentbounds(for:location:textcontainer:proposedlinefragment:position:).md)
  Returns the layout bounds of the attachment you specify.
- [func image(for: CGRect, attributes: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?) -> UIImage?](nstextattachmentlayout/image(for:attributes:location:textcontainer:).md)
  Returns the image object rendered at the bounds and inside the text container you specify.
- [func viewProvider(for: UIView?, location: any NSTextLocation, textContainer: NSTextContainer?) -> NSTextAttachmentViewProvider?](nstextattachmentlayout/viewprovider(for:location:textcontainer:).md)
  Returns the text attachment view provider corresponding to the file type.

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
- [protocol NSTextAttachmentContainer](nstextattachmentcontainer.md)
  A set of methods that defines the interface to text attachment objects from a layout manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachmentlayout)*