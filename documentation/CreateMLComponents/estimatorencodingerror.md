# EstimatorEncodingError

**Framework**: Create ML Components  
**Kind**: enum

An estimator encoding error.

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
enum EstimatorEncodingError
```

## Topics

### Analyzing the error
- [EstimatorEncodingError.invalidState(debugDescription:)](estimatorencodingerror/invalidstate(debugdescription:).md)
  An error that indicates that an estimator cannot perform encoding from its current state.
- [var errorDescription: String?](estimatorencodingerror/errordescription.md)
  A localized message describing what error occurred.
### Operators
- [static func == (EstimatorEncodingError, EstimatorEncodingError) -> Bool](estimatorencodingerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [CustomDebugStringConvertible Implementations](estimatorencodingerror/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](estimatorencodingerror/equatable-implementations.md)
- [Error Implementations](estimatorencodingerror/error-implementations.md)
- [LocalizedError Implementations](estimatorencodingerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)

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
- [enum TabularPipelineDataError](tabularpipelinedataerror.md)
  Errors related to tabular pipeline data affinity problems.
- [enum VideoReaderError](videoreadererror.md)
  Video loader errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatorencodingerror)*