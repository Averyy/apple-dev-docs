# vortexField()

**Framework**: SpriteKit  
**Kind**: method

Creates a field node that applies a perpendicular force to physics bodies.

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
@MainActor
class func vortexField() -> SKFieldNode
```

#### Return Value

A new vortex field node.

#### Discussion

The strength of the field measures the acceleration of the field in meters per second squared (meaning that similar to gravity, all physics bodies are affected equally). The physics body is accelerated along the perpendicular of the line between the field node’s position and the position of the physics body. A positive field strength indicates the body is accelerated in a counter-clockwise direction. The [`falloff`](skfieldnode/falloff.md) property of a vortex field node is set by default to `2`.

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
- [class func turbulenceField(withSmoothness: CGFloat, animationSpeed: CGFloat) -> SKFieldNode](skfieldnode/turbulencefield(withsmoothness:animationspeed:).md)
  Creates a field node that applies a randomized acceleration to physics bodies.
- [class func velocityField(with: SKTexture) -> SKFieldNode](skfieldnode/velocityfield(with:).md)
  Creates a field node that sets the velocity of physics bodies that enter the node’s area based on the pixel values of a texture.
- [class func velocityField(withVector: vector_float3) -> SKFieldNode](skfieldnode/velocityfield(withvector:).md)
  Creates a field node that gives physics bodies a constant velocity.
- [class func customField(evaluationBlock: SKFieldForceEvaluator) -> SKFieldNode](skfieldnode/customfield(evaluationblock:).md)
  Creates a field node that calculates and applies a custom force to the physics body.
- [typealias SKFieldForceEvaluator](skfieldforceevaluator.md)
  The definition for a custom block that processes a single physics body’s interaction with the field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skfieldnode/vortexfield())*