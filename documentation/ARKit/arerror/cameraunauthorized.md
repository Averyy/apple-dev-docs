# cameraUnauthorized

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

An error that indicates the app lacks user permission for the camera.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
static var cameraUnauthorized: ARError.Code { get }
```

#### Discussion

To use the device’s camera:

- Your app’s Info.plist file must provide a message for the [NSCameraUsageDescription](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/plist/info/NSCameraUsageDescription) key. If this key is missing, any attempt to run an AR session fails with this error.
- When your app first attempts to run an AR session or otherwise use the camera, iOS automatically shows an alert with your camera usage description message, asking the user to grant camera permission to your app. If the user accepts this request, the session begins; otherwise the session fails with this error.
- If the user has previously denied camera permission for your app, all attempts to run an AR session or otherwise use the camera fail with this error. To grant camera permission, the user must explicitly enable your app in the iOS Settings app, under Privacy > Camera.

## See Also

### Identifying an error cause
- [ARError.Code](./code.md)
  Codes that identify errors in ARKit.
- [static var requestFailed: ARError.Code](./requestfailed.md)
  An error that indicates a request fails.
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
- [static var worldTrackingFailed: ARError.Code](./worldtrackingfailed.md)
  An error that indicates when world tracking experiences an unrecoverable problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arerror/cameraunauthorized)*