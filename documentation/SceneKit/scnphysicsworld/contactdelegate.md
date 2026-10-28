# contactDelegate

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A delegate that is called when two physics bodies come in contact with each other.

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
weak var contactDelegate: (any SCNPhysicsContactDelegate)? { get set }
```

```objc
@property (atomic, weak, nullable) id<SCNPhysicsContactDelegate> contactDelegate;
```

## Discussion

A contact is created when two physics bodies overlap and one of the physics bodies has a [`collisionBitMask`](../scnphysicsbody/collisionbitmask.md) property that overlaps with the other body’s [`categoryBitMask`](../scnphysicsbody/categorybitmask.md) property.

## See Also

### Detecting Contacts Between Physics Bodies
- [func contactTestBetween(SCNPhysicsBody, SCNPhysicsBody, options: [SCNPhysicsWorld.TestOption : Any]?) -> [SCNPhysicsContact]](./contacttestbetween%28_,_,options%29.md)
  Checks for contacts between two physics bodies.
- [func contactTest(with: SCNPhysicsBody, options: [SCNPhysicsWorld.TestOption : Any]?) -> [SCNPhysicsContact]](./contacttest%28with,options%29.md)
  Checks for contacts between one physics body and any other bodies in the physics world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/contactdelegate)*