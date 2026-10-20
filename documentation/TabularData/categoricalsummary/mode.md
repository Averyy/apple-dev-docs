# mode

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

The most common values in a column, ignoring missing elements.

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
var mode: [Element]
```

#### Discussion

The summary orders the elements based on their original locations within the column.

## See Also

### Inspecting a Summary
- [var debugDescription: String](./debugdescription.md)
  A text representation of the summary’s statistics suitable for debugging.
- [var uniqueCount: Int](./uniquecount.md)
  The number of elements with distinct values in a column that excludes missing elements.
- [var someCount: Int](./somecount.md)
  The number of non-missing elements in the column.
- [var noneCount: Int](./nonecount.md)
  The number of missing elements in the column.
- [var totalCount: Int](./totalcount.md)
  The total number of elements in the column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/categoricalsummary/mode)*