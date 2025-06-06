# NSTextAttachmentCellProtocol

**Framework**: AppKit  
**Kind**: protocol

A set of methods that declares the interface for objects that draw text attachment icons and handle mouse events on their icons.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSTextAttachmentCellProtocol : NSObjectProtocol
```

#### Overview

With the exceptions of [`cellBaselineOffset()`](nstextattachmentcellprotocol/cellbaselineoffset().md), [`attachment`](nstextattachmentcellprotocol/attachment.md), and [`attachment`](nstextattachmentcellprotocol/attachment.md), all of these methods are implemented by the [`NSCell`](nscell.md) class.For general information on text attachments, see [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) and [`NSTextView`](nstextview.md).

## Topics

### Setting the attachment
- [var attachment: NSTextAttachment?](nstextattachmentcellprotocol/attachment.md)
  Returns the text attachment object that owns the cell.
- [var attachment: NSTextAttachment?](nstextattachmentcellprotocol/attachment.md)
  Returns the text attachment object that owns the cell.
### Drawing the cell contents
- [func draw(withFrame: NSRect, in: NSView?)](nstextattachmentcellprotocol/draw(withframe:in:).md)
  Draws the cell’s image in the specified rectangle of the currently focused view.
- [func draw(withFrame: NSRect, in: NSView?, characterIndex: Int)](nstextattachmentcellprotocol/draw(withframe:in:characterindex:).md)
  Draws the cell’s image at the specified index point in the view.
- [func draw(withFrame: NSRect, in: NSView?, characterIndex: Int, layoutManager: NSLayoutManager)](nstextattachmentcellprotocol/draw(withframe:in:characterindex:layoutmanager:).md)
  Draws the cell’s image using the specified layout manager.
- [func highlight(Bool, withFrame: NSRect, in: NSView?)](nstextattachmentcellprotocol/highlight(_:withframe:in:).md)
  Draws the receiver’s image with optional highlighting.
### Providing the cell metrics
- [func cellSize() -> NSSize](nstextattachmentcellprotocol/cellsize.md)
  Returns the size of the attachment’s icon.
- [func cellBaselineOffset() -> NSPoint](nstextattachmentcellprotocol/cellbaselineoffset.md)
  Returns the text position where you draw the attachment cell’s image, relative to the current point established in the glyph layout.
- [func cellFrame(for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](nstextattachmentcellprotocol/cellframe(for:proposedlinefragment:glyphposition:characterindex:).md)
  Returns the frame of the cell to draw at the specified position in a text container.
### Responding to mouse events
- [func wantsToTrackMouse() -> Bool](nstextattachmentcellprotocol/wantstotrackmouse.md)
  Returns a Boolean value that indicates whether the attachment handles mouse events occurring over its image.
- [func wantsToTrackMouse(for: NSEvent, in: NSRect, of: NSView?, atCharacterIndex: Int) -> Bool](nstextattachmentcellprotocol/wantstotrackmouse(for:in:of:atcharacterindex:).md)
  Allows an attachment to specify the events for which it tracks the mouse.
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView?, untilMouseUp: Bool) -> Bool](nstextattachmentcellprotocol/trackmouse(with:in:of:untilmouseup:).md)
  Handles a mouse-down event on the cell’s image, and optionally waits until a mouse-up event
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView?, atCharacterIndex: Int, untilMouseUp: Bool) -> Bool](nstextattachmentcellprotocol/trackmouse(with:in:of:atcharacterindex:untilmouseup:).md)
  Handles a mouse-down event on the image at the specified character position.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSTextAttachmentCell](nstextattachmentcell-swift.class.md)

## See Also

- [class NSTextAttachment](nstextattachment.md)
  The values for the attachment characteristics of attributed strings and related objects.
- [class NSTextAttachmentViewProvider](nstextattachmentviewprovider.md)
  A container object that associates a text attachment at a particular document location with a view object.
- [class NSAdaptiveImageGlyph](nsadaptiveimageglyph.md)
  A data object for an emoji-like image that can appear in attributed text.
- [protocol NSTextAttachmentContainer](nstextattachmentcontainer.md)
  A set of methods that defines the interface to text attachment objects from a layout manager.
- [protocol NSTextAttachmentLayout](nstextattachmentlayout.md)
  A set of methods that defines the interface to attachment objects from a text layout manager.
- [class NSTextAttachmentCell](nstextattachmentcell-swift.class.md)
  An object that implements the functionality of the text attachment cell protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol)*