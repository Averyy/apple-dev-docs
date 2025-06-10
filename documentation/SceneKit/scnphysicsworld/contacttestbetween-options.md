# contactTestBetween(_:_:options:)

**Framework**: SceneKit  
**Kind**: method

Checks for contacts between two physics bodies.

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
func contactTestBetween(_ bodyA: SCNPhysicsBody, _ bodyB: SCNPhysicsBody, options: [SCNPhysicsWorld.TestOption : Any]? = nil) -> [SCNPhysicsContact]
```

#### Return Value

An array of [`SCNPhysicsContact`](scnphysicscontact.md) objects describing contacts between the two bodies, or `nil` if the bodies are not in contact.

#### Discussion

SceneKit sends messages to the physics world’s [`contactDelegate`](scnphysicsworld/contactdelegate.md) object only when collisions occur between bodies whose [`collisionBitMask`](scnphysicsbody/collisionbitmask.md) and [`categoryBitMask`](scnphysicsbody/categorybitmask.md) properties overlap, and only for collisions between certain types of bodies. (For details, see [`SCNPhysicsBodyType`](scnphysicsbodytype.md).) Use this method to directly test for contacts between any two bodies at a time of your choosing. For example, to implement a game where the player character can pick up an item, you might call this method when the player presses the “pick up” button to see if the player character is in contact with the item to be picked up.

## Parameters

- `bodyA`: The first body (to test for contact with the second).
- `bodyB`: The second body (to test for contact with the first).
- `options`: A dictionary of options affecting the test, or   to use default options. For applicable keys and the possible values, see  .

## See Also

- [var contactDelegate: (any SCNPhysicsContactDelegate)?](scnphysicsworld/contactdelegate.md)
  A delegate that is called when two physics bodies come in contact with each other.
- [func contactTest(with: SCNPhysicsBody, options: [SCNPhysicsWorld.TestOption : Any]?) -> [SCNPhysicsContact]](scnphysicsworld/contacttest(with:options:).md)
  Checks for contacts between one physics body and any other bodies in the physics world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/contacttestbetween(_:_:options:))*