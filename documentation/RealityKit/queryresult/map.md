# map(_:)

**Framework**: RealityKit  
**Kind**: method

Returns an array containing the results of mapping the given closure over the sequence’s elements.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func map<T, E>(_ transform: (Self.Element) throws(E) -> T) throws(E) -> [T] where E : Error
```

#### Return Value

An array containing the transformed elements of this sequence.

#### Discussion

In this example, `map` is used first to convert the names in the array to lowercase strings and then to count their characters.

```None
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
let lowercaseNames = cast.map { $0.lowercased() }
// 'lowercaseNames' == ["vivien", "marlon", "kim", "karl"]
let letterCounts = cast.map { $0.count }
// 'letterCounts' == [6, 6, 3, 4]
```

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

## Parameters

- `transform`: A mapping closure.   accepts an   element of this sequence as its parameter and returns a transformed   value of the same or of a different type.

## See Also

- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](queryresult/flatmap(_:)-6wvi7.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](queryresult/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](queryresult/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](queryresult/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [var lazy: LazySequence<Self>](queryresult/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](queryresult/flatmap(_:)-icze.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/queryresult/map(_:))*