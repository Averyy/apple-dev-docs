# ModelUpdateError

**Framework**: Create ML Components  
**Kind**: enum

An updatable model error.

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
enum ModelUpdateError
```

## Topics

### Analyzing the error
- [ModelUpdateError.invalidState(debugDescription:)](modelupdateerror/invalidstate(debugdescription:).md)
  An error that indicates that a default initialized transformer suitable for fitting cannot perform apply before performing an update.
- [var errorDescription: String?](modelupdateerror/errordescription.md)
  A localized message describing what error occurred.
### Operators
- [static func == (ModelUpdateError, ModelUpdateError) -> Bool](modelupdateerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [CustomDebugStringConvertible Implementations](modelupdateerror/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](modelupdateerror/equatable-implementations.md)
- [Error Implementations](modelupdateerror/error-implementations.md)
- [LocalizedError Implementations](modelupdateerror/localizederror-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/modelupdateerror)*