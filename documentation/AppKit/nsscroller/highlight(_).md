# highlight(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Highlights or unhighlights the scroll button the user clicked.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Has had no effect since 10.7

## Declaration

```swift
func highlight(_ flag: Bool)
```

```objc
- (void) highlight:(BOOL) flag;
```

#### Discussion

The receiver invokes this method while tracking the mouse; you should not invoke it directly. If `flag` is [`true`](../../Swift/true.md), the appropriate part is drawn highlighted; otherwise it’s drawn normally.

##### Special Considerations

This method has no effect in macOS 10.7 and later.

## See Also

### Related Documentation
- [func rect(for: NSScroller.Part) -> NSRect](./rect%28for%29.md)
  Returns the rectangle occupied by `aPart`, which for this method is interpreted literally rather than as an indicator of scrolling direction.
### Deprecated methods
- [func drawArrow(NSScroller.Arrow, highlight: Bool)](./drawarrow%28_,highlight%29.md)
  Draws the scroll button indicated by `arrow`, which is either `NSScrollerIncrementArrow` (the down or right scroll button) or `NSScrollerDecrementArrow` (up or left).
- [func trackScrollButtons(with: NSEvent)](./trackscrollbuttons%28with%29.md)
  Tracks the scroll buttons and sends action messages to the receiver’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/highlight(_:))*