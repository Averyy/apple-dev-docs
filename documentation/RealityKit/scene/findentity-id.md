# findEntity(id:)

**Framework**: RealityKit  
**Kind**: method

Returns `Entity` with the given `Entity.ID` in the `Scene`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func findEntity(id: Entity.ID) -> Entity?
```

#### Return Value

`Entity` with the given `Entity.ID`, or `nil` if no such `Entity` is found in the `Scene`.

#### Discussion

> **Note**: This method uses efficient mapping from `Entity.ID` to `Entity`, not linear traversal of all Entities in the `Scene`.

## Parameters

- `id`:   obtained from 

## See Also

- [func findEntity(named: String) -> Entity?](scene/findentity(named:).md)
  Searches the scene’s anchor entity hierarchies for an entity with the given name.
- [func performQuery(_:)](scene/performquery(_:).md)
  Returns all entities of the scene which pass the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/findentity(id:))*