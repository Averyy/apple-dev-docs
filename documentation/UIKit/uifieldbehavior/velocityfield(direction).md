# velocityField(direction:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a field behavior object that applies a directional velocity to items.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func velocityField(direction: CGVector) -> Self
```

```objc
+ (instancetype) velocityFieldWithVector:(CGVector) direction;
```

#### Return Value

A field behavior object that applies a velocity to items.

#### Discussion

Velocity fields apply their velocity to the item, overriding any other acceleration forces currently on the item. The vector in the `direction` parameter is combined with the field [`strength`](./strength.md) to determine the velocity of items in the field.

## Parameters

- `direction`: The vector indicating the direction of the velocity force. You can change this value later by modifying the [`direction`](./direction.md) property.

## See Also

### Getting the field behaviors
- [class func dragField() -> Self](./dragfield%28%29.md)
  Creates and returns a field behavior for slowing an object’s velocity.
- [class func springField() -> Self](./springfield%28%29.md)
  Creates and returns a spring field behavior.
- [class func electricField() -> Self](./electricfield%28%29.md)
  Creates and returns a field behavior object that interacts with charged items.
- [class func magneticField() -> Self](./magneticfield%28%29.md)
  Creates and returns a field behavior that interacts with charged items.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/velocityfield(direction:))*