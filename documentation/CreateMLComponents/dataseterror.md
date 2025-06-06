# DatasetError

**Framework**: Create ML Components  
**Kind**: enum

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
- [case incompatibleDataFormat(URL, debugDescription: String)](dataseterror/incompatibledataformat(_:debugdescription:).md)
  An error that indicates that a resource doesn’t have the expected data format.
- [case incorrectName(URL, debugDescription: String)](dataseterror/incorrectname(_:debugdescription:).md)
  An error that indicates that a resource has incorrect name format.
- [DatasetError.missingResource(_:)](dataseterror/missingresource(_:).md)
  An error that indicates that a resource is missing.
- [DatasetError.unreadableResource(_:)](dataseterror/unreadableresource(_:).md)
  An error that indicates that a resource is unreadable.
- [var errorDescription: String?](dataseterror/errordescription.md)
  A localized message describing what error occurred.
### Operators
- [static func == (DatasetError, DatasetError) -> Bool](dataseterror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [CustomDebugStringConvertible Implementations](dataseterror/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](dataseterror/equatable-implementations.md)
- [Error Implementations](dataseterror/error-implementations.md)
- [LocalizedError Implementations](dataseterror/localizederror-implementations.md)

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
- [enum TabularPipelineDataError](tabularpipelinedataerror.md)
  Errors related to tabular pipeline data affinity problems.
- [enum VideoReaderError](videoreadererror.md)
  Video loader errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/dataseterror)*