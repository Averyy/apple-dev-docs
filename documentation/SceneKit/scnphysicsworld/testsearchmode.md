# SCNPhysicsWorld.TestSearchMode

**Framework**: SceneKit  
**Kind**: struct  
**Role**: Structure

Options affecting how SceneKit searches for bodies in a collision, ray, or sweep test, used with the [`searchMode`](./testoption/searchmode.md) key.

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
struct TestSearchMode
```

```c
typedef NSString * SCNPhysicsTestSearchMode;
```

## Topics

### Type Properties
- [static let all: SCNPhysicsWorld.TestSearchMode](./testsearchmode/all.md)
  Searches should return all contacts matching the search parameters.
- [static let any: SCNPhysicsWorld.TestSearchMode](./testsearchmode/any.md)
  Searches should return only the first contact found regardless of its position relative to the search parameters.
- [static let closest: SCNPhysicsWorld.TestSearchMode](./testsearchmode/closest.md)
  Searches should return only the closest contact to the beginning of the search.
### Initializers
- [init(rawValue: String)](./testsearchmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Type Properties
- [static let backfaceCulling: SCNPhysicsWorld.TestOption](./testoption/backfaceculling.md)
  The key for choosing whether to ignore back-facing polygons in physics shapes when searching for contacts.
- [static let collisionBitMask: SCNPhysicsWorld.TestOption](./testoption/collisionbitmask.md)
  The key for selecting which categories of physics bodies that SceneKit should test for contacts.
- [static let searchMode: SCNPhysicsWorld.TestOption](./testoption/searchmode.md)
  The key for selecting the number and order of contacts to be tested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/testsearchmode)*