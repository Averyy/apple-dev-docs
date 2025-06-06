# lazy

**Framework**: RealityKit  
**Kind**: property

A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var lazy: LazySequence<Self> { get }
```

## See Also

- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](queryresult/map(_:).md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](queryresult/flatmap(_:)-6wvi7.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](queryresult/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](queryresult/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](queryresult/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](queryresult/flatmap(_:)-icze.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/queryresult/lazy)*