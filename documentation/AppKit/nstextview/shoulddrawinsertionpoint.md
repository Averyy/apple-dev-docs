# shouldDrawInsertionPoint

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the receiver should draw its insertion point.

**Availability**:
- macOS

## Declaration

```swift
var shouldDrawInsertionPoint: Bool { get }
```

```objc
@property (readonly) BOOL shouldDrawInsertionPoint;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver should draw its insertion point, [`false`](../../Swift/false.md) otherwise.

## See Also

### Controlling text display
- [func setNeedsDisplay(NSRect, avoidAdditionalLayout: Bool)](./setneedsdisplay%28_,avoidadditionallayout%29.md)
  Marks the receiver as requiring display.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/shoulddrawinsertionpoint)*