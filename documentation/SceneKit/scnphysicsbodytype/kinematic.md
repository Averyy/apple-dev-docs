# SCNPhysicsBodyType.kinematic

**Framework**: SceneKit  
**Kind**: case

A physics body that is unaffected by forces or collisions but that can cause collisions affecting other bodies when moved.

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
case kinematic
```

#### Discussion

Use kinematic bodies for scene elements that you want to control directly directly but whose movement manipulates other elements. For example, to allow the user to push objects around with a finger, you might create a kinematic body and attach it to an invisible node that you move to follow touch events. (In macOS, use the same technique to allow the user to move objects with the mouse pointer.)

## See Also

- [SCNPhysicsBodyType.static](scnphysicsbodytype/static.md)
  A physics body that is unaffected by forces or collisions and cannot move.
- [SCNPhysicsBodyType.dynamic](scnphysicsbodytype/dynamic.md)
  A physics body that can be affected by forces and collisions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbodytype/kinematic)*