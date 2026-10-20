# OptimizationError

**Framework**: Create ML Components  
**Kind**: enum  
**Role**: Enumeration

An optimization error.

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
enum OptimizationError
```

## Topics

### Analyzing the error
- [OptimizationError.numericOverflow](./optimizationerror/numericoverflow.md)
  Numerical overflow. Step size parameter may be too large.
- [OptimizationError.numericUnderflow](./optimizationerror/numericunderflow.md)
  Numerical underflow (not enough progress).
- [OptimizationError.unsupportedPlatform](./optimizationerror/unsupportedplatform.md)
  The optimization operation is not supported on this platform.
### Getting the debug description
- [var debugDescription: String](./optimizationerror/debugdescription.md)
  A text representation of the error.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./optimizationerror/customdebugstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
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
- [enum PipelineDataError](./pipelinedataerror.md)
  Errors related to pipeline data affinity problems.
- [enum SerializationError](./serializationerror.md)
  A serialization error.
- [enum TabularPipelineDataError](./tabularpipelinedataerror.md)
  Errors related to tabular pipeline data affinity problems.
- [enum VideoReaderError](./videoreadererror.md)
  Video loader errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/optimizationerror)*