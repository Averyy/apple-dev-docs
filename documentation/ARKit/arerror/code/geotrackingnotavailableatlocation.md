# ARError.Code.geoTrackingNotAvailableAtLocation

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

An error that indicates a location lacks geotracking support.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
case geoTrackingNotAvailableAtLocation
```

```c
ARErrorCodeGeoTrackingNotAvailableAtLocation
```

#### Discussion

This error code indicates that ARKit does not have the necessary localization imagery to support geo tracking at the user’s current location. See [`checkAvailability(completionHandler:)`](../../argeotrackingconfiguration/checkavailability%28completionhandler%29.md) for more information.

If [`checkAvailability(completionHandler:)`](../../argeotrackingconfiguration/checkavailability%28completionhandler%29.md) returns [`true`](../../../Swift/true.md) and an app begins geo-tracking session, ARKit provides this state reason when the user has moved to an unsupported area.

## See Also

### Errors
- [ARError.Code.requestFailed](./requestfailed.md)
  An error that indicates a request fails.
- [ARError.Code.cameraUnauthorized](./cameraunauthorized.md)
  An error that indicates the app lacks user permission for the camera.
- [ARError.Code.fileIOFailed](./fileiofailed.md)
  An error that indicates a file access fails to read or write.
- [ARError.Code.insufficientFeatures](./insufficientfeatures.md)
  An error that indicates the framework requires more features to complete a task.
- [ARError.Code.invalidCollaborationData](./invalidcollaborationdata.md)
  An error that indicates the framework fails to parse collaboration data the app receives over the network.
- [ARError.Code.invalidConfiguration](./invalidconfiguration.md)
  An error that indicates the configuration contains ambiguous or erroneous data.
- [ARError.Code.invalidReferenceImage](./invalidreferenceimage.md)
  An error that indicates the framework fails to process a reference image.
- [ARError.Code.invalidReferenceObject](./invalidreferenceobject.md)
  An error that indicates the framework fails to process a reference object.
- [ARError.Code.invalidWorldMap](./invalidworldmap.md)
  An error that indicates the framework fails to process a world map.
- [ARError.Code.microphoneUnauthorized](./microphoneunauthorized.md)
  An error that indicates the app lacks user permission for the microphone.
- [ARError.Code.objectMergeFailed](./objectmergefailed.md)
  An error that indicates the framework fails to merge a detected object.
- [ARError.Code.sensorFailed](./sensorfailed.md)
  An error that indicates a sensor fails to provide required input.
- [ARError.Code.sensorUnavailable](./sensorunavailable.md)
  An error that indicates the framework fails to access a required sensor.
- [ARError.Code.unsupportedConfiguration](./unsupportedconfiguration.md)
  An error that indicates the device lacks support for the session’s configuration.
- [ARError.Code.worldTrackingFailed](./worldtrackingfailed.md)
  An error that indicates when world tracking experiences an unrecoverable problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arerror/code/geotrackingnotavailableatlocation)*