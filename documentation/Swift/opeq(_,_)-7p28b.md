# >=(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Returns a Boolean value indicating whether the first tuple is ordered after or the same as the second in a lexicographical ordering.

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
func >= <A, B, C>(lhs: (A, B, C), rhs: (A, B, C)) -> Bool where A : Comparable, B : Comparable, C : Comparable
```

## Discussion

Given two tuples `(a1, a2, ..., aN)` and `(b1, b2, ..., bN)`, the first tuple is after or the same as the second tuple if and only if `a1 > b1` or (`a1 == b1` and `(a2, ..., aN) >= (b2, ..., bN)`).

## Parameters

- `lhs`: A tuple of `Comparable` elements.
- `rhs`: Another tuple of elements of the same type as `lhs`.

## See Also

### Tuple Comparison
- [func < ((), ()) -> Bool](./op%28_,_%29-1b1cu.md)
  Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [func < <A, B>((A, B), (A, B)) -> Bool](./op%28_,_%29-4ck5h.md)
  Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [func < <A, B, C>((A, B, C), (A, B, C)) -> Bool](./op%28_,_%29-23151.md)
  Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [func < <A, B, C, D>((A, B, C, D), (A, B, C, D)) -> Bool](./op%28_,_%29-6p1tf.md)
  Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [func < <A, B, C, D, E>((A, B, C, D, E), (A, B, C, D, E)) -> Bool](./op%28_,_%29-3hhjy.md)
  Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [func < <A, B, C, D, E, F>((A, B, C, D, E, F), (A, B, C, D, E, F)) -> Bool](./op%28_,_%29-8mgtp.md)
  Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [func <= ((), ()) -> Bool](./opeq%28_,_%29-16p1e.md)
  Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [func <= <A, B>((A, B), (A, B)) -> Bool](./opeq%28_,_%29-3jpod.md)
  Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [func <= <A, B, C>((A, B, C), (A, B, C)) -> Bool](./opeq%28_,_%29-8u5uu.md)
  Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [func <= <A, B, C, D>((A, B, C, D), (A, B, C, D)) -> Bool](./opeq%28_,_%29-6kea2.md)
  Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [func <= <A, B, C, D, E>((A, B, C, D, E), (A, B, C, D, E)) -> Bool](./opeq%28_,_%29-1hzxz.md)
  Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [func <= <A, B, C, D, E, F>((A, B, C, D, E, F), (A, B, C, D, E, F)) -> Bool](./opeq%28_,_%29-7n746.md)
  Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [func > ((), ()) -> Bool](./op%28_,_%29-yktb.md)
  Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.
- [func > <A, B>((A, B), (A, B)) -> Bool](./op%28_,_%29-4xg09.md)
  Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.
- [func > <A, B, C>((A, B, C), (A, B, C)) -> Bool](./op%28_,_%29-7p512.md)
  Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/_=(_:_:)-7p28b)*