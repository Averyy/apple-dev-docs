# geoTrackingFailed

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

An error that indicates when localization imagery fails to match the device’s camera captures.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
static var geoTrackingFailed: ARError.Code { get }
```

## Discussion

ARKit will raise an error with this error code when visual localization is taking too long. This situation indicates that the app has met all requirements for geo tracking except for visual localization. To try again, the app needs to ask the user pan the device around the physical environment to acquire different camera-feed imagery. For more information, see [Assisting the User with Visual Localization](../argeotrackingstatus/state-swift.enum/localizing.md#Assisting-the-User-with-Visual-Localization).

## See Also

### Identifying an error cause
- [ARError.Code](./code.md)
  Codes that identify errors in ARKit.
- [static var requestFailed: ARError.Code](./requestfailed.md)
  An error that indicates a request fails.
- [static var cameraUnauthorized: ARError.Code](./cameraunauthorized.md)
  An error that indicates the app lacks user permission for the camera.
- [static var fileIOFailed: ARError.Code](./fileiofailed.md)
  An error that indicates a file access fails to read or write.
- [static var insufficientFeatures: ARError.Code](./insufficientfeatures.md)
  An error that indicates the framework requires more features to complete a task.
- [static var invalidCollaborationData: ARError.Code](./invalidcollaborationdata.md)
  An error that indicates the framework fails to parse collaboration data the app receives over the network.
- [static var invalidConfiguration: ARError.Code](./invalidconfiguration.md)
  An error that indicates the configuration contains ambiguous or erroneous data.
- [static var invalidReferenceImage: ARError.Code](./invalidreferenceimage.md)
  An error that indicates the framework fails to process a reference image.
- [static var invalidReferenceObject: ARError.Code](./invalidreferenceobject.md)
  An error that indicates the framework fails to process a reference object.
- [static var invalidWorldMap: ARError.Code](./invalidworldmap.md)
  An error that indicates the framework fails to process a world map.
- [static var microphoneUnauthorized: ARError.Code](./microphoneunauthorized.md)
  An error that indicates the app lacks user permission for the microphone.
- [static var objectMergeFailed: ARError.Code](./objectmergefailed.md)
  An error that indicates the framework fails to merge a detected object.
- [static var sensorFailed: ARError.Code](./sensorfailed.md)
  An error that indicates a sensor fails to provide required input.
- [static var sensorUnavailable: ARError.Code](./sensorunavailable.md)
  An error that indicates the framework fails to access a required sensor.
- [static var unsupportedConfiguration: ARError.Code](./unsupportedconfiguration.md)
  An error that indicates the device lacks support for the session’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arerror/geotrackingfailed)*