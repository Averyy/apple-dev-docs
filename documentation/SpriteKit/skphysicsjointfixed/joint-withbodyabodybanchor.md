# joint(withBodyA:bodyB:anchor:)

**Framework**: SpriteKit  
**Kind**: method

Creates a new fixed joint.

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
class func joint(withBodyA bodyA: SKPhysicsBody, bodyB: SKPhysicsBody, anchor: CGPoint) -> SKPhysicsJointFixed
```

#### Return Value

A new fixed joint.

#### Discussion

You must add the joint to a physics world associated with the scene before it takes effect.

## Parameters

- `bodyA`: The first body to connect. The body must be connected to a node that is already part of the scene’s node tree.
- `bodyB`: The second body to connect. The body must be connected to a node that is already part of the scene’s node tree.
- `anchor`: The anchor point for the connection in the scene’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointfixed/joint(withbodya:bodyb:anchor:))*