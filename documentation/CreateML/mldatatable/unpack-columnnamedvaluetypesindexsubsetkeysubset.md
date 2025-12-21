# unpack(columnNamed:valueTypes:indexSubset:keySubset:)

**Framework**: Create ML  
**Kind**: method

Creates a new data table with additional columns that contain the unpacked collections in the given column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func unpack(columnNamed: String, valueTypes: [MLDataValue.ValueType]? = nil, indexSubset: [Int]? = nil, keySubset: [String]? = nil) -> MLDataTable
```

#### Return Value

A new data table.

#### Discussion

This function performs the inverse of [`pack(columnsNamed:to:type:filling:)`](mldatatable/pack(columnsnamed:to:type:filling:).md).

## Parameters

- `columnNamed`: The name of the column to unpack. The underlying type of   the column must be either   or  .
- `valueTypes`: An array of the underlying types for the new, unpacked   columns. If  , the method infers the underlying types in the   sequence or dictionary.
- `indexSubset`: The subset of indicies to unpack from a specified   sequence-typed column. If  , the method unpacks all indicies.
- `keySubset`: The subset of keys to unpack from a specified   dictionary-typed column. If  , the method unpacks all keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/unpack(columnnamed:valuetypes:indexsubset:keysubset:))*