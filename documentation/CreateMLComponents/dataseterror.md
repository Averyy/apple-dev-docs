# DatasetError

**Framework**: Create ML Components  
**Kind**: enum  
**Role**: Enumeration

Dataset processing errors.

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
enum DatasetError
```

## Topics

### Analyzing the error
- [case incompatibleDataFormat(URL, debugDescription: String)](./dataseterror/incompatibledataformat%28_,debugdescription%29.md)
  An error that indicates that a resource doesn’t have the expected data format.
- [case incorrectName(URL, debugDescription: String)](./dataseterror/incorrectname%28_,debugdescription%29.md)
  An error that indicates that a resource has incorrect name format.
- [DatasetError.missingResource(_:)](./dataseterror/missingresource%28_%29.md)
  An error that indicates that a resource is missing.
- [DatasetError.unreadableResource(_:)](./dataseterror/unreadableresource%28_%29.md)
  An error that indicates that a resource is unreadable.
### Getting the debug description
- [var debugDescription: String](./dataseterror/debugdescription.md)
  A text representation of the error.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./dataseterror/customdebugstringconvertible-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/dataseterror)*