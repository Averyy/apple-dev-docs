# !=(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.

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
func != <A, B, C, D, E>(lhs: (A, B, C, D, E), rhs: (A, B, C, D, E)) -> Bool where A : Equatable, B : Equatable, C : Equatable, D : Equatable, E : Equatable
```

#### Discussion

For two tuples to compare as equal, each corresponding pair of components must be equal. The following example compares tuples made up of 5 components:

```swift
let a = ("a", 1, 2, 3, 4)
let b = ("a", 1, 2, 3, 4)
print(a != b)
// Prints "false"

let c = ("a", 1, 2, 3, 5)
print(a != c)
// Prints "true"
```

## Parameters

- `lhs`: A tuple of   elements.
- `rhs`: Another tuple of elements of the same type as  .

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
- [func != <A, B, C, D, E, F>((A, B, C, D, E, F), (A, B, C, D, E, F)) -> Bool](!=(_:_:)-3nrcc.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != ((any (~Copyable & ~Escapable).Type)?, (any (~Copyable & ~Escapable).Type)?) -> Bool](!=(_:_:)-1mxms.md)
  Returns a Boolean value indicating whether two types are not identical.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/!=(_:_:)-4fzl6)*