# clone(recursive:)

**Framework**: RealityKit  
**Kind**: method

Duplicates an entity to create a new entity.

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
@preconcurrency func clone(recursive: Bool) -> Self
```

#### Return Value

The duplicate.

#### Discussion

All component data is cloned automatically. If you clone an entity that stores custom data that’s not part of a component, override the [`didClone(from:)`](entity/didclone(from:).md) method to copy that data manually.

## Parameters

- `recursive`: A Boolean that you set to   to recursively copy all   the children of the entity. Otherwise, no descendants are copied.

## See Also

- [init()](entity/init.md)
  Creates a new entity.
- [func didClone(from: Entity)](entity/didclone(from:).md)
  Tells a newly cloned entity that cloning is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/clone(recursive:))*