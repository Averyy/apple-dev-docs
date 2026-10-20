# ==(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Returns a Boolean value indicating whether the corresponding components of two tuples are equal.

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
func == <A, B, C, D, E, F>(lhs: (A, B, C, D, E, F), rhs: (A, B, C, D, E, F)) -> Bool where A : Equatable, B : Equatable, C : Equatable, D : Equatable, E : Equatable, F : Equatable
```

#### Discussion

For two tuples to compare as equal, each corresponding pair of components must be equal. The following example compares tuples made up of 6 components:

```swift
let a = ("a", 1, 2, 3, 4, 5)
let b = ("a", 1, 2, 3, 4, 5)
print(a == b)
// Prints "true"

let c = ("a", 1, 2, 3, 4, 6)
print(a == c)
// Prints "false"
```

## Parameters

- `lhs`: A tuple of `Equatable` elements.
- `rhs`: Another tuple of elements of the same type as `lhs`.

## See Also

### Tuple Comparison
- [func == ((), ()) -> Bool](./eqeq%28_,_%29-958in.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == <A, B>((A, B), (A, B)) -> Bool](./eqeq%28_,_%29-2htbb.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == <A, B, C>((A, B, C), (A, B, C)) -> Bool](./eqeq%28_,_%29-h88g.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == <A, B, C, D>((A, B, C, D), (A, B, C, D)) -> Bool](./eqeq%28_,_%29-7lhq7.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == <A, B, C, D, E>((A, B, C, D, E), (A, B, C, D, E)) -> Bool](./eqeq%28_,_%29-1hbor.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == ((any (~Copyable & ~Escapable).Type)?, (any (~Copyable & ~Escapable).Type)?) -> Bool](./eqeq%28_,_%29-9kf9y.md)
  Returns a Boolean value indicating whether two types are identical.
- [func != ((), ()) -> Bool](./noteq%28_,_%29-18co7.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B>((A, B), (A, B)) -> Bool](./noteq%28_,_%29-7er1l.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B, C>((A, B, C), (A, B, C)) -> Bool](./noteq%28_,_%29-754t2.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B, C, D>((A, B, C, D), (A, B, C, D)) -> Bool](./noteq%28_,_%29-7ao4l.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B, C, D, E>((A, B, C, D, E), (A, B, C, D, E)) -> Bool](./noteq%28_,_%29-4fzl6.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B, C, D, E, F>((A, B, C, D, E, F), (A, B, C, D, E, F)) -> Bool](./noteq%28_,_%29-3nrcc.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != ((any (~Copyable & ~Escapable).Type)?, (any (~Copyable & ~Escapable).Type)?) -> Bool](./noteq%28_,_%29-1mxms.md)
  Returns a Boolean value indicating whether two types are not identical.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/==(_:_:)-1ud2a)*