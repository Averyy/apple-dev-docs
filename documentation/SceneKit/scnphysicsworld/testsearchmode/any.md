# any

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

Searches should return only the first contact found regardless of its position relative to the search parameters.

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
static let any: SCNPhysicsWorld.TestSearchMode
```

```c
extern SCNPhysicsTestSearchMode const SCNPhysicsTestSearchModeAny;
```

## See Also

### Type Properties
- [static let all: SCNPhysicsWorld.TestSearchMode](./all.md)
  Searches should return all contacts matching the search parameters.
- [static let closest: SCNPhysicsWorld.TestSearchMode](./closest.md)
  Searches should return only the closest contact to the beginning of the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/testsearchmode/any)*