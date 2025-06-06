# containerView

**Framework**: UIKit  
**Kind**: property

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

#### Discussion

If you don’t set this property, the system automatically determines the container according to the focus item that provides the effect and [`referenceView`](uifocushaloeffect/referenceview.md), if present.

## See Also

- [var referenceView: UIView?](uifocushaloeffect/referenceview.md)
  The view to place the halo effect above.
- [var position: UIFocusHaloEffect.Position](uifocushaloeffect/position-swift.property.md)
  The position of the halo effect relative to its shape.
- [UIFocusHaloEffect.Position](uifocushaloeffect/position-swift.enum.md)
  Constants that describe positions for drawing the halo focus effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocushaloeffect/containerview)*