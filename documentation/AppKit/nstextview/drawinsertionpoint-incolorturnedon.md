# drawInsertionPoint(in:color:turnedOn:)

**Framework**: AppKit  
**Kind**: method

Draws or erases the insertion point.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawInsertionPoint(in rect: NSRect, color: NSColor, turnedOn flag: Bool)
```

#### Discussion

The focus must be locked on the receiver when this method is invoked. You should not need to invoke this method directly.

## Parameters

- `rect`: The rectangle in which to draw the insertion point.
- `color`: The color with which to draw the insertion point.
- `flag`:   to draw the insertion point,   to erase it.

## See Also

- [var backgroundColor: NSColor](nstextview/backgroundcolor.md)
  The receiver’s background color.
- [func lockFocus()](nsview/lockfocus.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
- [var insertionPointColor: NSColor!](nstextview/insertionpointcolor.md)
  The color of the insertion point.
- [func setNeedsDisplay(NSRect, avoidAdditionalLayout: Bool)](nstextview/setneedsdisplay(_:avoidadditionallayout:).md)
  Marks the receiver as requiring display.
- [var shouldDrawInsertionPoint: Bool](nstextview/shoulddrawinsertionpoint.md)
  A Boolean value that determines whether the receiver should draw its insertion point.
- [func drawBackground(in: NSRect)](nstextview/drawbackground(in:).md)
  Draws the background of the text view.
- [func setConstrainedFrameSize(NSSize)](nstextview/setconstrainedframesize(_:).md)
  Attempts to set the frame size as if by user action.
- [func cleanUpAfterDragOperation()](nstextview/cleanupafterdragoperation.md)
  Releases the drag information still existing after the dragging session has completed.
- [func showFindIndicator(for: NSRange)](nstextview/showfindindicator(for:).md)
  Causes a temporary highlighting effect to appear around the visible portion (or portions) of the specified range.
- [class func scrollableDocumentContentTextView() -> NSScrollView](nstextview/scrollabledocumentcontenttextview.md)
- [class func scrollablePlainDocumentContentTextView() -> NSScrollView](nstextview/scrollableplaindocumentcontenttextview.md)
- [class func scrollableTextView() -> NSScrollView](nstextview/scrollabletextview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/drawinsertionpoint(in:color:turnedon:))*