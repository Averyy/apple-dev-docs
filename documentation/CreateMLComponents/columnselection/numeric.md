# ColumnSelection.numeric

**Framework**: Create ML Components  
**Kind**: case

Select all numeric columns in the data frame.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
case numeric
```

#### Discussion

Numeric columns are columns with elements of type `Int`, `UInt8`, `Float`, `Double`. Also arrays of those types and shaped arrays of those types.

## See Also

- [ColumnSelection.all](columnselection/all.md)
  Select all columns in the data frame.
- [ColumnSelection.exclude(columnNames:)](columnselection/exclude(columnnames:).md)
  Selects all columns except the specified columns.
- [ColumnSelection.include(columnNames:)](columnselection/include(columnnames:).md)
  Selects only the specified columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnselection/numeric)*