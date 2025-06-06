# id

**Framework**: RealityKit  
**Kind**: property

The stable identity of the entity associated with this instance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
nonisolated
var id: UInt64 { get }
```

## See Also

- [var scene: Scene?](entity/scene.md)
  The scene that owns the entity.
- [var name: String](entity/name.md)
  The name of the entity.
- [func findEntity(named: String) -> Entity?](entity/findentity(named:).md)
  Recursively searches all descendant entities for one with the given name.
- [typealias ID](entity/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
- [var debugDescription: String](entity/debugdescription.md)
  A human readable description of the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/id-8kxa)*