# rect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The rectangle bounds of the region.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
var rect: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect rect;
```

## Discussion

This rectangle must be in the [`UIPointerInteraction`](../uipointerinteraction.md) view’s coordinate space.

## See Also

### Configuring a region
- [var identifier: AnyHashable?](./identifier-1tw1m.md)
  An optional identifier for the region.
- [var latchingAxes: UIAxis](./latchingaxes.md)
  Axes along which the region latches after a primary click.
- [identifier](./identifier-9i5wc.md)
  An optional identifier for the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerregion/rect)*