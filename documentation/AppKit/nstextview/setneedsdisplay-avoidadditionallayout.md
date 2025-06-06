# setNeedsDisplay(_:avoidAdditionalLayout:)

**Framework**: AppKit  
**Kind**: method

Marks the receiver as requiring display.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setNeedsDisplay(_ rect: NSRect, avoidAdditionalLayout flag: Bool)
```

#### Discussion

`NSTextView` overrides the `NSView` [`setNeedsDisplay(_:)`](nsview/setneedsdisplay(_:).md) method to invoke this method with a `flag` argument of [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `rect`: The rectangle in which display is required.
- `flag`: A value of   causes the receiver to not perform any layout, even if this means that portions of the text view remain empty. Otherwise the receiver performs at least as much layout as needed to display  .

## See Also

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
- [func showFindIndicator(for: NSRange)](nstextview/showfindindicator(for:).md)
  Causes a temporary highlighting effect to appear around the visible portion (or portions) of the specified range.
- [class func scrollableDocumentContentTextView() -> NSScrollView](nstextview/scrollabledocumentcontenttextview.md)
- [class func scrollablePlainDocumentContentTextView() -> NSScrollView](nstextview/scrollableplaindocumentcontenttextview.md)
- [class func scrollableTextView() -> NSScrollView](nstextview/scrollabletextview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/setneedsdisplay(_:avoidadditionallayout:))*