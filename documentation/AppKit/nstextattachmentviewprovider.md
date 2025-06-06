# NSTextAttachmentViewProvider

**Framework**: AppKit  
**Kind**: class

A container object that associates a text attachment at a particular document location with a view object.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class NSTextAttachmentViewProvider
```

#### Overview

Use `NSTextAttachmentViewProvider` when you need to represent document locations in terms of an [`NSTextLocation`](nstextlocation.md) or an [`NSTextRange`](nstextrange.md) or you want to support view-based text attachments. The view provider controls the view placement and layout without requiring view classes to be aware of the text attachment coordination using a [`NSTextLayoutManager`](nstextlayoutmanager.md) in macOS 12 or iOS 15 and later.

## Topics

### Initializing a text attachment view
- [init(textAttachment: NSTextAttachment, parentView: NSView?, textLayoutManager: NSTextLayoutManager?, location: any NSTextLocation)](nstextattachmentviewprovider/init(textattachment:parentview:textlayoutmanager:location:).md)
  Creates a new text attachment view whose content starts at the location you provide.
### Defining the contents
- [var location: any NSTextLocation](nstextattachmentviewprovider/location.md)
  The location that indicates the start of the text attachment.
- [var textAttachment: NSTextAttachment?](nstextattachmentviewprovider/textattachment.md)
  The text attachment for this view.
- [var textLayoutManager: NSTextLayoutManager?](nstextattachmentviewprovider/textlayoutmanager.md)
  The text layout manager for this view.
- [var tracksTextAttachmentViewBounds: Bool](nstextattachmentviewprovider/trackstextattachmentviewbounds.md)
  A Boolean value that determines the text attachment’s bounds policy.
- [var view: NSView?](nstextattachmentviewprovider/view.md)
  The text attachment’s view.
### Defining a custom view hierarchy
- [func loadView()](nstextattachmentviewprovider/loadview.md)
  Draws the custom view hierarchy that text attachment view subclasses implement.
### Determining the Attachment’s Bounds
- [func attachmentBounds(for: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?, proposedLineFragment: CGRect, position: CGPoint) -> CGRect](nstextattachmentviewprovider/attachmentbounds(for:location:textcontainer:proposedlinefragment:position:).md)
  Returns the layout bounds for an attachment at a specific text location that contains the text attributes you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSTextAttachment](nstextattachment.md)
  The values for the attachment characteristics of attributed strings and related objects.
- [class NSAdaptiveImageGlyph](nsadaptiveimageglyph.md)
  A data object for an emoji-like image that can appear in attributed text.
- [protocol NSTextAttachmentContainer](nstextattachmentcontainer.md)
  A set of methods that defines the interface to text attachment objects from a layout manager.
- [protocol NSTextAttachmentLayout](nstextattachmentlayout.md)
  A set of methods that defines the interface to attachment objects from a text layout manager.
- [class NSTextAttachmentCell](nstextattachmentcell-swift.class.md)
  An object that implements the functionality of the text attachment cell protocol.
- [protocol NSTextAttachmentCellProtocol](nstextattachmentcellprotocol.md)
  A set of methods that declares the interface for objects that draw text attachment icons and handle mouse events on their icons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentviewprovider)*