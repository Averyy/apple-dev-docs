# minimumRadius

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The minimum distance at which to start calculating new values for the field.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var minimumRadius: CGFloat { get set }
```

```objc
@property (nonatomic, assign) CGFloat minimumRadius;
```

## Discussion

Use this property to modify the behavior of distance-based effects when objects are close to the center of the field. Distances that are less than the minimum value are treated as if they are equal to the minimum value. In addition, effects such as [`falloff`](./falloff.md) are not applied until the minimum distance is reached.

The default value of this property is very small, but not zero.

## See Also

### Configuring the field attributes
- [var position: CGPoint](./position.md)
  The position of the field in the reference coordinate system.
- [var region: UIRegion](./region.md)
  The shape of the field.
- [var strength: CGFloat](./strength.md)
  The strength of the field.
- [var falloff: CGFloat](./falloff.md)
  The rate of decay for the field strength.
- [var direction: CGVector](./direction.md)
  The direction of motion for a linear field.
- [var smoothness: CGFloat](./smoothness.md)
  The smoothness of the noise used to generate the field.
- [var animationSpeed: CGFloat](./animationspeed.md)
  The rate at which the animation should proceed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/minimumradius)*