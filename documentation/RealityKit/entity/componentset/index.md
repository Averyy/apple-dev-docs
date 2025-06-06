# Entity.ComponentSet.Index

**Framework**: RealityKit  
**Kind**: struct

A type that represents a position in the collection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct Index
```

#### Overview

Valid indices consist of the position of every element and a “past the end” position that’s not valid for use as a subscript argument.

## Topics

### Operators
- [static func == (Entity.ComponentSet.Index, Entity.ComponentSet.Index) -> Bool](entity/componentset/index/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (Entity.ComponentSet.Index, Entity.ComponentSet.Index) -> Bool](entity/componentset/index/_(_:_:).md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
### Default Implementations
- [Comparable Implementations](entity/componentset/index/comparable-implementations.md)
- [Equatable Implementations](entity/componentset/index/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/index)*