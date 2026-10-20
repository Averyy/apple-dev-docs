# showFindIndicator(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Causes a temporary highlighting effect to appear around the visible portion (or portions) of the specified range.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func showFindIndicator(for charRange: NSRange)
```

```objc
- (void) showFindIndicatorForRange:(NSRange) charRange;
```

#### Discussion

This method supports lozenge-style indication of find results. The indicators automatically disappear after a certain period of time, or when the method is called again, or when any of a number of changes occur to the view (such as changes to text, view size, or view position).

This method does not itself scroll the specified range to be visible; any desired scrolling should be done before this method is called, first, because the method acts only on the visible portion of the specified range, and, second, because scrolling causes the indicators to disappear. Calling this method with a zero-length range always removes any existing indicators.

## Parameters

- `charRange`: The character range around which indicators appear.

## See Also

### Controlling text display
- [func setNeedsDisplay(NSRect, avoidAdditionalLayout: Bool)](./setneedsdisplay%28_,avoidadditionallayout%29.md)
  Marks the receiver as requiring display.
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
- [class func scrollableDocumentContentTextView() -> NSScrollView](./scrollabledocumentcontenttextview%28%29.md)
- [class func scrollablePlainDocumentContentTextView() -> NSScrollView](./scrollableplaindocumentcontenttextview%28%29.md)
- [class func scrollableTextView() -> NSScrollView](./scrollabletextview%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/showfindindicator(for:))*