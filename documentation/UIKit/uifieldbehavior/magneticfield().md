# magneticField()

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a field behavior that interacts with charged items.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func magneticField() -> Self
```

```objc
+ (instancetype) magneticField;
```

## Return Value

A field behavior object that applies a magnetic field to charged items.

## Discussion

The magnetic field behavior models a uniform magnetic field in the positive-z direction—that is, coming out of the screen. The amount of force applied by the field is modeled after the second part of the Lorentz equation (`F = qvB`). When the velocity of a charged item is perpendicular to the uniform magnetic field, the item feels a force normal to both the velocity and the field, resulting in a counter-clockwise rotation. Specifying a negative value for the [`strength`](./strength.md) of the field results in a clockwise rotation.

You can use magnetic fields as a way to apply forces to an object that are based on charge instead of mass.

## See Also

### Getting the field behaviors
- [class func dragField() -> Self](./dragfield%28%29.md)
  Creates and returns a field behavior for slowing an object’s velocity.
- [class func springField() -> Self](./springfield%28%29.md)
  Creates and returns a spring field behavior.
- [class func velocityField(direction: CGVector) -> Self](./velocityfield%28direction%29.md)
  Creates and returns a field behavior object that applies a directional velocity to items.
- [class func electricField() -> Self](./electricfield%28%29.md)
  Creates and returns a field behavior object that interacts with charged items.
- [class func radialGravityField(position: CGPoint) -> Self](./radialgravityfield%28position%29.md)
  Creates and returns a field behavior object that models a radial gravitational force.
- [class func linearGravityField(direction: CGVector) -> Self](./lineargravityfield%28direction%29.md)
  Creates and returns a field behavior object that models a linear gravitational force.
- [class func vortexField() -> Self](./vortexfield%28%29.md)
  Creates and returns a field behavior object that applies a rotational force relative to the field’s position.
- [class func noiseField(smoothness: CGFloat, animationSpeed: CGFloat) -> Self](./noisefield%28smoothness,animationspeed%29.md)
  Creates and returns a field behavior object that applies random noise to other forces.
- [class func turbulenceField(smoothness: CGFloat, animationSpeed: CGFloat) -> Self](./turbulencefield%28smoothness,animationspeed%29.md)
  Creates and returns a field behavior object that applies noise to an item in motion.
- [class func field(evaluationBlock: (UIFieldBehavior, CGPoint, CGVector, CGFloat, CGFloat, TimeInterval) -> CGVector) -> Self](./field%28evaluationblock%29.md)
  Creates and returns a field behavior object that applies an app-specified field to items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/magneticfield())*