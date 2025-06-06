# electricField()

**Framework**: UIKit  
**Kind**: method

Creates and returns a field behavior object that interacts with charged items.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func electricField() -> Self
```

#### Return Value

An field behavior object that applies an electric field to charged items.

#### Discussion

The amount of force applied by the field is proportional to the charge of the item and is modeled after the first part of the Lorentz equation (`F = qE`). This equation means that the force equals the charge of the object multiplied by the strength of the electric field at the item’s current location in that field.

You can use electric fields as a way to apply forces to an object that are based on charge instead of mass. You can use electric fields to repel or attract items in your interface, with opposite charges attracting each other and similar charges repelling each other. In other words, an item with a positive charge value is attracted to fields whose [`strength`](uifieldbehavior/strength.md) value is negative and repelled by fields whose [`strength`](uifieldbehavior/strength.md) value is positive.

## See Also

- [class func dragField() -> Self](uifieldbehavior/dragfield.md)
  Creates and returns a field behavior for slowing an object’s velocity.
- [class func springField() -> Self](uifieldbehavior/springfield.md)
  Creates and returns a spring field behavior.
- [class func velocityField(direction: CGVector) -> Self](uifieldbehavior/velocityfield(direction:).md)
  Creates and returns a field behavior object that applies a directional velocity to items.
- [class func magneticField() -> Self](uifieldbehavior/magneticfield.md)
  Creates and returns a field behavior that interacts with charged items.
- [class func radialGravityField(position: CGPoint) -> Self](uifieldbehavior/radialgravityfield(position:).md)
  Creates and returns a field behavior object that models a radial gravitational force.
- [class func linearGravityField(direction: CGVector) -> Self](uifieldbehavior/lineargravityfield(direction:).md)
  Creates and returns a field behavior object that models a linear gravitational force.
- [class func vortexField() -> Self](uifieldbehavior/vortexfield.md)
  Creates and returns a field behavior object that applies a rotational force relative to the field’s position.
- [class func noiseField(smoothness: CGFloat, animationSpeed: CGFloat) -> Self](uifieldbehavior/noisefield(smoothness:animationspeed:).md)
  Creates and returns a field behavior object that applies random noise to other forces.
- [class func turbulenceField(smoothness: CGFloat, animationSpeed: CGFloat) -> Self](uifieldbehavior/turbulencefield(smoothness:animationspeed:).md)
  Creates and returns a field behavior object that applies noise to an item in motion.
- [class func field(evaluationBlock: (UIFieldBehavior, CGPoint, CGVector, CGFloat, CGFloat, TimeInterval) -> CGVector) -> Self](uifieldbehavior/field(evaluationblock:).md)
  Creates and returns a field behavior object that applies an app-specified field to items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/electricfield())*