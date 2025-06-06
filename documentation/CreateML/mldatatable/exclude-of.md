# exclude(_:of:)

**Framework**: Create ML  
**Kind**: method

Creates a subset of the table by excluding the rows that contain any of the given values in the given column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func exclude<T>(_ values: T..., of columnNamed: String) -> MLDataTable where T : MLDataValueConvertible
```

#### Return Value

A new data table.

## Parameters

- `values`: The values to exclude from the new table.
- `columnNamed`: The name of the column to search for excluded values.

## See Also

- [func dropMissing() -> MLDataTable](mldatatable/dropmissing.md)
  Creates a subset of the table by removing any row missing one or more values.
- [func dropDuplicates() -> MLDataTable](mldatatable/dropduplicates.md)
  Creates a subset of the table by removing all duplicate rows.
- [func randomSample(by: Double, seed: Int) -> MLDataTable](mldatatable/randomsample(by:seed:).md)
  Creates a subset of the table by randomly selecting the given proportion of rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/exclude(_:of:))*