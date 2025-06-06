# physicsWorld(_:didUpdate:)

**Framework**: SceneKit  
**Kind**: method

Tells the delegate that new information is available about an ongoing contact.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
optional func physicsWorld(_ world: SCNPhysicsWorld, didUpdate contact: SCNPhysicsContact)
```

#### Discussion

SceneKit calls this method on each step of the physics simulation (see the [`timeStep`](scnphysicsworld/timestep.md) property) if information about the contact changes—for example, if two bodies are sliding against one another.

## Parameters

- `world`: The physics world that is processing the contact.
- `contact`: An object that describes the contact.

## See Also

- [func physicsWorld(SCNPhysicsWorld, didBegin: SCNPhysicsContact)](scnphysicscontactdelegate/physicsworld(_:didbegin:).md)
  Tells the delegate that two bodies have come into contact.
- [func physicsWorld(SCNPhysicsWorld, didEnd: SCNPhysicsContact)](scnphysicscontactdelegate/physicsworld(_:didend:).md)
  Tells the delegate that a contact has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicscontactdelegate/physicsworld(_:didupdate:))*