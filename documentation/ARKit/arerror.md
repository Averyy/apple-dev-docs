# ARError

**Framework**: ARKit  
**Kind**: struct

An error reported by ARKit.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct ARError
```

## Topics

### Inspecting error information
- [static var errorDomain: String](arerror/errordomain.md)
### Identifying an error cause
- [ARError.Code](arerror/code.md)
  Codes that identify errors in ARKit.
- [static var requestFailed: ARError.Code](arerror/requestfailed.md)
  An error that indicates a request fails.
- [static var cameraUnauthorized: ARError.Code](arerror/cameraunauthorized.md)
  An error that indicates the app lacks user permission for the camera.
- [static var fileIOFailed: ARError.Code](arerror/fileiofailed.md)
  An error that indicates a file access fails to read or write.
- [static var insufficientFeatures: ARError.Code](arerror/insufficientfeatures.md)
  An error that indicates the framework requires more features to complete a task.
- [static var invalidCollaborationData: ARError.Code](arerror/invalidcollaborationdata.md)
  An error that indicates the framework fails to parse collaboration data the app receives over the network.
- [static var invalidConfiguration: ARError.Code](arerror/invalidconfiguration.md)
  An error that indicates the configuration contains ambiguous or erroneous data.
- [static var invalidReferenceImage: ARError.Code](arerror/invalidreferenceimage.md)
  An error that indicates the framework fails to process a reference image.
- [static var invalidReferenceObject: ARError.Code](arerror/invalidreferenceobject.md)
  An error that indicates the framework fails to process a reference object.
- [static var invalidWorldMap: ARError.Code](arerror/invalidworldmap.md)
  An error that indicates the framework fails to process a world map.
- [static var microphoneUnauthorized: ARError.Code](arerror/microphoneunauthorized.md)
  An error that indicates the app lacks user permission for the microphone.
- [static var objectMergeFailed: ARError.Code](arerror/objectmergefailed.md)
  An error that indicates the framework fails to merge a detected object.
- [static var sensorFailed: ARError.Code](arerror/sensorfailed.md)
  An error that indicates a sensor fails to provide required input.
- [static var sensorUnavailable: ARError.Code](arerror/sensorunavailable.md)
  An error that indicates the framework fails to access a required sensor.
- [static var unsupportedConfiguration: ARError.Code](arerror/unsupportedconfiguration.md)
  An error that indicates the device lacks support for the session’s configuration.
- [static var worldTrackingFailed: ARError.Code](arerror/worldtrackingfailed.md)
  An error that indicates when world tracking experiences an unrecoverable problem.
- [static var geoTrackingFailed: ARError.Code](arerror/geotrackingfailed.md)
  An error that indicates when localization imagery fails to match the device’s camera captures.
- [static var geoTrackingNotAvailableAtLocation: ARError.Code](arerror/geotrackingnotavailableatlocation.md)
  An error that indicates a location lacks geotracking support.
- [static var locationUnauthorized: ARError.Code](arerror/locationunauthorized.md)
  An error that indicates the app lacks user permission for the device’s current location.
- [static var highResolutionFrameCaptureFailed: ARError.Code](arerror/highresolutionframecapturefailed.md)
  An error that indicates a problem in the system’s capture pipeline.
- [static var highResolutionFrameCaptureInProgress: ARError.Code](arerror/highresolutionframecaptureinprogress.md)
  An error that indicates the system needs to finish a high-resolution frame request before accepting another request.
### Type Properties
- [static var networkConnectionFailure: ARError.Code](arerror/networkconnectionfailure.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ARError.Code](arerror/code.md)
  Codes that identify errors in ARKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arerror)*