# contactDelegate

**Framework**: SceneKit  
**Kind**: property

A delegate that is called when two physics bodies come in contact with each other.

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
weak var contactDelegate: (any SCNPhysicsContactDelegate)? { get set }
```

#### Discussion

A contact is created when two physics bodies overlap and one of the physics bodies has a [`collisionBitMask`](scnphysicsbody/collisionbitmask.md) property that overlaps with the other body’s [`categoryBitMask`](scnphysicsbody/categorybitmask.md) property.

## See Also

- [func contactTestBetween(SCNPhysicsBody, SCNPhysicsBody, options: [SCNPhysicsWorld.TestOption : Any]?) -> [SCNPhysicsContact]](scnphysicsworld/contacttestbetween(_:_:options:).md)
  Checks for contacts between two physics bodies.
- [func contactTest(with: SCNPhysicsBody, options: [SCNPhysicsWorld.TestOption : Any]?) -> [SCNPhysicsContact]](scnphysicsworld/contacttest(with:options:).md)
  Checks for contacts between one physics body and any other bodies in the physics world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/contactdelegate)*