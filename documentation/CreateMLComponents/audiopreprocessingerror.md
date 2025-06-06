# AudioPreprocessingError

**Framework**: Create ML Components  
**Kind**: enum

Audio preprocessing errors.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum AudioPreprocessingError
```

## Topics

### Analyzing the error
- [case incompatibleTargetFormatForConversion(inputFormat: AVAudioFormat, targetFormat: AVAudioFormat)](audiopreprocessingerror/incompatibletargetformatforconversion(inputformat:targetformat:).md)
  An error that indicates that the input and output formats are incompatible for creating an audio converter.
- [var errorDescription: String?](audiopreprocessingerror/errordescription.md)
  A localized message describing what error occurred.
### Operators
- [static func == (AudioPreprocessingError, AudioPreprocessingError) -> Bool](audiopreprocessingerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [CustomDebugStringConvertible Implementations](audiopreprocessingerror/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](audiopreprocessingerror/equatable-implementations.md)
- [Error Implementations](audiopreprocessingerror/error-implementations.md)
- [LocalizedError Implementations](audiopreprocessingerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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
- [enum SerializationError](serializationerror.md)
  A serialization error.
- [enum TabularPipelineDataError](tabularpipelinedataerror.md)
  Errors related to tabular pipeline data affinity problems.
- [enum VideoReaderError](videoreadererror.md)
  Video loader errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audiopreprocessingerror)*