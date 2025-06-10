# SKPhysicsContactDelegate

**Framework**: SpriteKit  
**Kind**: protocol

Methods your app can implement to respond when physics bodies come into contact.

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
protocol SKPhysicsContactDelegate : NSObjectProtocol
```

## Mentions

- [Responding to Frame-Cycle Events](responding-to-frame-cycle-events.md)
- [Getting Started with Physics](getting-started-with-physics.md)

#### Overview

An object that implements the [`SKPhysicsContactDelegate`](skphysicscontactdelegate.md) protocol can respond when two physics bodies with overlapping [`contactTestBitMask`](skphysicsbody/contacttestbitmask.md) values are in contact with each other in a physics world. To receive contact messages, you set the [`contactDelegate`](skphysicsworld/contactdelegate.md) property of a [`SKPhysicsWorld`](skphysicsworld.md) object. The delegate is called when a contact starts or ends.

> ❗ **Important**:  The physics contact delegate methods are called during the physics simulation step. During that time, the physics world can’t be modified and the behavior of any changes to the physics bodies in the simulation is undefined. If you need to make such changes, set a flag inside [`didBegin(_:)`](skphysicscontactdelegate/didbegin(_:).md) or [`didEnd(_:)`](skphysicscontactdelegate/didend(_:).md) and make changes in response to that flag in the [`update(_:for:)`](skscenedelegate/update(_:for:).md) method in a [`SKSceneDelegate`](skscenedelegate.md).

You can use the contact delegate to play a sound or execute game logic, such as increasing a player’s score, when a contact event occurs. The following code shows how to display a shockwave effect when two nodes with the name `ball` come into contact. The code only creates the effect when the collision impulse is above a specified threshold:

Listing 1. Creating a shockwave effect when objects come into contact

```swift
let shockWaveAction: SKAction = {
    let growAndFadeAction = SKAction.group([SKAction.scale(to: 50, duration: 0.5),
                                            SKAction.fadeOut(withDuration: 0.5)])
    
    let sequence = SKAction.sequence([growAndFadeAction,
                                      SKAction.removeFromParent()])
    
    return sequence
}()

func didBegin(_ contact: SKPhysicsContact) {
    if contact.collisionImpulse > 5 &&
        contact.bodyA.node?.name == "ball" &&
        contact.bodyB.node?.name == "ball" {
        
        let shockwave = SKShapeNode(circleOfRadius: 1)

        shockwave.position = contact.contactPoint
        scene.addChild(shockwave)
        
        shockwave.run(shockWaveAction)
    }
}
```

## Topics

### Responding to Contact Events
- [func didBegin(SKPhysicsContact)](skphysicscontactdelegate/didbegin(_:).md)
  Called when two bodies first contact each other.
- [func didEnd(SKPhysicsContact)](skphysicscontactdelegate/didend(_:).md)
  Called when the contact ends between two physics bodies.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Getting Started with Physics](getting-started-with-physics.md)
  Simulate gravity, acceleration, collision detection, or joints.
- [class SKPhysicsWorld](skphysicsworld.md)
  The driver of the physics engine in a scene; it exposes the ability for you to configure and query the physics system.
- [class SKPhysicsBody](skphysicsbody.md)
  An object that adds physics simulation to a node.
- [class SKPhysicsContact](skphysicscontact.md)
  A description of the contact between two physics bodies.
- [class SKFieldNode](skfieldnode.md)
  A node that applies physics effects to nearby nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicscontactdelegate)*