# flatMap(_:)

**Framework**: TabularData  
**Kind**: method

Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func flatMap<SegmentOfResult>(_ transform: (Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element] where SegmentOfResult : Sequence
```

#### Return Value

The resulting flattened array.

#### Discussion

Use this method to receive a single-level collection when your transformation produces a sequence or collection for each element.

In this example, note the difference in the result of using `map` and `flatMap` with a transformation that returns an array.

```None
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

- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](anycolumnslice/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func shuffled() -> [Self.Element]](anycolumnslice/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](anycolumnslice/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](anycolumnslice/filter(_:).md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](anycolumnslice/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](anycolumnslice/flatmap(_:)-m7l1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumnslice/flatmap(_:)-5y1nc)*