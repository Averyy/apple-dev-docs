# name

**Framework**: RealityKit  
**Kind**: property

The name of the entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var name: String { get set }
```

#### Discussion

You can find an entity by name in a scene by calling the scene’s [`findEntity(named:)`](scene/findentity(named:).md) method. Or you can recursively search among the children of a given entity by calling the entity’s [`findEntity(named:)`](entity/findentity(named:).md) method.

Entity names are not guaranteed to be unique. When you search by name, these methods return the first entity encountered with the given name.

## See Also

- [var scene: Scene?](entity/scene.md)
  The scene that owns the entity.
- [func findEntity(named: String) -> Entity?](entity/findentity(named:).md)
  Recursively searches all descendant entities for one with the given name.
- [var debugDescription: String](entity/debugdescription.md)
  A human readable description of the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/name)*