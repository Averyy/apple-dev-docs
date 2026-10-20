# SerializationError

**Framework**: Create ML Components  
**Kind**: enum  
**Role**: Enumeration

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
- [SerializationError.notRepresentableAsCoreML(debugDescription:)](./serializationerror/notrepresentableascoreml%28debugdescription%29.md)
  An error that indicates that the transformer cannot be represented as a CoreML model.
- [SerializationError.packageAlreadyExists(_:)](./serializationerror/packagealreadyexists%28_%29.md)
  An error that indicates that the package already exists at the URL.
- [SerializationError.packageNotFound(_:)](./serializationerror/packagenotfound%28_%29.md)
  An error that indicates that the package at specified URL was not found.
### Getting the debug description
- [var debugDescription: String](./serializationerror/debugdescription.md)
  A text representation of the error.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./serializationerror/customdebugstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Escapable](../Swift/escapable.md)
- [LocalizedError](../Foundation/localizederror.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [enum AudioPreprocessingError](./audiopreprocessingerror.md)
  Audio preprocessing errors.
- [enum AudioReaderError](./audioreadererror.md)
  Audio reader errors.
- [enum CompatibilityError](./compatibilityerror.md)
  A compatibility error.
- [enum ConcatenationError](./concatenationerror.md)
  Errors thrown when concatenating numeric values.
- [enum DatasetError](./dataseterror.md)
  Dataset processing errors.
- [enum EstimatorEncodingError](./estimatorencodingerror.md)
  An estimator encoding error.
- [enum ModelCompatibilityError](./modelcompatibilityerror.md)
  Errors related to CoreML model compatibility.
- [enum ModelUpdateError](./modelupdateerror.md)
  An updatable model error.
- [enum OptimizationError](./optimizationerror.md)
  An optimization error.
- [enum PipelineDataError](./pipelinedataerror.md)
  Errors related to pipeline data affinity problems.
- [enum TabularPipelineDataError](./tabularpipelinedataerror.md)
  Errors related to tabular pipeline data affinity problems.
- [enum VideoReaderError](./videoreadererror.md)
  Video loader errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/serializationerror)*