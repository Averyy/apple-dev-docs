# VideoReaderError

**Framework**: Create ML Components  
**Kind**: enum

Video loader errors.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum VideoReaderError
```

## Topics

### Analyzing the error
- [VideoReaderError.cameraAuthorizationDenied](videoreadererror/cameraauthorizationdenied.md)
  An error that indicates that the camera authorization status is denied. The user has explicitly denied permission for media capture.
- [VideoReaderError.cameraAuthorizationRestricted](videoreadererror/cameraauthorizationrestricted.md)
  An error that indicates that the camera authorization status is restricted. The user is not allowed to access media capture devices.
- [VideoReaderError.frameRateNotSupported(_:)](videoreadererror/frameratenotsupported(_:).md)
  An error that indicates that the frame rate is not supported by the input camera.
- [VideoReaderError.missingVideoTrack(_:)](videoreadererror/missingvideotrack(_:).md)
  An error that indicates that the VideoReader cannot find a video track.
- [VideoReaderError.sourceCameraNotAvailable](videoreadererror/sourcecameranotavailable.md)
  An error that indicates that no cameras are available.
- [var errorDescription: String?](videoreadererror/errordescription.md)
  A localized message describing what error occurred.
### Operators
- [static func == (VideoReaderError, VideoReaderError) -> Bool](videoreadererror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [VideoReaderError.captureSessionStopped](videoreadererror/capturesessionstopped.md)
  An error that indicates that the capture session stopped.
### Default Implementations
- [CustomDebugStringConvertible Implementations](videoreadererror/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](videoreadererror/equatable-implementations.md)
- [Error Implementations](videoreadererror/error-implementations.md)
- [LocalizedError Implementations](videoreadererror/localizederror-implementations.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreadererror)*