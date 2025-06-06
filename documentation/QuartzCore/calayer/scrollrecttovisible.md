# scrollRectToVisible(_:)

**Framework**: Core Animation  
**Kind**: method

Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified rectangle becomes visible.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func scrollRectToVisible(_ r: CGRect)
```

#### Discussion

If the layer is not contained by a [`CAScrollLayer`](cascrolllayer.md) object, this method does nothing.

## Parameters

- `r`: The rectangle to be made visible.

## See Also

- [var visibleRect: CGRect](calayer/visiblerect.md)
  The visible region of the layer in its own coordinate space.
- [func scroll(CGPoint)](calayer/scroll(_:).md)
  Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified point lies at the origin of the scroll layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/scrollrecttovisible(_:))*