# pack(columnsNamed:to:type:filling:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Creates a new data table with an additional column that contains the combined values of the given columns.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func pack(columnsNamed: String..., to: String, type: MLDataTable.PackType = .sequence, filling: MLDataValue = MLDataValue.invalid) -> MLDataTable
```

#### Return Value

A new data table.

#### Discussion

This function performs the inverse of [`unpack(columnNamed:valueTypes:indexSubset:keySubset:)`](./unpack%28columnnamed,valuetypes,indexsubset,keysubset%29.md).

## Parameters

- `columnsNamed`: The name of the columns to compact.
- `to`: The name of the new condensed column.
- `type`: The collection type for the new column. Typically, the type is a sequence or a dictionary.
- `filling`: The value to fill in any missing values with.

## See Also

### Compacting columns
- [MLDataTable.PackType](./packtype.md)
  The storage operations for combining multiple columns into one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/pack(columnsnamed:to:type:filling:))*