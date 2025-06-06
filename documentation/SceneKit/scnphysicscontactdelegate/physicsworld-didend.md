# physicsWorld(_:didEnd:)

**Framework**: SceneKit  
**Kind**: method

Tells the delegate that a contact has ended.

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
optional func physicsWorld(_ world: SCNPhysicsWorld, didEnd contact: SCNPhysicsContact)
```

## Parameters

- `world`: The physics world that is processing the contact.
- `contact`: An object that describes the contact.

## See Also

- [func physicsWorld(SCNPhysicsWorld, didBegin: SCNPhysicsContact)](scnphysicscontactdelegate/physicsworld(_:didbegin:).md)
  Tells the delegate that two bodies have come into contact.
- [func physicsWorld(SCNPhysicsWorld, didUpdate: SCNPhysicsContact)](scnphysicscontactdelegate/physicsworld(_:didupdate:).md)
  Tells the delegate that new information is available about an ongoing contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicscontactdelegate/physicsworld(_:didend:))*