# horizontalScrollElasticity

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The scroll view’s horizontal scrolling elasticity mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var horizontalScrollElasticity: NSScrollView.Elasticity { get set }
```

```objc
@property NSScrollElasticity horizontalScrollElasticity;
```

#### Discussion

A scroll view can scroll its contents past its bounds to achieve an elastic effect.

When set to [`NSScrollView.Elasticity.automatic`](./elasticity/automatic.md), scrolling the horizontal axis beyond its document bounds only occurs if the document width is greater than the view width, or the vertical scroller is hidden and the horizontal scroller is visible. The default value is [`NSScrollView.Elasticity.automatic`](./elasticity/automatic.md).

See [`NSScrollView.Elasticity`](./elasticity.md) for possible values.

## See Also

### Specifying the Scroll View Elasticity
- [var verticalScrollElasticity: NSScrollView.Elasticity](./verticalscrollelasticity.md)
  The scroll view’s vertical scrolling elasticity mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/horizontalscrollelasticity)*