# joint(withBodyA:bodyB:anchorA:anchorB:)

**Framework**: SpriteKit  
**Kind**: method

Creates a new limit joint.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func joint(withBodyA bodyA: SKPhysicsBody, bodyB: SKPhysicsBody, anchorA: CGPoint, anchorB: CGPoint) -> SKPhysicsJointLimit
```

#### Return Value

A new limit joint.

#### Discussion

You must add the joint to a physics world associated with the scene before it takes effect.

## Parameters

- `bodyA`: The first body to connect. The body must be connected to a node that is already part of the scene’s node tree.
- `bodyB`: The second body to connect. The body must be connected to a node that is already part of the scene’s node tree.
- `anchorA`: A connection point on the first body in the scene’s coordinate system.
- `anchorB`: A connection point on the second body in the scene’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointlimit/joint(withbodya:bodyb:anchora:anchorb:))*