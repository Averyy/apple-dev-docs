# init()

**Framework**: RealityKit  
**Kind**: init

Creates a new entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency required init()
```

## See Also

- [convenience init<each T>(components: repeat each T)](entity/init(components:)-80z41.md)
  Creates an entity with one or multiple components.
- [convenience init(components: [any Component])](entity/init(components:)-41rn1.md)
  Creates an entity with multiple components.
- [func clone(recursive: Bool) -> Self](entity/clone(recursive:).md)
  Duplicates an entity to create a new entity.
- [func didClone(from: Entity)](entity/didclone(from:).md)
  Tells a newly cloned entity that cloning is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/init())*