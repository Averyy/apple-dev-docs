# drawBackground(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the background of the text view.

**Availability**:
- macOS

## Declaration

```swift
func drawBackground(in rect: NSRect)
```

```objc
- (void) drawViewBackgroundInRect:(NSRect) rect;
```

#### Discussion

Subclasses can override this method to perform additional drawing behind the text.

## Parameters

- `rect`: The rectangle in which to draw the background.

## See Also

### Controlling text display
- [func setNeedsDisplay(NSRect, avoidAdditionalLayout: Bool)](./setneedsdisplay%28_,avoidadditionallayout%29.md)
  Marks the receiver as requiring display.
- [var shouldDrawInsertionPoint: Bool](./shoulddrawinsertionpoint.md)
  A Boolean value that determines whether the receiver should draw its insertion point.
- [func drawInsertionPoint(in: NSRect, color: NSColor, turnedOn: Bool)](./drawinsertionpoint%28in,color,turnedon%29.md)
  Draws or erases the insertion point.
- [func setConstrainedFrameSize(NSSize)](./setconstrainedframesize%28_%29.md)
  Attempts to set the frame size as if by user action.
- [func cleanUpAfterDragOperation()](./cleanupafterdragoperation%28%29.md)
  Releases the drag information still existing after the dragging session has completed.
- [func showFindIndicator(for: NSRange)](./showfindindicator%28for%29.md)
  Causes a temporary highlighting effect to appear around the visible portion (or portions) of the specified range.
- [class func scrollableDocumentContentTextView() -> NSScrollView](./scrollabledocumentcontenttextview%28%29.md)
- [class func scrollablePlainDocumentContentTextView() -> NSScrollView](./scrollableplaindocumentcontenttextview%28%29.md)
- [class func scrollableTextView() -> NSScrollView](./scrollabletextview%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/drawbackground(in:))*