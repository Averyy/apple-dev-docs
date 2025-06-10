# contactTest(with:options:)

**Framework**: SceneKit  
**Kind**: method

Checks for contacts between one physics body and any other bodies in the physics world.

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
func contactTest(with body: SCNPhysicsBody, options: [SCNPhysicsWorld.TestOption : Any]? = nil) -> [SCNPhysicsContact]
```

#### Return Value

An array of [`SCNPhysicsContact`](scnphysicscontact.md) objects describing contacts between the specified body and any others, or `nil` if the body is not in contact with any other bodies.

#### Discussion

SceneKit sends messages to the physics world’s contactdelegate object only when collisions occur between bodies whose [`collisionBitMask`](scnphysicsbody/collisionbitmask.md) and [`categoryBitMask`](scnphysicsbody/categorybitmask.md) properties overlap, and only for collisions between certain types of bodies. (For details, see [`SCNPhysicsBodyType`](scnphysicsbodytype.md).) Use this method to directly test for all contacts between one body and any other bodies at a time of your choosing. For example, to implement a game with a “wall jump” effect, you could call this method when the player presses the jump button to see if the player character is in contact with any walls.

## Parameters

- `body`: The body to test for contact.
- `options`: A dictionary of options affecting the test, or   to use default options. For applicable keys and the possible values, see  .

## See Also

- [var contactDelegate: (any SCNPhysicsContactDelegate)?](scnphysicsworld/contactdelegate.md)
  A delegate that is called when two physics bodies come in contact with each other.
- [func contactTestBetween(SCNPhysicsBody, SCNPhysicsBody, options: [SCNPhysicsWorld.TestOption : Any]?) -> [SCNPhysicsContact]](scnphysicsworld/contacttestbetween(_:_:options:).md)
  Checks for contacts between two physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/contacttest(with:options:))*