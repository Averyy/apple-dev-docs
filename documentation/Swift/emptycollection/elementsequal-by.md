# elementsEqual(_:by:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/emptycollection/elementsequal(_:by:))*