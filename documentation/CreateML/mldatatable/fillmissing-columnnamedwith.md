# fillMissing(columnNamed:with:)

**Framework**: Create ML  
**Kind**: method

Creates a modified copy of the table by filling in the missing values in the named column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func fillMissing(columnNamed: String, with value: MLDataValue) -> MLDataTable
```

#### Return Value

A new data table.

## Parameters

- `columnNamed`: The name of the column with missing values.
- `value`: An   to put in place for every missing value in the column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/fillmissing(columnnamed:with:))*