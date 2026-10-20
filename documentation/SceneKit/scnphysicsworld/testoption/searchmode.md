# searchMode

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

The key for selecting the number and order of contacts to be tested.

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
static let searchMode: SCNPhysicsWorld.TestOption
```

```c
extern SCNPhysicsTestOption const SCNPhysicsTestSearchModeKey;
```

#### Discussion

See `Physics Test Search Modes` for possible values. The default value is [`any`](../testsearchmode/any.md).

This key applies only to ray and convex sweep tests.

## See Also

### Type Properties
- [static let backfaceCulling: SCNPhysicsWorld.TestOption](./backfaceculling.md)
  The key for choosing whether to ignore back-facing polygons in physics shapes when searching for contacts.
- [static let collisionBitMask: SCNPhysicsWorld.TestOption](./collisionbitmask.md)
  The key for selecting which categories of physics bodies that SceneKit should test for contacts.
- [SCNPhysicsWorld.TestSearchMode](../testsearchmode.md)
  Options affecting how SceneKit searches for bodies in a collision, ray, or sweep test, used with the [`searchMode`](./searchmode.md) key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/testoption/searchmode)*