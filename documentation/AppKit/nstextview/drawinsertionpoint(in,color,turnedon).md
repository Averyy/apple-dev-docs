# drawInsertionPoint(in:color:turnedOn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws or erases the insertion point.

**Availability**:
- macOS

## Declaration

```swift
func drawInsertionPoint(in rect: NSRect, color: NSColor, turnedOn flag: Bool)
```

```objc
- (void) drawInsertionPointInRect:(NSRect) rect color:(NSColor *) color turnedOn:(BOOL) flag;
```

## Discussion

The focus must be locked on the receiver when this method is invoked. You should not need to invoke this method directly.

## Parameters

- `rect`: The rectangle in which to draw the insertion point.
- `color`: The color with which to draw the insertion point.
- `flag`: [`true`](../../Swift/true.md) to draw the insertion point, [`false`](../../Swift/false.md) to erase it.

## See Also

### Related Documentation
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The receiver’s background color.
- [func lockFocus()](../nsview/lockfocus%28%29.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
- [var insertionPointColor: NSColor!](./insertionpointcolor.md)
  The color of the insertion point.
### Controlling text display
- [func setNeedsDisplay(NSRect, avoidAdditionalLayout: Bool)](./setneedsdisplay%28_,avoidadditionallayout%29.md)
  Marks the receiver as requiring display.
- [var shouldDrawInsertionPoint: Bool](./shoulddrawinsertionpoint.md)
  A Boolean value that determines whether the receiver should draw its insertion point.
- [func drawBackground(in: NSRect)](./drawbackground%28in%29.md)
  Draws the background of the text view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/drawinsertionpoint(in:color:turnedon:))*