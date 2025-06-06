# flatMap(_:)

**Framework**: Swift  
**Kind**: method

Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.

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
func flatMap<SegmentOfResult>(_ transform: (Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element] where SegmentOfResult : Sequence
```

#### Return Value

The resulting flattened array.

#### Discussion

Use this method to receive a single-level collection when your transformation produces a sequence or collection for each element.

In this example, note the difference in the result of using `map` and `flatMap` with a transformation that returns an array.

```swift
let numbers = [1, 2, 3, 4]

let mapped = numbers.map { Array(repeating: $0, count: $0) }
// [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4]]

let flatMapped = numbers.flatMap { Array(repeating: $0, count: $0) }
// [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
```

In fact, `s.flatMap(transform)`  is equivalent to `Array(s.map(transform).joined())`.

> **Note**: O( + ), where  is the length of this sequence and  is the length of the result.

O( + ), where  is the length of this sequence and  is the length of the result.

## Parameters

- `transform`: A closure that accepts an element of this   sequence as its argument and returns a sequence or collection.

## See Also

- [func mapValues<T>((Value) throws -> T) rethrows -> Dictionary<Key, T>](dictionary/mapvalues(_:).md)
  Returns a new dictionary containing the keys of this dictionary with the values transformed by the given closure.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](dictionary/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](dictionary/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](dictionary/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func compactMapValues<T>((Value) throws -> T?) rethrows -> Dictionary<Key, T>](dictionary/compactmapvalues(_:).md)
  Returns a new dictionary containing only the key-value pairs that have non-`nil` values as the result of transformation by the given closure.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](dictionary/flatmap(_:)-6chv9.md)
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](dictionary/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func shuffled() -> [Self.Element]](dictionary/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](dictionary/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/flatmap(_:)-i3ly)*