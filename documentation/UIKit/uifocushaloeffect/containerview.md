# containerView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The container view to place the halo effect into.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
weak var containerView: UIView? { get set }
```

```objc
@property (nonatomic, weak, nullable) UIView * containerView;
```

## Discussion

If you don’t set this property, the system automatically determines the container according to the focus item that provides the effect and [`referenceView`](./referenceview.md), if present.

## See Also

### Configuring a halo effect
- [var referenceView: UIView?](./referenceview.md)
  The view to place the halo effect above.
- [var position: UIFocusHaloEffect.Position](./position-swift.property.md)
  The position of the halo effect relative to its shape.
- [UIFocusHaloEffect.Position](./position-swift.enum.md)
  Constants that describe positions for drawing the halo focus effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocushaloeffect/containerview)*