# falloff

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The rate of decay for the field strength.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var falloff: CGFloat { get set }
```

```objc
@property (nonatomic, assign) CGFloat falloff;
```

#### Discussion

This property defines how quickly the field strength diminishes as the distance from the field’s center increases. Falloff is not applied until the distance between objects is greater than the value in the [`minimumRadius`](./minimumradius.md) property.

The default value of the property is 0, which yields a uniform field that does not diminish over distance.

## See Also

### Configuring the field attributes
- [var position: CGPoint](./position.md)
  The position of the field in the reference coordinate system.
- [var region: UIRegion](./region.md)
  The shape of the field.
- [var strength: CGFloat](./strength.md)
  The strength of the field.
- [var minimumRadius: CGFloat](./minimumradius.md)
  The minimum distance at which to start calculating new values for the field.
- [var direction: CGVector](./direction.md)
  The direction of motion for a linear field.
- [var smoothness: CGFloat](./smoothness.md)
  The smoothness of the noise used to generate the field.
- [var animationSpeed: CGFloat](./animationspeed.md)
  The rate at which the animation should proceed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/falloff)*