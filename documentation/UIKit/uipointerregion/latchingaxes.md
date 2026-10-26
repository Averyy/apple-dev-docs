# latchingAxes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Axes along which the region latches after a primary click.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
var latchingAxes: UIAxis { get set }
```

```objc
@property (nonatomic) UIAxis latchingAxes;
```

#### Discussion

If you set this property, the [`UIPointerStyle`](../uipointerstyle.md) associated with this region locks in and only allows freeform movement along the axes you specify.

## See Also

### Configuring a region
- [var rect: CGRect](./rect.md)
  The rectangle bounds of the region.
- [var identifier: AnyHashable?](./identifier-1tw1m.md)
  An optional identifier for the region.
- [identifier](./identifier-9i5wc.md)
  An optional identifier for the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerregion/latchingaxes)*