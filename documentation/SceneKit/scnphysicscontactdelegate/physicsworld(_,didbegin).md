# physicsWorld(_:didBegin:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that two bodies have come into contact.

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
optional func physicsWorld(_ world: SCNPhysicsWorld, didBegin contact: SCNPhysicsContact)
```

```objc
- (void) physicsWorld:(SCNPhysicsWorld *) world didBeginContact:(SCNPhysicsContact *) contact;
```

## Parameters

- `world`: The physics world that is processing the contact.
- `contact`: An object that describes the contact.

## See Also

### Responding to Contact Events
- [func physicsWorld(SCNPhysicsWorld, didUpdate: SCNPhysicsContact)](./physicsworld%28_,didupdate%29.md)
  Tells the delegate that new information is available about an ongoing contact.
- [func physicsWorld(SCNPhysicsWorld, didEnd: SCNPhysicsContact)](./physicsworld%28_,didend%29.md)
  Tells the delegate that a contact has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicscontactdelegate/physicsworld(_:didbegin:))*