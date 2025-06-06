# dropMissing()

**Framework**: Create ML  
**Kind**: method

Creates a subset of the table by removing any row missing one or more values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func dropMissing() -> MLDataTable
```

#### Return Value

A new data table.

## See Also

- [func dropDuplicates() -> MLDataTable](mldatatable/dropduplicates.md)
  Creates a subset of the table by removing all duplicate rows.
- [func exclude<T>(T..., of: String) -> MLDataTable](mldatatable/exclude(_:of:).md)
  Creates a subset of the table by excluding the rows that contain any of the given values in the given column.
- [func randomSample(by: Double, seed: Int) -> MLDataTable](mldatatable/randomsample(by:seed:).md)
  Creates a subset of the table by randomly selecting the given proportion of rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/dropmissing())*