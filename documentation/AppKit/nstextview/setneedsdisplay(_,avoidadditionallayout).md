# setNeedsDisplay(_:avoidAdditionalLayout:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Marks the receiver as requiring display.

**Availability**:
- macOS

## Declaration

```swift
func setNeedsDisplay(_ rect: NSRect, avoidAdditionalLayout flag: Bool)
```

```objc
- (void) setNeedsDisplayInRect:(NSRect) rect avoidAdditionalLayout:(BOOL) flag;
```

## Discussion

`NSTextView` overrides the `NSView` [`setNeedsDisplay(_:)`](../nsview/setneedsdisplay%28_%29.md) method to invoke this method with a `flag` argument of [`false`](../../Swift/false.md).

## Parameters

- `rect`: The rectangle in which display is required.
- `flag`: A value of [`true`](../../Swift/true.md) causes the receiver to not perform any layout, even if this means that portions of the text view remain empty. Otherwise the receiver performs at least as much layout as needed to display `aRect`.

## See Also

### Controlling text display
- [var shouldDrawInsertionPoint: Bool](./shoulddrawinsertionpoint.md)
  A Boolean value that determines whether the receiver should draw its insertion point.
- [func drawInsertionPoint(in: NSRect, color: NSColor, turnedOn: Bool)](./drawinsertionpoint%28in,color,turnedon%29.md)
  Draws or erases the insertion point.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/setneedsdisplay(_:avoidadditionallayout:))*