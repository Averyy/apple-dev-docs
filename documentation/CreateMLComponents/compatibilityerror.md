# CompatibilityError

**Framework**: Create ML Components  
**Kind**: enum  
**Role**: Enumeration

A compatibility error.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
enum CompatibilityError
```

## Topics

### Analyzing the Error
- [CompatibilityError.unsupportedRevision(_:)](./compatibilityerror/unsupportedrevision%28_%29.md)
  An error that indicates that the revision is not supported.
### Getting the debug description
- [var debugDescription: String](./compatibilityerror/debugdescription.md)
  A text representation of the error.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./compatibilityerror/customdebugstringconvertible-implementations.md)

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
- [enum SerializationError](./serializationerror.md)
  A serialization error.
- [enum TabularPipelineDataError](./tabularpipelinedataerror.md)
  Errors related to tabular pipeline data affinity problems.
- [enum VideoReaderError](./videoreadererror.md)
  Video loader errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/compatibilityerror)*