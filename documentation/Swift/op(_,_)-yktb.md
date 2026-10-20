# >(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.

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
func > (lhs: (), rhs: ()) -> Bool
```

#### Discussion

An arity zero tuple is never strictly after another arity zero tuple in a lexicographical ordering.

## Parameters

- `lhs`: An empty tuple.
- `rhs`: An empty tuple.

## See Also

- [func < ((), ()) -> Bool](_(_:_:)-1b1cu.md)
  Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [func < <A, B>((A, B), (A, B)) -> Bool](_(_:_:)-4ck5h.md)
  Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [func < <A, B, C>((A, B, C), (A, B, C)) -> Bool](_(_:_:)-23151.md)
  Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [func < <A, B, C, D>((A, B, C, D), (A, B, C, D)) -> Bool](_(_:_:)-6p1tf.md)
  Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [func < <A, B, C, D, E>((A, B, C, D, E), (A, B, C, D, E)) -> Bool](_(_:_:)-3hhjy.md)
  Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [func < <A, B, C, D, E, F>((A, B, C, D, E, F), (A, B, C, D, E, F)) -> Bool](_(_:_:)-8mgtp.md)
  Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [func <= ((), ()) -> Bool](_=(_:_:)-16p1e.md)
  Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [func <= <A, B>((A, B), (A, B)) -> Bool](_=(_:_:)-3jpod.md)
  Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [func <= <A, B, C>((A, B, C), (A, B, C)) -> Bool](_=(_:_:)-8u5uu.md)
  Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [func <= <A, B, C, D>((A, B, C, D), (A, B, C, D)) -> Bool](_=(_:_:)-6kea2.md)
  Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [func <= <A, B, C, D, E>((A, B, C, D, E), (A, B, C, D, E)) -> Bool](_=(_:_:)-1hzxz.md)
  Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [func <= <A, B, C, D, E, F>((A, B, C, D, E, F), (A, B, C, D, E, F)) -> Bool](_=(_:_:)-7n746.md)
  Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [func > <A, B>((A, B), (A, B)) -> Bool](_(_:_:)-4xg09.md)
  Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.
- [func > <A, B, C>((A, B, C), (A, B, C)) -> Bool](_(_:_:)-7p512.md)
  Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.
- [func > <A, B, C, D>((A, B, C, D), (A, B, C, D)) -> Bool](_(_:_:)-5gb41.md)
  Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/_(_:_:)-yktb)*