# findEntity(named:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Recursively searches all descendant entities for one with the given name.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func findEntity(named name: String) -> Entity?
```

#### Return Value

An entity with the given name, or `nil` if no entity is found.

#### Discussion

The [`findEntity(named:)`](./findentity%28named%29.md) method conducts a depth-first, recursive search over all of the entity’s descendants for one whose [`name`](./name.md) property matches the given name. The method returns the first match. Entity names need not be unique.

## Parameters

- `name`: The entity name for which to search.

## See Also

### Inspecting an entity
- [var scene: Scene?](./scene.md)
  The scene that owns the entity.
- [var name: String](./name.md)
  The name of the entity.
- [var debugDescription: String](./debugdescription.md)
  A human readable description of the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/findentity(named:))*