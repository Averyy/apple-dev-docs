# compactMap(_:)

**Framework**: TabularData  
**Kind**: method

Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.

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
func compactMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```

#### Return Value

An array of the non-`nil` results of calling `transform` with each element of the sequence.

#### Discussion

Use this method to receive an array of non-optional values when your transformation produces an optional value.

In this example, note the difference in the result of using `map` and `compactMap` with a transformation that returns an optional `Int` value.

```None
let possibleNumbers = ["1", "2", "three", "///4///", "5"]

let mapped: [Int?] = possibleNumbers.map { str in Int(str) }
// [1, 2, nil, nil, 5]

let compactMapped: [Int] = possibleNumbers.compactMap { str in Int(str) }
// [1, 2, 5]
```

> **Note**: O(), where  is the length of this sequence.

## Parameters

- `transform`: A closure that accepts an element of this   sequence as its argument and returns an optional value.

## See Also

- [func sorted() -> [Self.Element]](filledcolumn/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](filledcolumn/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func shuffled() -> [Self.Element]](filledcolumn/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](filledcolumn/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](filledcolumn/filter(_:).md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](filledcolumn/flatmap(_:)-28fxz.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](filledcolumn/flatmap(_:)-4cljy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/compactmap(_:))*