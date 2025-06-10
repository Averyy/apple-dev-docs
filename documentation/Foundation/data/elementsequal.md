# elementsEqual(_:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.

**Availability**:
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func elementsEqual<OtherSequence>(_ other: OtherSequence) -> Bool where OtherSequence : Sequence, Self.Element == OtherSequence.Element
```

#### Return Value

`true` if this sequence and `other` contain the same elements in the same order.

#### Discussion

At least one of the sequences must be finite.

This example tests whether one countable range shares the same elements as another countable range and an array.

```None
let a = 1...3
let b = 1...10

print(a.elementsEqual(b))
// Prints "false"
print(a.elementsEqual([1, 2, 3]))
// Prints "true"
```

> **Note**: O(), where  is the lesser of the length of the sequence and the length of `other`.

## Parameters

- `other`: A sequence to compare to this sequence.

## See Also

- [static func == (Data, Data) -> Bool](data/==(_:_:).md)
  Returns `true` if the two `Data` arguments are equal.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](data/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](data/lexicographicallyprecedes(_:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](data/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/elementsequal(_:))*