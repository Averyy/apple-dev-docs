# linearGravityField(withVector:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates a field node that accelerates physics bodies in a specific direction.

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
class func linearGravityField(withVector direction: vector_float3) -> SKFieldNode
```

```objc
+ (SKFieldNode *) linearGravityFieldWithVector:(vector_float3) direction;
```

#### Return Value

A new linear gravity field node.

#### Discussion

If the field node is rotated, the direction of its gravity field is also rotated. The calculated force is proportional to the physics body’s mass (meaning that the acceleration applied to all affected physics bodies is a constant).

## Parameters

- `direction`: The direction and magnitude of the gravitational force. The values represent the acceleration of the field in meters per second squared. For example, to simulate earth’s gravity, specify `(0, -9.8, 0)`. The `z` component on the vector is ignored.

## See Also

### Creating Field Nodes
- [class func dragField() -> SKFieldNode](./dragfield%28%29.md)
  Creates a field node that applies a force that resists the motion of physics bodies.
- [class func electricField() -> SKFieldNode](./electricfield%28%29.md)
  Creates a field node that applies an electrical force proportional to the electrical charge of physics bodies.
- [class func magneticField() -> SKFieldNode](./magneticfield%28%29.md)
  Creates a field node that applies a magnetic force based on the velocity and electrical charge of the physics bodies.
- [class func noiseField(withSmoothness: CGFloat, animationSpeed: CGFloat) -> SKFieldNode](./noisefield%28withsmoothness,animationspeed%29.md)
  Creates a field node that applies a randomized acceleration to physics bodies.
- [class func radialGravityField() -> SKFieldNode](./radialgravityfield%28%29.md)
  Creates a field node that accelerates physics bodies toward the field node.
- [class func springField() -> SKFieldNode](./springfield%28%29.md)
  Creates a field node that applies a spring-like force that pulls physics bodies toward the field node.
- [class func turbulenceField(withSmoothness: CGFloat, animationSpeed: CGFloat) -> SKFieldNode](./turbulencefield%28withsmoothness,animationspeed%29.md)
  Creates a field node that applies a randomized acceleration to physics bodies.
- [class func velocityField(with: SKTexture) -> SKFieldNode](./velocityfield%28with%29.md)
  Creates a field node that sets the velocity of physics bodies that enter the node’s area based on the pixel values of a texture.
- [class func velocityField(withVector: vector_float3) -> SKFieldNode](./velocityfield%28withvector%29.md)
  Creates a field node that gives physics bodies a constant velocity.
- [class func vortexField() -> SKFieldNode](./vortexfield%28%29.md)
  Creates a field node that applies a perpendicular force to physics bodies.
- [class func customField(evaluationBlock: SKFieldForceEvaluator) -> SKFieldNode](./customfield%28evaluationblock%29.md)
  Creates a field node that calculates and applies a custom force to the physics body.
- [typealias SKFieldForceEvaluator](../skfieldforceevaluator.md)
  The definition for a custom block that processes a single physics body’s interaction with the field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skfieldnode/lineargravityfield(withvector:))*