# elementsEqual(_:by:)

**Framework**: TabularData  
**Kind**: method

Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.

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
func elementsEqual<OtherSequence>(_ other: OtherSequence, by areEquivalent: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool where OtherSequence : Sequence
```

#### Return Value

`true` if this sequence and `other` contain equivalent items, using `areEquivalent` as the equivalence test; otherwise, `false.`

#### Discussion

At least one of the sequences must be finite.

The predicate must be an  over the elements. That is, for any elements `a`, `b`, and `c`, the following conditions must hold:

- `areEquivalent(a, a)` is always `true`. (Reflexivity)
- `areEquivalent(a, b)` implies `areEquivalent(b, a)`. (Symmetry)
- If `areEquivalent(a, b)` and `areEquivalent(b, c)` are both `true`, then `areEquivalent(a, c)` is also `true`. (Transitivity)

> **Note**: O(), where  is the lesser of the length of the sequence and the length of `other`.

## Parameters

- `other`: A sequence to compare to this sequence.
- `areEquivalent`: A predicate that returns   if its two arguments   are equivalent; otherwise,  .

## See Also

- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](column/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](column/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/elementsequal(_:by:))*