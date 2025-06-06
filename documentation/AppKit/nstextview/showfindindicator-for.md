# showFindIndicator(for:)

**Framework**: AppKit  
**Kind**: method

Causes a temporary highlighting effect to appear around the visible portion (or portions) of the specified range.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func showFindIndicator(for charRange: NSRange)
```

#### Discussion

This method supports lozenge-style indication of find results. The indicators automatically disappear after a certain period of time, or when the method is called again, or when any of a number of changes occur to the view (such as changes to text, view size, or view position).

This method does not itself scroll the specified range to be visible; any desired scrolling should be done before this method is called, first, because the method acts only on the visible portion of the specified range, and, second, because scrolling causes the indicators to disappear. Calling this method with a zero-length range always removes any existing indicators.

## Parameters

- `charRange`: The character range around which indicators appear.

## See Also

- [func setNeedsDisplay(NSRect, avoidAdditionalLayout: Bool)](nstextview/setneedsdisplay(_:avoidadditionallayout:).md)
  Marks the receiver as requiring display.
- [var shouldDrawInsertionPoint: Bool](nstextview/shoulddrawinsertionpoint.md)
  A Boolean value that determines whether the receiver should draw its insertion point.
- [func drawInsertionPoint(in: NSRect, color: NSColor, turnedOn: Bool)](nstextview/drawinsertionpoint(in:color:turnedon:).md)
  Draws or erases the insertion point.
- [func drawBackground(in: NSRect)](nstextview/drawbackground(in:).md)
  Draws the background of the text view.
- [func setConstrainedFrameSize(NSSize)](nstextview/setconstrainedframesize(_:).md)
  Attempts to set the frame size as if by user action.
- [func cleanUpAfterDragOperation()](nstextview/cleanupafterdragoperation.md)
  Releases the drag information still existing after the dragging session has completed.
- [class func scrollableDocumentContentTextView() -> NSScrollView](nstextview/scrollabledocumentcontenttextview.md)
- [class func scrollablePlainDocumentContentTextView() -> NSScrollView](nstextview/scrollableplaindocumentcontenttextview.md)
- [class func scrollableTextView() -> NSScrollView](nstextview/scrollabletextview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/showfindindicator(for:))*