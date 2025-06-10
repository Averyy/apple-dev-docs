# TabularPipelineDataError

**Framework**: Create ML Components  
**Kind**: enum

Errors related to tabular pipeline data affinity problems.

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
enum TabularPipelineDataError
```

## Topics

### Getting the cases
- [case incorrectType(operation: String, columnName: String, actual: String, expected: String)](tabularpipelinedataerror/incorrecttype(operation:columnname:actual:expected:).md)
  A column has an incorrect type.
- [TabularPipelineDataError.missingColumn(operation:columnName:)](tabularpipelinedataerror/missingcolumn(operation:columnname:).md)
  A column is missing from the data frame.
- [TabularPipelineDataError.missingValues(operation:columnName:)](tabularpipelinedataerror/missingvalues(operation:columnname:).md)
  The selected column has missing values.
- [var errorDescription: String?](tabularpipelinedataerror/errordescription.md)
  A localized message describing what error occurred.
### Operators
- [static func == (TabularPipelineDataError, TabularPipelineDataError) -> Bool](tabularpipelinedataerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [CustomDebugStringConvertible Implementations](tabularpipelinedataerror/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](tabularpipelinedataerror/equatable-implementations.md)
- [Error Implementations](tabularpipelinedataerror/error-implementations.md)
- [LocalizedError Implementations](tabularpipelinedataerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum AudioPreprocessingError](audiopreprocessingerror.md)
  Audio preprocessing errors.
- [enum AudioReaderError](audioreadererror.md)
  Audio reader errors.
- [enum CompatibilityError](compatibilityerror.md)
  A compatibility error.
- [enum ConcatenationError](concatenationerror.md)
  Errors thrown when concatenating numeric values.
- [enum DatasetError](dataseterror.md)
  Dataset processing errors.
- [enum EstimatorEncodingError](estimatorencodingerror.md)
  An estimator encoding error.
- [enum ModelCompatibilityError](modelcompatibilityerror.md)
  Errors related to CoreML model compatibility.
- [enum ModelUpdateError](modelupdateerror.md)
  An updatable model error.
- [enum OptimizationError](optimizationerror.md)
  An optimization error.
- [enum PipelineDataError](pipelinedataerror.md)
  Errors related to pipeline data affinity problems.
- [enum SerializationError](serializationerror.md)
  A serialization error.
- [enum VideoReaderError](videoreadererror.md)
  Video loader errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularpipelinedataerror)*