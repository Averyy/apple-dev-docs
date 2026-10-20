# referenceView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view to place the halo effect above.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
weak var referenceView: UIView? { get set }
```

```objc
@property (nonatomic, weak, nullable) UIView * referenceView;
```

#### Discussion

If you set this property, the halo effect appears above this view. If you also set [`containerView`](./containerview.md), this reference view must be a descendant of the container view. The system ensures that the halo effect is in the container but visually above the reference view.

## See Also

### Configuring a halo effect
- [var containerView: UIView?](./containerview.md)
  The container view to place the halo effect into.
- [var position: UIFocusHaloEffect.Position](./position-swift.property.md)
  The position of the halo effect relative to its shape.
- [UIFocusHaloEffect.Position](./position-swift.enum.md)
  Constants that describe positions for drawing the halo focus effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocushaloeffect/referenceview)*