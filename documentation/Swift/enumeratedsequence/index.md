# EnumeratedSequence.Index

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A type that represents a position in the collection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@frozen
struct Index
```

Available when `Base` conforms to `Collection`.

## Overview

Valid indices consist of the position of every element and a “past the end” position that’s not valid for use as a subscript argument.

## Topics

### Instance Properties
- [let base: Base.Index](./index/base.md)
  The position in the underlying collection.
### Default Implementations
- [Comparable Implementations](./index/comparable-implementations.md)
- [Equatable Implementations](./index/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../comparable.md)
- [Equatable](../equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/enumeratedsequence/index)*