# searchMode

**Framework**: SceneKit  
**Kind**: property

The key for selecting the number and order of contacts to be tested.

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
static let searchMode: SCNPhysicsWorld.TestOption
```

#### Discussion

See `Physics Test Search Modes` for possible values. The default value is [`any`](scnphysicsworld/testsearchmode/any.md).

This key applies only to ray and convex sweep tests.

## See Also

- [static let backfaceCulling: SCNPhysicsWorld.TestOption](scnphysicsworld/testoption/backfaceculling.md)
  The key for choosing whether to ignore back-facing polygons in physics shapes when searching for contacts.
- [static let collisionBitMask: SCNPhysicsWorld.TestOption](scnphysicsworld/testoption/collisionbitmask.md)
  The key for selecting which categories of physics bodies that SceneKit should test for contacts.
- [SCNPhysicsWorld.TestSearchMode](scnphysicsworld/testsearchmode.md)
  Options affecting how SceneKit searches for bodies in a collision, ray, or sweep test, used with the [`searchMode`](scnphysicsworld/testoption/searchmode.md) key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/testoption/searchmode)*