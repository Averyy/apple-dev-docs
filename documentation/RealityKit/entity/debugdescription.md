# debugDescription

**Framework**: RealityKit  
**Kind**: property

A human readable description of the entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var debugDescription: String { get }
```

## See Also

- [var scene: Scene?](entity/scene.md)
  The scene that owns the entity.
- [var name: String](entity/name.md)
  The name of the entity.
- [func findEntity(named: String) -> Entity?](entity/findentity(named:).md)
  Recursively searches all descendant entities for one with the given name.
- [var id: UInt64](entity/id-8kxa.md)
  The stable identity of the entity associated with this instance.
- [typealias ID](entity/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/debugdescription)*