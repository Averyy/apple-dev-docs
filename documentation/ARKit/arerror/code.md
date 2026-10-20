# ARError.Code

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Codes that identify errors in ARKit.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
enum Code
```

```c
enum ARErrorCode : NSInteger;
```

## Topics

### Errors
- [ARError.Code.requestFailed](./code/requestfailed.md)
  An error that indicates a request fails.
- [ARError.Code.cameraUnauthorized](./code/cameraunauthorized.md)
  An error that indicates the app lacks user permission for the camera.
- [ARError.Code.fileIOFailed](./code/fileiofailed.md)
  An error that indicates a file access fails to read or write.
- [ARError.Code.insufficientFeatures](./code/insufficientfeatures.md)
  An error that indicates the framework requires more features to complete a task.
- [ARError.Code.invalidCollaborationData](./code/invalidcollaborationdata.md)
  An error that indicates the framework fails to parse collaboration data the app receives over the network.
- [ARError.Code.invalidConfiguration](./code/invalidconfiguration.md)
  An error that indicates the configuration contains ambiguous or erroneous data.
- [ARError.Code.invalidReferenceImage](./code/invalidreferenceimage.md)
  An error that indicates the framework fails to process a reference image.
- [ARError.Code.invalidReferenceObject](./code/invalidreferenceobject.md)
  An error that indicates the framework fails to process a reference object.
- [ARError.Code.invalidWorldMap](./code/invalidworldmap.md)
  An error that indicates the framework fails to process a world map.
- [ARError.Code.microphoneUnauthorized](./code/microphoneunauthorized.md)
  An error that indicates the app lacks user permission for the microphone.
- [ARError.Code.objectMergeFailed](./code/objectmergefailed.md)
  An error that indicates the framework fails to merge a detected object.
- [ARError.Code.sensorFailed](./code/sensorfailed.md)
  An error that indicates a sensor fails to provide required input.
- [ARError.Code.sensorUnavailable](./code/sensorunavailable.md)
  An error that indicates the framework fails to access a required sensor.
- [ARError.Code.unsupportedConfiguration](./code/unsupportedconfiguration.md)
  An error that indicates the device lacks support for the session’s configuration.
- [ARError.Code.worldTrackingFailed](./code/worldtrackingfailed.md)
  An error that indicates when world tracking experiences an unrecoverable problem.
- [ARError.Code.geoTrackingFailed](./code/geotrackingfailed.md)
  An error that indicates when localization imagery fails to match the device’s camera captures.
- [ARError.Code.geoTrackingNotAvailableAtLocation](./code/geotrackingnotavailableatlocation.md)
  An error that indicates a location lacks geotracking support.
- [ARError.Code.locationUnauthorized](./code/locationunauthorized.md)
  An error that indicates the app lacks user permission for the device’s current location.
- [ARError.Code.highResolutionFrameCaptureFailed](./code/highresolutionframecapturefailed.md)
  An error that indicates a problem in the system’s capture pipeline.
- [ARError.Code.highResolutionFrameCaptureInProgress](./code/highresolutionframecaptureinprogress.md)
  An error that indicates the system needs to finish a high-resolution frame request before accepting another request.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct ARError](../arerror.md)
  An error reported by ARKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arerror/code)*