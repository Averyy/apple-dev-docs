# identifier

**Framework**: UIKit  
**Kind**: property

An optional identifier for the region.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var identifier: AnyHashable? { get }
```

#### Discussion

Use this value to identify the [`UIPointerRegion`](uipointerregion.md) in subsequent pointer interaction delegate calls.

## See Also

- [var rect: CGRect](uipointerregion/rect.md)
  The rectangle bounds of the region.
- [var latchingAxes: UIAxis](uipointerregion/latchingaxes.md)
  Axes along which the region latches after a primary click.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerregion/identifier-1tw1m)*