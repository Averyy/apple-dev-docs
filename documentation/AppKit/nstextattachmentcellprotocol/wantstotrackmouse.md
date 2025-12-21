# wantsToTrackMouse()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether the attachment handles mouse events occurring over its image.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func wantsToTrackMouse() -> Bool
```

#### Discussion

The default implementation of this method returns [`true`](https://developer.apple.com/documentation/Swift/true). The [`NSView`](nsview.md) containing the cell should invoke this method before sending a [`trackMouse(with:in:of:untilMouseUp:)`](nstextattachmentcellprotocol/trackmouse(with:in:of:untilmouseup:).md) message.

For an attachment in an attributed string, if the attachment cell returns [`false`](https://developer.apple.com/documentation/Swift/false), its attachment character should be selected rather than the cell being asked to track the mouse. This results in the attachment icon behaving as any regular glyph in text.

## See Also

- [func wantsToTrackMouse(for: NSEvent, in: NSRect, of: NSView?, atCharacterIndex: Int) -> Bool](nstextattachmentcellprotocol/wantstotrackmouse(for:in:of:atcharacterindex:).md)
  Allows an attachment to specify the events for which it tracks the mouse.
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView?, untilMouseUp: Bool) -> Bool](nstextattachmentcellprotocol/trackmouse(with:in:of:untilmouseup:).md)
  Handles a mouse-down event on the cell’s image, and optionally waits until a mouse-up event
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView?, atCharacterIndex: Int, untilMouseUp: Bool) -> Bool](nstextattachmentcellprotocol/trackmouse(with:in:of:atcharacterindex:untilmouseup:).md)
  Handles a mouse-down event on the image at the specified character position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/wantstotrackmouse())*