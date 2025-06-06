# verticalScrollElasticity

**Framework**: AppKit  
**Kind**: property

The scroll view’s vertical scrolling elasticity mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var verticalScrollElasticity: NSScrollView.Elasticity { get set }
```

#### Discussion

A scroll view can scroll its contents past its bounds to achieve an elastic effect.

When set to [`NSScrollView.Elasticity.automatic`](nsscrollview/elasticity/automatic.md), scrolling the vertical axis beyond its document bounds only occurs if any of the following are true: the vertical scroller is visible, the content height is greater than view height, or the horizontal scroller hidden. The default value is [`NSScrollView.Elasticity.automatic`](nsscrollview/elasticity/automatic.md).

See [`NSScrollView.Elasticity`](nsscrollview/elasticity.md) for possible values.

## See Also

- [var horizontalScrollElasticity: NSScrollView.Elasticity](nsscrollview/horizontalscrollelasticity.md)
  The scroll view’s horizontal scrolling elasticity mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/verticalscrollelasticity)*