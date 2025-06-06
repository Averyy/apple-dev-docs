# ARError.Code.cameraUnauthorized

**Framework**: ARKit  
**Kind**: case

An error that indicates the app lacks user permission for the camera.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case cameraUnauthorized
```

#### Discussion

To use the device’s camera:

- Your app’s Info.plist file must provide a message for the [`NSCameraUsageDescription`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/plist/info/NSCameraUsageDescription) key. If this key is missing, any attempt to run an AR session fails with this error.
- When your app first attempts to run an AR session or otherwise use the camera, iOS automatically shows an alert with your camera usage description message, asking the user to grant camera permission to your app. If the user accepts this request, the session begins; otherwise the session fails with this error.
- If the user has previously denied camera permission for your app, all attempts to run an AR session or otherwise use the camera fail with this error. To grant camera permission, the user must explicitly enable your app in the iOS Settings app, under Privacy > Camera.

## See Also

- [ARError.Code.requestFailed](arerror/code/requestfailed.md)
  An error that indicates a request fails.
- [ARError.Code.fileIOFailed](arerror/code/fileiofailed.md)
  An error that indicates a file access fails to read or write.
- [ARError.Code.insufficientFeatures](arerror/code/insufficientfeatures.md)
  An error that indicates the framework requires more features to complete a task.
- [ARError.Code.invalidCollaborationData](arerror/code/invalidcollaborationdata.md)
  An error that indicates the framework fails to parse collaboration data the app receives over the network.
- [ARError.Code.invalidConfiguration](arerror/code/invalidconfiguration.md)
  An error that indicates the configuration contains ambiguous or erroneous data.
- [ARError.Code.invalidReferenceImage](arerror/code/invalidreferenceimage.md)
  An error that indicates the framework fails to process a reference image.
- [ARError.Code.invalidReferenceObject](arerror/code/invalidreferenceobject.md)
  An error that indicates the framework fails to process a reference object.
- [ARError.Code.invalidWorldMap](arerror/code/invalidworldmap.md)
  An error that indicates the framework fails to process a world map.
- [ARError.Code.microphoneUnauthorized](arerror/code/microphoneunauthorized.md)
  An error that indicates the app lacks user permission for the microphone.
- [ARError.Code.objectMergeFailed](arerror/code/objectmergefailed.md)
  An error that indicates the framework fails to merge a detected object.
- [ARError.Code.sensorFailed](arerror/code/sensorfailed.md)
  An error that indicates a sensor fails to provide required input.
- [ARError.Code.sensorUnavailable](arerror/code/sensorunavailable.md)
  An error that indicates the framework fails to access a required sensor.
- [ARError.Code.unsupportedConfiguration](arerror/code/unsupportedconfiguration.md)
  An error that indicates the device lacks support for the session’s configuration.
- [ARError.Code.worldTrackingFailed](arerror/code/worldtrackingfailed.md)
  An error that indicates when world tracking experiences an unrecoverable problem.
- [ARError.Code.geoTrackingFailed](arerror/code/geotrackingfailed.md)
  An error that indicates when localization imagery fails to match the device’s camera captures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arerror/code/cameraunauthorized)*