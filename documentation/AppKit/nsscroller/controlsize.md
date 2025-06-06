# controlSize

**Framework**: AppKit  
**Kind**: property

The size of the scroller.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var controlSize: NSControl.ControlSize { get set }
```

#### Discussion

Valid values for `controlSize` are described in [`NSControl.ControlSize`](nscontrol/controlsize-swift.enum.md) (`NSCell`).

## See Also

- [class func scrollerWidth(for: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> CGFloat](nsscroller/scrollerwidth(for:scrollerstyle:).md)
  Returns the width for scrollers of the receiving class for a given control size and scroller style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/controlsize)*