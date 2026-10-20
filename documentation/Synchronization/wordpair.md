# WordPair

**Framework**: Synchronization  
**Kind**: struct  
**Role**: Structure

A pair of two word sized `UInt`s.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@frozen
struct WordPair
```

#### Overview

This type’s primary purpose is to be used in double wide atomic operations. On platforms that support it, atomic operations on `WordPair` are done in a single operation for two words. Users can use this type as itself when used on `Atomic`, or it could be used as an intermediate step for custom `AtomicRepresentable` types that are also double wide.

```swift
let atomicPair = Atomic<WordPair>(WordPair(first: 0, second: 0))
atomicPair.store(WordPair(first: someVersion, second: .max), ordering: .relaxed)
```

When used as an intermediate step for custom `AtomicRepresentable` types, it is critical that their `AtomicRepresentation` be equal to `WordPair.AtomicRepresentation`.

```swift
struct GridPoint {
  var x: Int
  var y: Int
}

extension GridPoint: AtomicRepresentable {
  typealias AtomicRepresentation = WordPair.AtomicRepresentation

  ...
}
```

> **Note**: This type only conforms to `AtomicRepresentable` on platforms that support double wide atomics.

## Topics

### Initializers
- [init(first: UInt, second: UInt)](./wordpair/init%28first,second%29.md)
  Initialize a new `WordPair` value given both individual words.
### Instance Properties
- [var first: UInt](./wordpair/first.md)
  The first element in this word pair.
- [var second: UInt](./wordpair/second.md)
  The second element in this word pair.
### Default Implementations
- [AtomicRepresentable Implementations](./wordpair/atomicrepresentable-implementations.md)
- [CustomDebugStringConvertible Implementations](./wordpair/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./wordpair/customstringconvertible-implementations.md)
- [Equatable Implementations](./wordpair/equatable-implementations.md)
- [Hashable Implementations](./wordpair/hashable-implementations.md)

## Relationships

### Conforms To
- [AtomicRepresentable](./atomicrepresentable.md)
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Comparable](../Swift/comparable.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Atomic Values
- [struct Atomic](./atomic.md)
  An atomic value.
- [struct AtomicLazyReference](./atomiclazyreference.md)
  A lazily initializable atomic strong reference.
- [protocol AtomicRepresentable](./atomicrepresentable.md)
  A type that supports atomic operations through a separate atomic storage representation.
- [protocol AtomicOptionalRepresentable](./atomicoptionalrepresentable.md)
  An atomic value that also supports atomic operations when wrapped in an `Optional`. Atomic optional representable types come with a standalone atomic representation for their optional-wrapped variants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/wordpair)*