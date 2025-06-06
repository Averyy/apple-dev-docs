# joint(withBodyA:bodyB:anchor:axis:)

**Framework**: SpriteKit  
**Kind**: method

Creates a new sliding joint.

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
class func joint(withBodyA bodyA: SKPhysicsBody, bodyB: SKPhysicsBody, anchor: CGPoint, axis: CGVector) -> SKPhysicsJointSliding
```

#### Return Value

A new sliding joint.

#### Discussion

You must add the joint to a physics world associated with the scene before it takes effect.

## Parameters

- `bodyA`: The first body to connect. The body must be connected to a node that is already part of the scene’s node tree.
- `bodyB`: The second body to connect. The body must be connected to a node that is already part of the scene’s node tree.
- `anchor`: The anchor point for the connection in the scene’s coordinate system.
- `axis`: A vector that defines the direction that the joint is allowed to slide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding/joint(withbodya:bodyb:anchor:axis:))*