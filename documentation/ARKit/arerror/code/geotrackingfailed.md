# ARError.Code.geoTrackingFailed

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

An error that indicates when localization imagery fails to match the device’s camera captures.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
case geoTrackingFailed
```

```c
ARErrorCodeGeoTrackingFailed
```

## Discussion

ARKit will raise an error with this error code when visual localization is taking too long. This situation indicates that the app has met all requirements for geo tracking except for visual localization. To try again, the app needs to ask the user pan the device around the physical environment to acquire different camera-feed imagery. For more information, see [Assisting the User with Visual Localization](../../argeotrackingstatus/state-swift.enum/localizing.md#Assisting-the-User-with-Visual-Localization).

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

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arerror/code/geotrackingfailed)*