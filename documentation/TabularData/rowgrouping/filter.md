# filter(_:)

**Framework**: TabularData  
**Kind**: method

Returns a row grouping containing only the groups that satisfy a predicate.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
func filter(_ isIncluded: (DataFrame.Slice) throws -> Bool) rethrows -> RowGrouping<GroupingKey>
```

#### Return Value

A data frame slice that contains the rows that satisfy the predicate.

## Parameters

- `isIncluded`: A predicate closure that takes a group and returns a Boolean that indicates whether   the group is included.

## See Also

- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](rowgrouping/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func shuffled() -> [Self.Element]](rowgrouping/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](rowgrouping/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](rowgrouping/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](rowgrouping/flatmap(_:)-4fkva.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](rowgrouping/flatmap(_:)-2ovll.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/filter(_:))*