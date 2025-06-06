# AnyHashable

**Framework**: Swift  
**Kind**: struct

A type-erased hashable value.

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
struct AnyHashable
```

#### Overview

The `AnyHashable` type forwards equality comparisons and hashing operations to an underlying hashable value, hiding the type of the wrapped value.

Where conversion using `as` or `as?` is possible between two types (such as `Int` and `NSNumber`), `AnyHashable` uses a canonical representation of the type-erased value so that instances wrapping the same value of either type compare as equal. For example, `AnyHashable(42)` compares as equal to `AnyHashable(42 as NSNumber)`.

You can store mixed-type keys in dictionaries and other collections that require `Hashable` conformance by wrapping mixed-type keys in `AnyHashable` instances:

```swift
let descriptions: [AnyHashable: Any] = [
    42: "an Int",
    43 as Int8: "an Int8",
    ["a", "b"] as Set: "a set of strings"
]
print(descriptions[42]!)                // prints "an Int"
print(descriptions[42 as Int8]!)        // prints "an Int"
print(descriptions[43 as Int8]!)        // prints "an Int8"
print(descriptions[44])                 // prints "nil"
print(descriptions[["a", "b"] as Set]!) // prints "a set of strings"
```

Note that `AnyHashable` does not guarantee that it preserves the hash encoding of wrapped values. Do not rely on `AnyHashable` generating such compatible hashes, as the hash encoding that it uses may change between any two releases of the standard library.

## Topics

### Initializers
- [init<H>(H)](anyhashable/init(_:).md)
  Creates a type-erased hashable value that wraps the given instance.
### Instance Properties
- [var base: Any](anyhashable/base.md)
  The value wrapped by this instance.
### Default Implementations
- [CustomDebugStringConvertible Implementations](anyhashable/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](anyhashable/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](anyhashable/customstringconvertible-implementations.md)
- [Equatable Implementations](anyhashable/equatable-implementations.md)
- [Hashable Implementations](anyhashable/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)

## See Also

- [struct AnySequence](anysequence.md)
  A type-erased sequence.
- [struct AnyCollection](anycollection.md)
  A type-erased wrapper over any collection with indices that support forward traversal.
- [struct AnyBidirectionalCollection](anybidirectionalcollection.md)
  A type-erased wrapper over any collection with indices that support bidirectional traversal.
- [struct AnyRandomAccessCollection](anyrandomaccesscollection.md)
  A type-erased wrapper over any collection with indices that support random access traversal.
- [struct AnyIterator](anyiterator.md)
  A type-erased iterator of `Element`.
- [struct AnyIndex](anyindex.md)
  A wrapper over an underlying index that hides the specific underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyhashable)*