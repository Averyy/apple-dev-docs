# controlSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The size of the scroller.

**Availability**:
- macOS

## Declaration

```swift
var controlSize: NSControl.ControlSize { get set }
```

```objc
@property NSControlSize controlSize;
```

#### Discussion

Valid values for `controlSize` are described in [`NSControl.ControlSize`](../nscontrol/controlsize-swift.enum.md) (`NSCell`).

## See Also

### Determining Scroller Size
- [class func scrollerWidth(for: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> CGFloat](./scrollerwidth%28for,scrollerstyle%29.md)
  Returns the width for scrollers of the receiving class for a given control size and scroller style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/controlsize)*