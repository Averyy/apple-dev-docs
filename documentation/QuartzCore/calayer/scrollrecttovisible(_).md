# scrollRectToVisible(_:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified rectangle becomes visible.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func scrollRectToVisible(_ r: CGRect)
```

```objc
- (void) scrollRectToVisible:(CGRect) r;
```

#### Discussion

If the layer is not contained by a [`CAScrollLayer`](../cascrolllayer.md) object, this method does nothing.

## Parameters

- `r`: The rectangle to be made visible.

## See Also

### Scrolling
- [var visibleRect: CGRect](./visiblerect.md)
  The visible region of the layer in its own coordinate space.
- [func scroll(CGPoint)](./scroll%28_%29.md)
  Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified point lies at the origin of the scroll layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/scrollrecttovisible(_:))*