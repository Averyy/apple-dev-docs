# AudioPreprocessingError

**Framework**: Create ML Components  
**Kind**: enum  
**Role**: Enumeration

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
- [case incompatibleTargetFormatForConversion(inputFormat: AVAudioFormat, targetFormat: AVAudioFormat)](./audiopreprocessingerror/incompatibletargetformatforconversion%28inputformat,targetformat%29.md)
  An error that indicates that the input and output formats are incompatible for creating an audio converter.
### Getting the debug description
- [var debugDescription: String](./audiopreprocessingerror/debugdescription.md)
  A text representation of the error.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./audiopreprocessingerror/customdebugstringconvertible-implementations.md)

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
- [enum SerializationError](./serializationerror.md)
  A serialization error.
- [enum TabularPipelineDataError](./tabularpipelinedataerror.md)
  Errors related to tabular pipeline data affinity problems.
- [enum VideoReaderError](./videoreadererror.md)
  Video loader errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audiopreprocessingerror)*