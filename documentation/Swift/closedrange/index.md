# ClosedRange.Index

**Framework**: Swift  
**Kind**: enum  
**Role**: Enumeration

A type that represents a position in the collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
enum Index
```

Available when `Bound` conforms to `Strideable` and `Bound.Stride` conforms to `SignedInteger`.

#### Overview

Valid indices consist of the position of every element and a “past the end” position that’s not valid for use as a subscript argument.

## Topics

### Enumeration Cases
- [ClosedRange.Index.inRange(_:)](./index/inrange%28_%29.md)
- [ClosedRange.Index.pastEnd](./index/pastend.md)
### Default Implementations
- [Comparable Implementations](./index/comparable-implementations.md)
- [Equatable Implementations](./index/equatable-implementations.md)
- [Hashable Implementations](./index/hashable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../comparable.md)
- [Equatable](../equatable.md)
- [Hashable](../hashable.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/closedrange/index)*