# lexicographicallyPrecedes(_:by:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.

**Availability**:
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func lexicographicallyPrecedes<OtherSequence>(_ other: OtherSequence, by areInIncreasingOrder: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool where OtherSequence : Sequence, Self.Element == OtherSequence.Element
```

#### Return Value

`true` if this sequence precedes `other` in a dictionary ordering as ordered by `areInIncreasingOrder`; otherwise, `false`.

#### Discussion

The predicate must be a  over the elements. That is, for any elements `a`, `b`, and `c`, the following conditions must hold:

- `areInIncreasingOrder(a, a)` is always `false`. (Irreflexivity)
- If `areInIncreasingOrder(a, b)` and `areInIncreasingOrder(b, c)` are both `true`, then `areInIncreasingOrder(a, c)` is also `true`. (Transitive comparability)
- Two elements are  if neither is ordered before the other according to the predicate. If `a` and `b` are incomparable, and `b` and `c` are incomparable, then `a` and `c` are also incomparable. (Transitive incomparability)

> **Note**: This method implements the mathematical notion of lexicographical ordering, which has no connection to Unicode.  If you are sorting strings to present to the end user, use `String` APIs that perform localized comparison instead.

> **Note**: O(), where  is the lesser of the length of the sequence and the length of `other`.

## Parameters

- `other`: A sequence to compare to this sequence.
- `areInIncreasingOrder`: A predicate that returns   if its first   argument should be ordered before its second argument; otherwise,   .

## See Also

- [static func == (Data, Data) -> Bool](data/==(_:_:).md)
  Returns `true` if the two `Data` arguments are equal.
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](data/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](data/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](data/lexicographicallyprecedes(_:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/lexicographicallyprecedes(_:by:))*