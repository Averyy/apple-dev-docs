# customField(evaluationBlock:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates a field node that calculates and applies a custom force to the physics body.

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
class func customField(evaluationBlock block: @escaping SKFieldForceEvaluator) -> SKFieldNode
```

```objc
+ (SKFieldNode *) customFieldWithEvaluationBlock:(SKFieldForceEvaluator) block;
```

#### Return Value

A new custom field node.

#### Discussion

The value returned by the custom block is a vector for an impulse force which is applied to the physics body being evaluated for that frame. Only the `x` and `y` components of the return value are used by SpriteKit, the `z` component is ignored.

The values passed into the block by the `position` and `velocity` arguments measured in meters: if you need to convert them into points — as used by SpriteKit — multiply the values by 150.

The following code shows how to create a custom field to emulate drag. The block returns the negative of the square root of the velocity of the physics body. This decelerates a physics body passing through the [`SKFieldNode`](../skfieldnode.md) object’s region.

Listing 1. Creating a custom drag field

```swift
let simpleDrag = SKFieldNode.customField {
    (position: vector_float3, velocity: vector_float3, mass: Float, charge: Float, deltaTime: TimeInterval) in
    return vector_float3(-sqrt(abs(velocity.x)) * sign(velocity.x),
                         -sqrt(abs(velocity.y)) * sign(velocity.y),
                         0)
}
```

## Parameters

- `block`: A custom block to be executed when a physics body is affected by the field. Your block should calculate and return the force to be applied to the body.

## See Also

### Creating Field Nodes
- [class func dragField() -> SKFieldNode](./dragfield%28%29.md)
  Creates a field node that applies a force that resists the motion of physics bodies.
- [class func electricField() -> SKFieldNode](./electricfield%28%29.md)
  Creates a field node that applies an electrical force proportional to the electrical charge of physics bodies.
- [class func linearGravityField(withVector: vector_float3) -> SKFieldNode](./lineargravityfield%28withvector%29.md)
  Creates a field node that accelerates physics bodies in a specific direction.
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
- [typealias SKFieldForceEvaluator](../skfieldforceevaluator.md)
  The definition for a custom block that processes a single physics body’s interaction with the field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skfieldnode/customfield(evaluationblock:))*