# scrollerWidth(for:scrollerStyle:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the width for scrollers of the receiving class for a given control size and scroller style.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class func scrollerWidth(for controlSize: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> CGFloat
```

```objc
+ (CGFloat) scrollerWidthForControlSize:(NSControlSize) controlSize scrollerStyle:(NSScrollerStyle) scrollerStyle;
```

#### Return Value

The width for scrollers of the receiving class for `controlSize` and `scrollerStyle`.

#### Discussion

You should use this method in preference to [`scrollerWidthForControlSize:`](./scrollerwidthforcontrolsize_.md), which assumes a scroller style of [`NSScroller.Style.legacy`](./style/legacy.md), and [`scrollerWidth`](./scrollerwidth.md) which in addition assumes a control size of [`NSRegularControlSize`](../nsregularcontrolsize.md).

## Parameters

- `controlSize`: A control size.
- `scrollerStyle`: A scroller style.

## See Also

### Determining Scroller Size
- [var controlSize: NSControl.ControlSize](./controlsize.md)
  The size of the scroller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/scrollerwidth(for:scrollerstyle:))*