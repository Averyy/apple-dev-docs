# <=(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.

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
func <= (lhs: (), rhs: ()) -> Bool
```

## Discussion

An arity zero tuple is always before or the same as another arity zero tuple in a lexicographical ordering.

## Parameters

- `lhs`: An empty tuple.
- `rhs`: An empty tuple.

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
- [func > <A, B, C, D>((A, B, C, D), (A, B, C, D)) -> Bool](./op%28_,_%29-5gb41.md)
  Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/_=(_:_:)-16p1e)*