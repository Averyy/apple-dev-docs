# flatMap(_:)

**Framework**: RealityKit  
**Kind**: method

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- Swift ?+

## Declaration

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```

## See Also

- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](entity/childcollection/map(_:)-78ywb.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](entity/childcollection/flatmap(_:)-5ijyo.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](entity/childcollection/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](entity/childcollection/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](entity/childcollection/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [var lazy: LazySequence<Self>](entity/childcollection/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/flatmap(_:)-9ovg6)*