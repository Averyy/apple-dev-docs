# trackScrollButtons(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tracks the scroll buttons and sends action messages to the receiver’s target.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Not invoked since 10.7

## Declaration

```swift
func trackScrollButtons(with event: NSEvent)
```

```objc
- (void) trackScrollButtons:(NSEvent *) event;
```

#### Discussion

This method is invoked automatically when the receiver receives `theEvent` mouse-down event in a scroll button; you should not invoke this method directly.

##### Special Considerations

This method is not invoked in macOS 10.7 and later.

## See Also

### Deprecated methods
- [func drawArrow(NSScroller.Arrow, highlight: Bool)](./drawarrow%28_,highlight%29.md)
  Draws the scroll button indicated by `arrow`, which is either `NSScrollerIncrementArrow` (the down or right scroll button) or `NSScrollerDecrementArrow` (up or left).
- [func highlight(Bool)](./highlight%28_%29.md)
  Highlights or unhighlights the scroll button the user clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/trackscrollbuttons(with:))*