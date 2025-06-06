# EnumeratedSequence

**Framework**: Swift  
**Kind**: struct

An enumeration of the elements of a sequence or collection.

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
struct EnumeratedSequence<Base> where Base : Sequence
```

#### Overview

`EnumeratedSequence` is a sequence of pairs (, ), where s are consecutive `Int` values starting at zero, and s are the elements of a base sequence.

To create an instance of `EnumeratedSequence`, call `enumerated()` on a sequence or collection. The following example enumerates the elements of an array.

```swift
var s = ["foo", "bar"].enumerated()
for (n, x) in s {
    print("\(n): \(x)")
}
// Prints "0: foo"
// Prints "1: bar"
```

## Topics

### Default Implementations
- [Sequence Implementations](enumeratedsequence/sequence-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Sendable](sendable.md)
- [Sequence](sequence.md)

## See Also

- [struct CollectionDifference](collectiondifference.md)
  A collection of insertions and removals that describe the difference between two ordered collection states.
- [struct DropFirstSequence](dropfirstsequence.md)
  A sequence that lazily consumes and drops `n` elements from an underlying `Base` iterator before possibly returning the first available element.
- [struct DropWhileSequence](dropwhilesequence.md)
  A sequence that lazily consumes and drops `n` elements from an underlying `Base` iterator before possibly returning the first available element.
- [typealias FlattenCollection](flattencollection.md)
- [struct FlattenSequence](flattensequence.md)
  A sequence consisting of all the elements contained in each segment contained in some `Base` sequence.
- [struct JoinedSequence](joinedsequence.md)
  A sequence that presents the elements of a base sequence of sequences concatenated using a given separator.
- [struct PrefixSequence](prefixsequence.md)
  A sequence that only consumes up to `n` elements from an underlying `Base` iterator.
- [struct Repeated](repeated.md)
  A collection whose elements are all identical.
- [struct ReversedCollection](reversedcollection.md)
  A collection that presents the elements of its base collection in reverse order.
- [struct StrideTo](strideto.md)
  A sequence of values formed by striding over a half-open interval.
- [struct StrideThrough](stridethrough.md)
  A sequence of values formed by striding over a closed interval.
- [struct UnfoldSequence](unfoldsequence.md)
  A sequence whose elements are produced via repeated applications of a closure to some mutable state.
- [struct Zip2Sequence](zip2sequence.md)
  A sequence of pairs built out of two underlying sequences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/enumeratedsequence)*