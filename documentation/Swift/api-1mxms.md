# !=(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether two types are not identical.

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
func != (t0: (any (~Copyable & ~Escapable).Type)?, t1: (any (~Copyable & ~Escapable).Type)?) -> Bool
```

#### Return Value

`true` if one, but not both, of `t0` and `t1` are `nil`, or if they represent different types; otherwise, `false`.

## Parameters

- `t0`: A type to compare.
- `t1`: Another type to compare.

## See Also

- [func == ((), ()) -> Bool](==(_:_:)-958in.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == <A, B>((A, B), (A, B)) -> Bool](==(_:_:)-2htbb.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == <A, B, C>((A, B, C), (A, B, C)) -> Bool](==(_:_:)-h88g.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == <A, B, C, D>((A, B, C, D), (A, B, C, D)) -> Bool](==(_:_:)-7lhq7.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == <A, B, C, D, E>((A, B, C, D, E), (A, B, C, D, E)) -> Bool](==(_:_:)-1hbor.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == <A, B, C, D, E, F>((A, B, C, D, E, F), (A, B, C, D, E, F)) -> Bool](==(_:_:)-1ud2a.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == ((any (~Copyable & ~Escapable).Type)?, (any (~Copyable & ~Escapable).Type)?) -> Bool](==(_:_:)-9kf9y.md)
  Returns a Boolean value indicating whether two types are identical.
- [func != ((), ()) -> Bool](!=(_:_:)-18co7.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B>((A, B), (A, B)) -> Bool](!=(_:_:)-7er1l.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B, C>((A, B, C), (A, B, C)) -> Bool](!=(_:_:)-754t2.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B, C, D>((A, B, C, D), (A, B, C, D)) -> Bool](!=(_:_:)-7ao4l.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B, C, D, E>((A, B, C, D, E), (A, B, C, D, E)) -> Bool](!=(_:_:)-4fzl6.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B, C, D, E, F>((A, B, C, D, E, F), (A, B, C, D, E, F)) -> Bool](!=(_:_:)-3nrcc.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/!=(_:_:)-1mxms)*