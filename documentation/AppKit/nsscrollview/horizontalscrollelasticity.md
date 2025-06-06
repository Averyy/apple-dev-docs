# horizontalScrollElasticity

**Framework**: AppKit  
**Kind**: property

The scroll view’s horizontal scrolling elasticity mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var horizontalScrollElasticity: NSScrollView.Elasticity { get set }
```

#### Discussion

A scroll view can scroll its contents past its bounds to achieve an elastic effect.

When set to [`NSScrollView.Elasticity.automatic`](nsscrollview/elasticity/automatic.md), scrolling the horizontal axis beyond its document bounds only occurs if the document width is greater than the view width, or the vertical scroller is hidden and the horizontal scroller is visible. The default value is [`NSScrollView.Elasticity.automatic`](nsscrollview/elasticity/automatic.md).

See [`NSScrollView.Elasticity`](nsscrollview/elasticity.md) for possible values.

## See Also

- [var verticalScrollElasticity: NSScrollView.Elasticity](nsscrollview/verticalscrollelasticity.md)
  The scroll view’s vertical scrolling elasticity mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/horizontalscrollelasticity)*