# starts(with:by:)

**Framework**: Create ML  
**Kind**: method

Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func starts<PossiblePrefix>(with possiblePrefix: PossiblePrefix, by areEquivalent: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool where PossiblePrefix : Sequence
```

#### Return Value

`true` if the initial elements of the sequence are equivalent to the elements of `possiblePrefix`; otherwise, `false`. If `possiblePrefix` has no elements, the return value is `true`.

#### Discussion

The predicate must be an  over the elements. That is, for any elements `a`, `b`, and `c`, the following conditions must hold:

- `areEquivalent(a, a)` is always `true`. (Reflexivity)
- `areEquivalent(a, b)` implies `areEquivalent(b, a)`. (Symmetry)
- If `areEquivalent(a, b)` and `areEquivalent(b, c)` are both `true`, then `areEquivalent(a, c)` is also `true`. (Transitivity)

> **Note**: O(), where  is the lesser of the length of the sequence and the length of `possiblePrefix`.

O(), where  is the lesser of the length of the sequence and the length of `possiblePrefix`.

## Parameters

- `possiblePrefix`: A sequence to compare to this sequence.
- `areEquivalent`: A predicate that returns   if its two arguments   are equivalent; otherwise,  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/columnnames-swift.struct/starts(with:by:))*