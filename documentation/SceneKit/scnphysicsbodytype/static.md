# SCNPhysicsBodyType.static

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

A physics body that is unaffected by forces or collisions and cannot move.

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
case `static`
```

```c
SCNPhysicsBodyTypeStatic
```

#### Discussion

Use static bodies to construct fixtures in your scene that other bodies need to collide with but that do not themselves move, such as floors, walls, and terrain.

## See Also

### Constants
- [SCNPhysicsBodyType.dynamic](./dynamic.md)
  A physics body that can be affected by forces and collisions.
- [SCNPhysicsBodyType.kinematic](./kinematic.md)
  A physics body that is unaffected by forces or collisions but that can cause collisions affecting other bodies when moved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbodytype/static)*