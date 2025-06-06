# setConstrainedFrameSize(_:)

**Framework**: AppKit  
**Kind**: method

Attempts to set the frame size as if by user action.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setConstrainedFrameSize(_ desiredSize: NSSize)
```

#### Discussion

This method respects the receiver’s existing minimum and maximum sizes and by whether resizing is permitted.

## Parameters

- `desiredSize`: The new desired size.

## See Also

- [var minSize: NSSize](nstext/minsize.md)
  The receiver’s minimum size.
- [var isVerticallyResizable: Bool](nstext/isverticallyresizable.md)
  A Boolean that controls whether the receiver changes its height to fit the height of its text.
- [var isHorizontallyResizable: Bool](nstext/ishorizontallyresizable.md)
  A Boolean that controls whether the receiver changes its width to fit the width of its text.
- [var maxSize: NSSize](nstext/maxsize.md)
  The receiver’s maximum size.
- [func setNeedsDisplay(NSRect, avoidAdditionalLayout: Bool)](nstextview/setneedsdisplay(_:avoidadditionallayout:).md)
  Marks the receiver as requiring display.
- [var shouldDrawInsertionPoint: Bool](nstextview/shoulddrawinsertionpoint.md)
  A Boolean value that determines whether the receiver should draw its insertion point.
- [func drawInsertionPoint(in: NSRect, color: NSColor, turnedOn: Bool)](nstextview/drawinsertionpoint(in:color:turnedon:).md)
  Draws or erases the insertion point.
- [func drawBackground(in: NSRect)](nstextview/drawbackground(in:).md)
  Draws the background of the text view.
- [func cleanUpAfterDragOperation()](nstextview/cleanupafterdragoperation.md)
  Releases the drag information still existing after the dragging session has completed.
- [func showFindIndicator(for: NSRange)](nstextview/showfindindicator(for:).md)
  Causes a temporary highlighting effect to appear around the visible portion (or portions) of the specified range.
- [class func scrollableDocumentContentTextView() -> NSScrollView](nstextview/scrollabledocumentcontenttextview.md)
- [class func scrollablePlainDocumentContentTextView() -> NSScrollView](nstextview/scrollableplaindocumentcontenttextview.md)
- [class func scrollableTextView() -> NSScrollView](nstextview/scrollabletextview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/setconstrainedframesize(_:))*