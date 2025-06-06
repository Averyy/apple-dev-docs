# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript

Creates a subset of the table given a range expression of rows.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript<R>(slice: R) -> MLDataTable where R : RangeExpression, R.Bound == Int { get }
```

#### Return Value

A new data table.

## Parameters

- `slice`: An interger range expression indicating which rows to include in the new data table.

## See Also

- [subscript(Range<Int>) -> MLDataTable](mldatatable/subscript(_:)-7h4j3.md)
  Creates a subset of the table given a range of rows.
- [func prefix(Int) -> MLDataTable](mldatatable/prefix(_:).md)
  Creates a subset of the table given a number of initial rows.
- [func suffix(Int) -> MLDataTable](mldatatable/suffix(_:).md)
  Creates a subset of the table given a number of final rows.
- [func intersect<T>(T..., of: String) -> MLDataTable](mldatatable/intersect(_:of:).md)
  Creates a subset of the table by including the rows that contain any of the given values in the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/subscript(_:)-5le8a)*