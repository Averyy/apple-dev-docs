# expand(columnNamed:to:)

**Framework**: Create ML  
**Kind**: method

Creates a new data table where duplicate row values in the given column are condensed into a new sequence-type column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func expand(columnNamed: String, to: String) -> MLDataTable
```

#### Return Value

A new data table.

#### Discussion

This function performs the inverse of [`condense(columnNamed:to:)`](mldatatable/condense(columnnamed:to:).md).

## Parameters

- `columnNamed`: The name of the column to expand.
- `to`: The name of the new expanded column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/expand(columnnamed:to:))*