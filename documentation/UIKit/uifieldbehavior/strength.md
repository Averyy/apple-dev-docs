# strength

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The strength of the field.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var strength: CGFloat { get set }
```

```objc
@property (nonatomic, assign) CGFloat strength;
```

## Discussion

The default value of this property is `1.0`. The effect of this value is dependent on the type of field. In practice, the best approach for determining the strength of the field you want is to experiment with different values until you get the behavior you want.

## See Also

### Configuring the field attributes
- [var position: CGPoint](./position.md)
  The position of the field in the reference coordinate system.
- [var region: UIRegion](./region.md)
  The shape of the field.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/strength)*