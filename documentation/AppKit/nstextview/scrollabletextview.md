# scrollableTextView()

**Framework**: AppKit  
**Kind**: method

**Availability**:
- macOS 10.14+

## Declaration

```swift
@MainActor
class func scrollableTextView() -> NSScrollView
```

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
- [func showFindIndicator(for: NSRange)](nstextview/showfindindicator(for:).md)
  Causes a temporary highlighting effect to appear around the visible portion (or portions) of the specified range.
- [class func scrollableDocumentContentTextView() -> NSScrollView](nstextview/scrollabledocumentcontenttextview.md)
- [class func scrollablePlainDocumentContentTextView() -> NSScrollView](nstextview/scrollableplaindocumentcontenttextview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/scrollabletextview())*