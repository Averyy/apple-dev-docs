# flatMap(_:)

**Framework**: Create ML  
**Kind**: method

Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

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

## Parameters

- `transform`: A closure that accepts an element of this   sequence as its argument and returns a sequence or collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/flatmap(_:)-5mw7j)*