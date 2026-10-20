# setConstrainedFrameSize(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attempts to set the frame size as if by user action.

**Availability**:
- macOS

## Declaration

```swift
func setConstrainedFrameSize(_ desiredSize: NSSize)
```

```objc
- (void) setConstrainedFrameSize:(NSSize) desiredSize;
```

#### Discussion

This method respects the receiver’s existing minimum and maximum sizes and by whether resizing is permitted.

## Parameters

- `desiredSize`: The new desired size.

## See Also

### Related Documentation
- [var minSize: NSSize](../nstext/minsize.md)
  The receiver’s minimum size.
- [var isVerticallyResizable: Bool](../nstext/isverticallyresizable.md)
  A Boolean that controls whether the receiver changes its height to fit the height of its text.
- [var isHorizontallyResizable: Bool](../nstext/ishorizontallyresizable.md)
  A Boolean that controls whether the receiver changes its width to fit the width of its text.
- [var maxSize: NSSize](../nstext/maxsize.md)
  The receiver’s maximum size.
### Controlling text display
- [func setNeedsDisplay(NSRect, avoidAdditionalLayout: Bool)](./setneedsdisplay%28_,avoidadditionallayout%29.md)
  Marks the receiver as requiring display.
- [var shouldDrawInsertionPoint: Bool](./shoulddrawinsertionpoint.md)
  A Boolean value that determines whether the receiver should draw its insertion point.
- [func drawInsertionPoint(in: NSRect, color: NSColor, turnedOn: Bool)](./drawinsertionpoint%28in,color,turnedon%29.md)
  Draws or erases the insertion point.
- [func drawBackground(in: NSRect)](./drawbackground%28in%29.md)
  Draws the background of the text view.
- [func cleanUpAfterDragOperation()](./cleanupafterdragoperation%28%29.md)
  Releases the drag information still existing after the dragging session has completed.
- [func showFindIndicator(for: NSRange)](./showfindindicator%28for%29.md)
  Causes a temporary highlighting effect to appear around the visible portion (or portions) of the specified range.
- [class func scrollableDocumentContentTextView() -> NSScrollView](./scrollabledocumentcontenttextview%28%29.md)
- [class func scrollablePlainDocumentContentTextView() -> NSScrollView](./scrollableplaindocumentcontenttextview%28%29.md)
- [class func scrollableTextView() -> NSScrollView](./scrollabletextview%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/setconstrainedframesize(_:))*