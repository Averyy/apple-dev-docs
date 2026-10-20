# AudioReaderError

**Framework**: Create ML Components  
**Kind**: enum  
**Role**: Enumeration

Audio reader errors.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum AudioReaderError
```

## Topics

### Analyzing the error
- [AudioReaderError.microphoneAuthorizationDenied](./audioreadererror/microphoneauthorizationdenied.md)
  An error that indicates that the microphone authorization status is denied. The user has explicitly denied permission for audio capture.
- [AudioReaderError.microphoneAuthorizationRestricted](./audioreadererror/microphoneauthorizationrestricted.md)
  An error that indicates that the microphone authorization status is restricted. The user is not allowed to access audio capture devices.
- [AudioReaderError.sourceDeviceNotAvailable](./audioreadererror/sourcedevicenotavailable.md)
  An error that indicates that no source devices are available.
### Getting the debug description
- [var debugDescription: String](./audioreadererror/debugdescription.md)
  A text representation of the error.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./audioreadererror/customdebugstringconvertible-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreadererror)*