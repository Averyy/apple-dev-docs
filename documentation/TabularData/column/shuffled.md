# shuffled()

**Framework**: TabularData  
**Kind**: method

Returns the elements of the sequence, shuffled.

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
func shuffled() -> [Self.Element]
```

#### Return Value

A shuffled array of this sequence’s elements.

#### Discussion

For example, you can shuffle the numbers between `0` and `9` by calling the `shuffled()` method on that range:

```None
let numbers = 0...9
let shuffledNumbers = numbers.shuffled()
// shuffledNumbers == [1, 7, 6, 2, 8, 9, 4, 3, 5, 0]
```

This method is equivalent to calling `shuffled(using:)`, passing in the system’s default random generator.

> **Note**: O(), where  is the length of the sequence.

## See Also

- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](column/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func shuffled<T>(using: inout T) -> [Self.Element]](column/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func filter((Column<WrappedElement>.Element) throws -> Bool) rethrows -> DiscontiguousColumnSlice<WrappedElement>](column/filter(_:).md)
  Generates a slice that contains the elements that satisfy a predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](column/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](column/flatmap(_:)-9y1gq.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](column/flatmap(_:)-6c3wd.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/shuffled())*