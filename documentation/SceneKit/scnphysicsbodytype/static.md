# SCNPhysicsBodyType.static

**Framework**: SceneKit  
**Kind**: case

A physics body that is unaffected by forces or collisions and cannot move.

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
case `static`
```

#### Discussion

Use static bodies to construct fixtures in your scene that other bodies need to collide with but that do not themselves move, such as floors, walls, and terrain.

## See Also

- [SCNPhysicsBodyType.dynamic](scnphysicsbodytype/dynamic.md)
  A physics body that can be affected by forces and collisions.
- [SCNPhysicsBodyType.kinematic](scnphysicsbodytype/kinematic.md)
  A physics body that is unaffected by forces or collisions but that can cause collisions affecting other bodies when moved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbodytype/static)*