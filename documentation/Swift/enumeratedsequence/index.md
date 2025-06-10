# EnumeratedSequence.Index

**Framework**: Swift  
**Kind**: struct

A type that represents a position in the collection.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@frozen
struct Index
```

#### Overview

Valid indices consist of the position of every element and a “past the end” position that’s not valid for use as a subscript argument.

## Topics

### Instance Properties
- [let base: Base.Index](enumeratedsequence/index/base.md)
  The position in the underlying collection.
### Default Implementations
- [Comparable Implementations](enumeratedsequence/index/comparable-implementations.md)
- [Equatable Implementations](enumeratedsequence/index/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [Equatable](equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/enumeratedsequence/index)*