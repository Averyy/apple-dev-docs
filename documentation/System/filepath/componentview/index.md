# FilePath.ComponentView.Index

**Framework**: System  
**Kind**: struct

A type that represents a position in the collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Index
```

#### Overview

Valid indices consist of the position of every element and a “past the end” position that’s not valid for use as a subscript argument.

## Topics

### Operators
- [static func == (FilePath.ComponentView.Index, FilePath.ComponentView.Index) -> Bool](filepath/componentview/index/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (FilePath.ComponentView.Index, FilePath.ComponentView.Index) -> Bool](filepath/componentview/index/_(_:_:).md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
### Instance Properties
- [var hashValue: Int](filepath/componentview/index/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](filepath/componentview/index/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Comparable Implementations](filepath/componentview/index/comparable-implementations.md)
- [Equatable Implementations](filepath/componentview/index/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/index)*