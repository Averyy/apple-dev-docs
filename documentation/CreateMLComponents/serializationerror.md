# SerializationError

**Framework**: Create ML Components  
**Kind**: enum

A serialization error.

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
enum SerializationError
```

## Topics

### Analyzing the error
- [SerializationError.notRepresentableAsCoreML(debugDescription:)](serializationerror/notrepresentableascoreml(debugdescription:).md)
  An error that indicates that the transformer cannot be represented as a CoreML model.
- [SerializationError.packageAlreadyExists(_:)](serializationerror/packagealreadyexists(_:).md)
  An error that indicates that the package already exists at the URL.
- [SerializationError.packageNotFound(_:)](serializationerror/packagenotfound(_:).md)
  An error that indicates that the package at specified URL was not found.
- [var errorDescription: String?](serializationerror/errordescription.md)
  A localized message describing what error occurred.
### Operators
- [static func == (SerializationError, SerializationError) -> Bool](serializationerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [CustomDebugStringConvertible Implementations](serializationerror/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](serializationerror/equatable-implementations.md)
- [Error Implementations](serializationerror/error-implementations.md)
- [LocalizedError Implementations](serializationerror/localizederror-implementations.md)

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
- [enum TabularPipelineDataError](tabularpipelinedataerror.md)
  Errors related to tabular pipeline data affinity problems.
- [enum VideoReaderError](videoreadererror.md)
  Video loader errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/serializationerror)*