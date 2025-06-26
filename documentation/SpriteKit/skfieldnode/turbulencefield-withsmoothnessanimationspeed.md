# turbulenceField(withSmoothness:animationSpeed:)

**Framework**: SpriteKit  
**Kind**: method

Creates a field node that applies a randomized acceleration to physics bodies.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func turbulenceField(withSmoothness smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode
```

#### Return Value

A new turbulence field node.

#### Discussion

The acceleration’s magnitude is proportional to a body’s velocity.

## Parameters

- `smoothness`: The smoothness of the noise used to generate the forces. This parameter should be a value between   and  , where   represents a uniform smoothness.
- `speed`: The speed at which the noise field should change. A value of   means that the field should not animate at all.

## See Also

- [class func dragField() -> SKFieldNode](skfieldnode/dragfield.md)
  Creates a field node that applies a force that resists the motion of physics bodies.
- [class func electricField() -> SKFieldNode](skfieldnode/electricfield.md)
  Creates a field node that applies an electrical force proportional to the electrical charge of physics bodies.
- [class func linearGravityField(withVector: vector_float3) -> SKFieldNode](skfieldnode/lineargravityfield(withvector:).md)
  Creates a field node that accelerates physics bodies in a specific direction.
- [class func magneticField() -> SKFieldNode](skfieldnode/magneticfield.md)
  Creates a field node that applies a magnetic force based on the velocity and electrical charge of the physics bodies.
- [class func noiseField(withSmoothness: CGFloat, animationSpeed: CGFloat) -> SKFieldNode](skfieldnode/noisefield(withsmoothness:animationspeed:).md)
  Creates a field node that applies a randomized acceleration to physics bodies.
- [class func radialGravityField() -> SKFieldNode](skfieldnode/radialgravityfield.md)
  Creates a field node that accelerates physics bodies toward the field node.
- [class func springField() -> SKFieldNode](skfieldnode/springfield.md)
  Creates a field node that applies a spring-like force that pulls physics bodies toward the field node.
- [class func velocityField(with: SKTexture) -> SKFieldNode](skfieldnode/velocityfield(with:).md)
  Creates a field node that sets the velocity of physics bodies that enter the node’s area based on the pixel values of a texture.
- [class func velocityField(withVector: vector_float3) -> SKFieldNode](skfieldnode/velocityfield(withvector:).md)
  Creates a field node that gives physics bodies a constant velocity.
- [class func vortexField() -> SKFieldNode](skfieldnode/vortexfield.md)
  Creates a field node that applies a perpendicular force to physics bodies.
- [class func customField(evaluationBlock: SKFieldForceEvaluator) -> SKFieldNode](skfieldnode/customfield(evaluationblock:).md)
  Creates a field node that calculates and applies a custom force to the physics body.
- [typealias SKFieldForceEvaluator](skfieldforceevaluator.md)
  The definition for a custom block that processes a single physics body’s interaction with the field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skfieldnode/turbulencefield(withsmoothness:animationspeed:))*