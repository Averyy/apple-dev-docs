# scene

**Framework**: RealityKit  
**Kind**: property

The scene that owns the entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var scene: Scene? { get }
```

#### Discussion

An entity belongs to a scene if the entity is part of a hierarchy that’s rooted in the scene’s [`anchors`](scene/anchors.md) collection.

The value of the property is `nil` if the entity isn’t currently attached to any scene.

## See Also

- [var name: String](entity/name.md)
  The name of the entity.
- [func findEntity(named: String) -> Entity?](entity/findentity(named:).md)
  Recursively searches all descendant entities for one with the given name.
- [var debugDescription: String](entity/debugdescription.md)
  A human readable description of the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/scene)*