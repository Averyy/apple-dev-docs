# TabularPipelineDataError.missingColumn(operation:columnName:)

**Framework**: Create ML Components  
**Kind**: case  
**Role**: Case

A column is missing from the data frame.

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
case missingColumn(operation: String, columnName: String)
```

## See Also

### Getting the cases
- [case incorrectType(operation: String, columnName: String, actual: String, expected: String)](./incorrecttype%28operation,columnname,actual,expected%29.md)
  A column has an incorrect type.
- [TabularPipelineDataError.missingValues(operation:columnName:)](./missingvalues%28operation,columnname%29.md)
  The selected column has missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularpipelinedataerror/missingcolumn(operation:columnname:))*