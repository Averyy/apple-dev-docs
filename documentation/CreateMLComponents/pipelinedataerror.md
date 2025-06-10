# PipelineDataError

**Framework**: Create ML Components  
**Kind**: enum

Errors related to pipeline data affinity problems.

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
enum PipelineDataError
```

## Topics

### Analyzing the error
- [PipelineDataError.emptyInput(operation:)](pipelinedataerror/emptyinput(operation:).md)
  An error that indicates that the input to fit is empty.
- [case incompatibleConfiguration(operation: String, debugDescription: String)](pipelinedataerror/incompatibleconfiguration(operation:debugdescription:).md)
  An error that indicates that an input is not compatible with an operation’s configuration.
- [case incompatibleDataFormat(operation: String, debugDescription: String)](pipelinedataerror/incompatibledataformat(operation:debugdescription:).md)
  An error that indicates that an input doesn’t have the expected data format.
- [PipelineDataError.incompatibleShape(_:debugDescription:)](pipelinedataerror/incompatibleshape(_:debugdescription:).md)
  An error that indicates that an input’s doesn’t have the expected shape for the operation.
- [PipelineDataError.missingAnnotation(operation:)](pipelinedataerror/missingannotation(operation:).md)
  An error that indicates that an expected annotation is missing.
- [PipelineDataError.missingValue(operation:)](pipelinedataerror/missingvalue(operation:).md)
  An error that indicates that an expected value is missing.
- [case unrecognizedCategory(operation: String, category: String)](pipelinedataerror/unrecognizedcategory(operation:category:).md)
  An error that indicates that a new category was encountered after fitting.
- [var errorDescription: String?](pipelinedataerror/errordescription.md)
  A localized message describing what error occurred.
### Operators
- [static func == (PipelineDataError, PipelineDataError) -> Bool](pipelinedataerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [CustomDebugStringConvertible Implementations](pipelinedataerror/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](pipelinedataerror/equatable-implementations.md)
- [Error Implementations](pipelinedataerror/error-implementations.md)
- [LocalizedError Implementations](pipelinedataerror/localizederror-implementations.md)

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
- [enum SerializationError](serializationerror.md)
  A serialization error.
- [enum TabularPipelineDataError](tabularpipelinedataerror.md)
  Errors related to tabular pipeline data affinity problems.
- [enum VideoReaderError](videoreadererror.md)
  Video loader errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/pipelinedataerror)*