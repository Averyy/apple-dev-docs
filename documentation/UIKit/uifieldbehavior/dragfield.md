# dragField()

**Framework**: UIKit  
**Kind**: method

Creates and returns a field behavior for slowing an object’s velocity.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func dragField() -> Self
```

#### Return Value

A field behavior object that applies a drag force to items.

#### Discussion

This field simulates the force of friction on an item. The force is applied in the opposite direction of the affected item’s velocity vector and has a magnitude that is proportional to the field’s [`strength`](uifieldbehavior/strength.md) property and the item’s current velocity.

## See Also

- [class func springField() -> Self](uifieldbehavior/springfield.md)
  Creates and returns a spring field behavior.
- [class func velocityField(direction: CGVector) -> Self](uifieldbehavior/velocityfield(direction:).md)
  Creates and returns a field behavior object that applies a directional velocity to items.
- [class func electricField() -> Self](uifieldbehavior/electricfield.md)
  Creates and returns a field behavior object that interacts with charged items.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/dragfield())*