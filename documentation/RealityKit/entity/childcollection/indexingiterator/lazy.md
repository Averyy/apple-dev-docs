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

- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](entity/childcollection/indexingiterator/map(_:).md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](entity/childcollection/indexingiterator/flatmap(_:)-std6.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](entity/childcollection/indexingiterator/flatmap(_:)-7ql02.md)
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](entity/childcollection/indexingiterator/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](entity/childcollection/indexingiterator/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](entity/childcollection/indexingiterator/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/indexingiterator/lazy)*