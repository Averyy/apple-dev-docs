# rect

**Framework**: UIKit  
**Kind**: property

The rectangle bounds of the region.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var rect: CGRect { get }
```

#### Discussion

This rectangle must be in the [`UIPointerInteraction`](uipointerinteraction.md) view’s coordinate space.

## See Also

- [var identifier: AnyHashable?](uipointerregion/identifier-1tw1m.md)
  An optional identifier for the region.
- [var latchingAxes: UIAxis](uipointerregion/latchingaxes.md)
  Axes along which the region latches after a primary click.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerregion/rect)*