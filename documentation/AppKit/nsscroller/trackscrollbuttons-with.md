# trackScrollButtons(with:)

**Framework**: AppKit  
**Kind**: method

Tracks the scroll buttons and sends action messages to the receiver’s target.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func trackScrollButtons(with event: NSEvent)
```

#### Discussion

This method is invoked automatically when the receiver receives `theEvent` mouse-down event in a scroll button; you should not invoke this method directly.

##### Special Considerations

This method is not invoked in macOS 10.7 and later.

## See Also

- [func drawArrow(NSScroller.Arrow, highlight: Bool)](nsscroller/drawarrow(_:highlight:).md)
  Draws the scroll button indicated by `arrow`, which is either `NSScrollerIncrementArrow` (the down or right scroll button) or `NSScrollerDecrementArrow` (up or left).
- [func highlight(Bool)](nsscroller/highlight(_:).md)
  Highlights or unhighlights the scroll button the user clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/trackscrollbuttons(with:))*