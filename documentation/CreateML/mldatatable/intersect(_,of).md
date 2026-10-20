# intersect(_:of:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Creates a subset of the table by including the rows that contain any of the given values in the given column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func intersect<T>(_ values: T..., of columnNamed: String) -> MLDataTable where T : MLDataValueConvertible
```

#### Return Value

A new data table.

## Parameters

- `values`: The values to include from the new table.
- `columnNamed`: The name of the column to search for included values.

## See Also

### Selecting rows
- [subscript(Range<Int>) -> MLDataTable](./subscript%28_%29-7h4j3.md)
  Creates a subset of the table given a range of rows.
- [subscript<R>(R) -> MLDataTable](./subscript%28_%29-5le8a.md)
  Creates a subset of the table given a range expression of rows.
- [func prefix(Int) -> MLDataTable](./prefix%28_%29.md)
  Creates a subset of the table given a number of initial rows.
- [func suffix(Int) -> MLDataTable](./suffix%28_%29.md)
  Creates a subset of the table given a number of final rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/intersect(_:of:))*