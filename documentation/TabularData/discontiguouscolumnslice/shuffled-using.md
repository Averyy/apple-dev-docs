# shuffled(using:)

**Framework**: TabularData  
**Kind**: method

Returns the elements of the sequence, shuffled using the given generator as a source for randomness.

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
func shuffled<T>(using generator: inout T) -> [Self.Element] where T : RandomNumberGenerator
```

#### Return Value

An array of this sequence’s elements in a shuffled order.

#### Discussion

You use this method to randomize the elements of a sequence when you are using a custom random number generator. For example, you can shuffle the numbers between `0` and `9` by calling the `shuffled(using:)` method on that range:

```None
let numbers = 0...9
let shuffledNumbers = numbers.shuffled(using: &myGenerator)
// shuffledNumbers == [8, 9, 4, 3, 2, 6, 7, 0, 5, 1]
```

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

> **Note**: The algorithm used to shuffle a sequence may change in a future version of Swift. If you’re passing a generator that results in the same shuffled order each time you run your program, that sequence may change when your program is compiled using a different version of Swift.

The algorithm used to shuffle a sequence may change in a future version of Swift. If you’re passing a generator that results in the same shuffled order each time you run your program, that sequence may change when your program is compiled using a different version of Swift.

## Parameters

- `generator`: The random number generator to use when shuffling   the sequence.

## See Also

- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](discontiguouscolumnslice/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func shuffled() -> [Self.Element]](discontiguouscolumnslice/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func filter((DiscontiguousColumnSlice<WrappedElement>.Element) throws -> Bool) rethrows -> DiscontiguousColumnSlice<WrappedElement>](discontiguouscolumnslice/filter(_:).md)
  Generates a slice that contains the elements that satisfy the predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](discontiguouscolumnslice/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](discontiguouscolumnslice/flatmap(_:)-85suh.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](discontiguouscolumnslice/flatmap(_:)-5uq62.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/shuffled(using:))*