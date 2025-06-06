# SCNPhysicsWorld.TestSearchMode

**Framework**: SceneKit  
**Kind**: struct

Options affecting how SceneKit searches for bodies in a collision, ray, or sweep test, used with the [`searchMode`](scnphysicsworld/testoption/searchmode.md) key.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct TestSearchMode
```

## Topics

### Type Properties
- [static let all: SCNPhysicsWorld.TestSearchMode](scnphysicsworld/testsearchmode/all.md)
  Searches should return all contacts matching the search parameters.
- [static let any: SCNPhysicsWorld.TestSearchMode](scnphysicsworld/testsearchmode/any.md)
  Searches should return only the first contact found regardless of its position relative to the search parameters.
- [static let closest: SCNPhysicsWorld.TestSearchMode](scnphysicsworld/testsearchmode/closest.md)
  Searches should return only the closest contact to the beginning of the search.
### Initializers
- [init(rawValue: String)](scnphysicsworld/testsearchmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static let backfaceCulling: SCNPhysicsWorld.TestOption](scnphysicsworld/testoption/backfaceculling.md)
  The key for choosing whether to ignore back-facing polygons in physics shapes when searching for contacts.
- [static let collisionBitMask: SCNPhysicsWorld.TestOption](scnphysicsworld/testoption/collisionbitmask.md)
  The key for selecting which categories of physics bodies that SceneKit should test for contacts.
- [static let searchMode: SCNPhysicsWorld.TestOption](scnphysicsworld/testoption/searchmode.md)
  The key for selecting the number and order of contacts to be tested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/testsearchmode)*