# SCNPhysicsContactDelegate

**Framework**: SceneKit  
**Kind**: protocol  
**Role**: Protocol

Methods you can implement to respond when a contact or collision occurs between two physics bodies in a scene.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
protocol SCNPhysicsContactDelegate : NSObjectProtocol
```

```objc
@protocol SCNPhysicsContactDelegate <NSObject>
```

#### Overview

To receive contact messages, you set the [`contactDelegate`](./scnphysicsworld/contactdelegate.md) property of an [`SCNPhysicsWorld`](./scnphysicsworld.md) object. SceneKit calls your delegate methods when a contact begins, when information about the contact changes, and when the contact ends.

## Topics

### Responding to Contact Events
- [func physicsWorld(SCNPhysicsWorld, didBegin: SCNPhysicsContact)](./scnphysicscontactdelegate/physicsworld%28_,didbegin%29.md)
  Tells the delegate that two bodies have come into contact.
- [func physicsWorld(SCNPhysicsWorld, didUpdate: SCNPhysicsContact)](./scnphysicscontactdelegate/physicsworld%28_,didupdate%29.md)
  Tells the delegate that new information is available about an ongoing contact.
- [func physicsWorld(SCNPhysicsWorld, didEnd: SCNPhysicsContact)](./scnphysicscontactdelegate/physicsworld%28_,didend%29.md)
  Tells the delegate that a contact has ended.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Collision and Contact Detection
- [class SCNPhysicsContact](./scnphysicscontact.md)
  Detailed information about a contact between two physics bodies in a scene’s physics simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicscontactdelegate)*