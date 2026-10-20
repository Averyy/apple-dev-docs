# region

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The shape of the field.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var region: UIRegion { get set }
```

```objc
@property (nonatomic, strong) UIRegion * region;
```

#### Discussion

This property defines the shape of the field centered on the point in the [`position`](./position.md) property. A field does not exert any force on items that lie outside of the specified region.

## See Also

### Configuring the field attributes
- [var position: CGPoint](./position.md)
  The position of the field in the reference coordinate system.
- [var strength: CGFloat](./strength.md)
  The strength of the field.
- [var falloff: CGFloat](./falloff.md)
  The rate of decay for the field strength.
- [var minimumRadius: CGFloat](./minimumradius.md)
  The minimum distance at which to start calculating new values for the field.
- [var direction: CGVector](./direction.md)
  The direction of motion for a linear field.
- [var smoothness: CGFloat](./smoothness.md)
  The smoothness of the noise used to generate the field.
- [var animationSpeed: CGFloat](./animationspeed.md)
  The rate at which the animation should proceed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/region)*