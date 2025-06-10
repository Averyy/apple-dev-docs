# SCNPhysicsContactDelegate

**Framework**: SceneKit  
**Kind**: protocol

Methods you can implement to respond when a contact or collision occurs between two physics bodies in a scene.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol SCNPhysicsContactDelegate : NSObjectProtocol
```

#### Overview

To receive contact messages, you set the [`contactDelegate`](scnphysicsworld/contactdelegate.md) property of an [`SCNPhysicsWorld`](scnphysicsworld.md) object. SceneKit calls your delegate methods when a contact begins, when information about the contact changes, and when the contact ends.

## Topics

### Responding to Contact Events
- [func physicsWorld(SCNPhysicsWorld, didBegin: SCNPhysicsContact)](scnphysicscontactdelegate/physicsworld(_:didbegin:).md)
  Tells the delegate that two bodies have come into contact.
- [func physicsWorld(SCNPhysicsWorld, didUpdate: SCNPhysicsContact)](scnphysicscontactdelegate/physicsworld(_:didupdate:).md)
  Tells the delegate that new information is available about an ongoing contact.
- [func physicsWorld(SCNPhysicsWorld, didEnd: SCNPhysicsContact)](scnphysicscontactdelegate/physicsworld(_:didend:).md)
  Tells the delegate that a contact has ended.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SCNPhysicsContact](scnphysicscontact.md)
  Detailed information about a contact between two physics bodies in a scene’s physics simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicscontactdelegate)*