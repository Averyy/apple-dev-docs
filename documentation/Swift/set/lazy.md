# lazy

**Framework**: Swift  
**Kind**: property

A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.

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
var lazy: LazySequence<Self> { get }
```

## See Also

- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](set/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](set/flatmap(_:)-i3my.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](set/flatmap(_:)-6chuh.md)
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](set/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](set/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func sorted() -> [Self.Element]](set/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](set/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func shuffled() -> [Self.Element]](set/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](set/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/lazy)*