# ConcatenationError

**Framework**: Create ML Components  
**Kind**: enum

Errors thrown when concatenating numeric values.

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
enum ConcatenationError
```

## Topics

### Analyzing the error
- [ConcatenationError.mismatchedShapes](concatenationerror/mismatchedshapes.md)
  Shaped arrays across columns have mismatched shapes and can’t be concatenated.
- [ConcatenationError.nonUniformShapes(columnName:)](concatenationerror/nonuniformshapes(columnname:).md)
  A column contains arrays or shaped arrays with non-uniform shapes.
- [var errorDescription: String?](concatenationerror/errordescription.md)
  A localized message describing what error occurred.
### Operators
- [static func == (ConcatenationError, ConcatenationError) -> Bool](concatenationerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [CustomDebugStringConvertible Implementations](concatenationerror/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](concatenationerror/equatable-implementations.md)
- [Error Implementations](concatenationerror/error-implementations.md)
- [LocalizedError Implementations](concatenationerror/localizederror-implementations.md)

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
- [enum TabularPipelineDataError](tabularpipelinedataerror.md)
  Errors related to tabular pipeline data affinity problems.
- [enum VideoReaderError](videoreadererror.md)
  Video loader errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/concatenationerror)*