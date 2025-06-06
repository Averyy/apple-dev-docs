# TabularPipelineDataError.missingValues(operation:columnName:)

**Framework**: Create ML Components  
**Kind**: case

The selected column has missing values.

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
case missingValues(operation: String, columnName: String)
```

## See Also

- [case incorrectType(operation: String, columnName: String, actual: String, expected: String)](tabularpipelinedataerror/incorrecttype(operation:columnname:actual:expected:).md)
  A column has an incorrect type.
- [TabularPipelineDataError.missingColumn(operation:columnName:)](tabularpipelinedataerror/missingcolumn(operation:columnname:).md)
  A column is missing from the data frame.
- [var errorDescription: String?](tabularpipelinedataerror/errordescription.md)
  A localized message describing what error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularpipelinedataerror/missingvalues(operation:columnname:))*