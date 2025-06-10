# didClone(from:)

**Framework**: RealityKit  
**Kind**: method

Tells a newly cloned entity that cloning is complete.

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
@preconcurrency func didClone(from source: Entity)
```

#### Discussion

This method clones all component data automatically. When you clone an entity that stores custom data that’s not part of a component, override the [`didClone(from:)`](entity/didclone(from:).md) method to copy that data manually after the clone finishes.

## Parameters

- `source`: The entity from which the cloned entity was copied.

## See Also

- [init()](entity/init.md)
  Creates a new entity.
- [convenience init<each T>(components: repeat each T)](entity/init(components:)-80z41.md)
  Creates an entity with one or multiple components.
- [convenience init(components: [any Component])](entity/init(components:)-41rn1.md)
  Creates an entity with multiple components.
- [func clone(recursive: Bool) -> Self](entity/clone(recursive:).md)
  Duplicates an entity to create a new entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/didclone(from:))*