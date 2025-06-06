# MLDataValue.DictionaryType.Index

**Framework**: Create ML  
**Kind**: struct

A type that represents a position in the collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Index
```

#### Overview

Valid indices consist of the position of every element and a “past the end” position that’s not valid for use as a subscript argument.

## Topics

### Comparing dictionary types
- [static func == (MLDataValue.DictionaryType.Index, MLDataValue.DictionaryType.Index) -> Bool](mldatavalue/dictionarytype/index/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (MLDataValue.DictionaryType.Index, MLDataValue.DictionaryType.Index) -> Bool](mldatavalue/dictionarytype/index/_(_:_:).md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
### Default Implementations
- [Comparable Implementations](mldatavalue/dictionarytype/index/comparable-implementations.md)
- [Equatable Implementations](mldatavalue/dictionarytype/index/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/index)*