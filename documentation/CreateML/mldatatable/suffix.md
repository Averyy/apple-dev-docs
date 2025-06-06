# suffix(_:)

**Framework**: Create ML  
**Kind**: method

Creates a subset of the table given a number of final rows.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func suffix(_ maxLength: Int = 10) -> MLDataTable
```

#### Return Value

A new data table.

## Parameters

- `maxLength`: The largest number of rows to use from the end of the data   table. The default value is  .

## See Also

- [subscript(Range<Int>) -> MLDataTable](mldatatable/subscript(_:)-7h4j3.md)
  Creates a subset of the table given a range of rows.
- [subscript<R>(R) -> MLDataTable](mldatatable/subscript(_:)-5le8a.md)
  Creates a subset of the table given a range expression of rows.
- [func prefix(Int) -> MLDataTable](mldatatable/prefix(_:).md)
  Creates a subset of the table given a number of initial rows.
- [func intersect<T>(T..., of: String) -> MLDataTable](mldatatable/intersect(_:of:).md)
  Creates a subset of the table by including the rows that contain any of the given values in the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/suffix(_:))*