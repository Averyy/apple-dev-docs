# linearGravityField(direction:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a field behavior object that models a linear gravitational force.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func linearGravityField(direction: CGVector) -> Self
```

```objc
+ (instancetype) linearGravityFieldWithVector:(CGVector) direction;
```

#### Return Value

A field behavior object that applies a directional gravitation force to items with mass.

#### Discussion

This field creates a directional gravitational force that applies uniformly to all dynamic items with mass. When setting the [`strength`](./strength.md) of the field, positive values attract items in the direction of the vector and negative values repel items. The force on a given item can be determined by the equation `F = ma`, where force equals the mass of the item multiplied by the acceleration imposed by the gravitational field, which with this type of field is constant.

## Parameters

- `direction`: The vector indicating the direction of the gravitational force. You can change this value later by modifying the [`direction`](./direction.md) property.

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
- [class func magneticField() -> Self](./magneticfield%28%29.md)
  Creates and returns a field behavior that interacts with charged items.
- [class func radialGravityField(position: CGPoint) -> Self](./radialgravityfield%28position%29.md)
  Creates and returns a field behavior object that models a radial gravitational force.
- [class func vortexField() -> Self](./vortexfield%28%29.md)
  Creates and returns a field behavior object that applies a rotational force relative to the field’s position.
- [class func noiseField(smoothness: CGFloat, animationSpeed: CGFloat) -> Self](./noisefield%28smoothness,animationspeed%29.md)
  Creates and returns a field behavior object that applies random noise to other forces.
- [class func turbulenceField(smoothness: CGFloat, animationSpeed: CGFloat) -> Self](./turbulencefield%28smoothness,animationspeed%29.md)
  Creates and returns a field behavior object that applies noise to an item in motion.
- [class func field(evaluationBlock: (UIFieldBehavior, CGPoint, CGVector, CGFloat, CGFloat, TimeInterval) -> CGVector) -> Self](./field%28evaluationblock%29.md)
  Creates and returns a field behavior object that applies an app-specified field to items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/lineargravityfield(direction:))*