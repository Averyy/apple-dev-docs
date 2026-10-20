# scroll(_:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified point lies at the origin of the scroll layer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func scroll(_ p: CGPoint)
```

```objc
- (void) scrollPoint:(CGPoint) p;
```

#### Discussion

If the layer is not contained by a [`CAScrollLayer`](../cascrolllayer.md) object, this method does nothing.

## Parameters

- `p`: The point in the current layer that should be scrolled into position.

## See Also

### Scrolling
- [var visibleRect: CGRect](./visiblerect.md)
  The visible region of the layer in its own coordinate space.
- [func scrollRectToVisible(CGRect)](./scrollrecttovisible%28_%29.md)
  Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified rectangle becomes visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/scroll(_:))*