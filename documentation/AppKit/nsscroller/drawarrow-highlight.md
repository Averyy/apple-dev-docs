# drawArrow(_:highlight:)

**Framework**: AppKit  
**Kind**: method

Draws the scroll button indicated by `arrow`, which is either `NSScrollerIncrementArrow` (the down or right scroll button) or `NSScrollerDecrementArrow` (up or left).

**Availability**:
- macOS 10.0+

## Declaration

```swift
func drawArrow(_ whichArrow: NSScroller.Arrow, highlight flag: Bool)
```

#### Discussion

If `flag` is [`true`](https://developer.apple.com/documentation/swift/true), the button is drawn highlighted; otherwise it’s drawn normally. You should never need to invoke this method directly, but may wish to override it to customize the appearance of scroll buttons.

> **Note**:  The [`drawArrow(_:highlight:)`](nsscroller/drawarrow(_:highlight:).md) method is not invoked in macOS 10.7 and later.

## See Also

- [func rect(for: NSScroller.Part) -> NSRect](nsscroller/rect(for:).md)
  Returns the rectangle occupied by `aPart`, which for this method is interpreted literally rather than as an indicator of scrolling direction.
- [func highlight(Bool)](nsscroller/highlight(_:).md)
  Highlights or unhighlights the scroll button the user clicked.
- [func trackScrollButtons(with: NSEvent)](nsscroller/trackscrollbuttons(with:).md)
  Tracks the scroll buttons and sends action messages to the receiver’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/drawarrow(_:highlight:))*