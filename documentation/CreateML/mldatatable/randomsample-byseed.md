# randomSample(by:seed:)

**Framework**: Create ML  
**Kind**: method

Creates a subset of the table by randomly selecting the given proportion of rows.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func randomSample(by proportion: Double, seed: Int = 42) -> MLDataTable
```

#### Return Value

A new data table.

## Parameters

- `proportion`: The fraction of rows to sample from the original table.   The value must be in the range  .
- `seed`: A number that seeds a random number generator.

## See Also

- [func dropMissing() -> MLDataTable](mldatatable/dropmissing.md)
  Creates a subset of the table by removing any row missing one or more values.
- [func dropDuplicates() -> MLDataTable](mldatatable/dropduplicates.md)
  Creates a subset of the table by removing all duplicate rows.
- [func exclude<T>(T..., of: String) -> MLDataTable](mldatatable/exclude(_:of:).md)
  Creates a subset of the table by excluding the rows that contain any of the given values in the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/randomsample(by:seed:))*