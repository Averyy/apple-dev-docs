# field(evaluationBlock:)

**Framework**: UIKit  
**Kind**: method

Creates and returns a field behavior object that applies an app-specified field to items.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func field(evaluationBlock block: @escaping (UIFieldBehavior, CGPoint, CGVector, CGFloat, CGFloat, TimeInterval) -> CGVector) -> Self
```

#### Return Value

A field behavior object that applies forces based on the custom algorithm you provided.

#### Discussion

Use this method to define a custom field for your app. The block you provide is called many times during the course of animations, so your implementation should be reasonably fast. Use the provided `field` object to retrieve values associated with the field itself, such as the field’s position and strength. The other parameters reflect information about the dynamic item affected by the field.

## Parameters

- `block`: The block to execute to compute the instantaneous force of the field on an item. This block returns a CGVector object that reflects the direction and magnitude of the force to apply. The block takes the following parameters: - **field**: The field behavior object being evaluated.
- **position**: The point at which to compute the force value, in the reference coordinate system. The position corresponds to the location of an item in the field.
- **velocity**: The velocity to be considered during evaluation of the force. Usually, this is the velocity of an item in the field. The vector reflects both the direction and magnitude of the velocity.
- **mass**: The mass value to be used in any force computations. Use this value in fields where the applied forces vary with the mass of the object.
- **charge**: The charge value to be used in any force computations. Use this value in fields where the applied forces vary with the charge of the object.
- **deltaTime**: The amount of time that has passed since the last time the force value for this item was computed.

## See Also

- [class func dragField() -> Self](uifieldbehavior/dragfield.md)
  Creates and returns a field behavior for slowing an object’s velocity.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/field(evaluationblock:))*