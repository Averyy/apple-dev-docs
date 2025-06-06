# clone(recursive:)

**Framework**: RealityKit  
**Kind**: method

Duplicates an entity to create a new entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func clone(recursive: Bool) -> Self
```

## Mentions

- [Manipulating Reality Composer scenes from code](manipulating-reality-composer-scenes-from-code.md)

#### Return Value

The duplicate.

#### Discussion

All component data is cloned automatically. If you clone an entity that stores custom data that’s not part of a component, override the [`didClone(from:)`](entity/didclone(from:).md) method to copy that data manually.

## Parameters

- `recursive`: A Boolean that you set to   to recursively copy all   the children of the entity. Otherwise, no descendants are copied.

## See Also

- [init()](entity/init.md)
  Creates a new entity.
- [convenience init<each T>(components: repeat each T)](entity/init(components:)-80z41.md)
  Creates an entity with one or multiple components.
- [convenience init(components: [any Component])](entity/init(components:)-41rn1.md)
  Creates an entity with multiple components.
- [func didClone(from: Entity)](entity/didclone(from:).md)
  Tells a newly cloned entity that cloning is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/clone(recursive:))*