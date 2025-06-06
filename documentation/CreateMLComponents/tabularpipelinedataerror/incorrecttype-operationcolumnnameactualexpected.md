# TabularPipelineDataError.incorrectType(operation:columnName:actual:expected:)

**Framework**: Create ML Components  
**Kind**: case

A column has an incorrect type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
case incorrectType(operation: String, columnName: String, actual: String, expected: String)
```

## See Also

- [TabularPipelineDataError.missingColumn(operation:columnName:)](tabularpipelinedataerror/missingcolumn(operation:columnname:).md)
  A column is missing from the data frame.
- [TabularPipelineDataError.missingValues(operation:columnName:)](tabularpipelinedataerror/missingvalues(operation:columnname:).md)
  The selected column has missing values.
- [var errorDescription: String?](tabularpipelinedataerror/errordescription.md)
  A localized message describing what error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularpipelinedataerror/incorrecttype(operation:columnname:actual:expected:))*