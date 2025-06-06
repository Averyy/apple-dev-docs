# ARError.Code.invalidReferenceImage

**Framework**: ARKit  
**Kind**: case

An error that indicates the framework fails to process a reference image.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
case invalidReferenceImage
```

#### Discussion

This error occurs when you supply a reference image to the configuration’s [`detectionImages`](arworldtrackingconfiguration/detectionimages.md) but ARKit determined it’s unusable. This can happen when the image data doesn’t contain enough features to identify a unique picture, for example, it’s all white.

## See Also

- [ARError.Code.requestFailed](arerror/code/requestfailed.md)
  An error that indicates a request fails.
- [ARError.Code.cameraUnauthorized](arerror/code/cameraunauthorized.md)
  An error that indicates the app lacks user permission for the camera.
- [ARError.Code.fileIOFailed](arerror/code/fileiofailed.md)
  An error that indicates a file access fails to read or write.
- [ARError.Code.insufficientFeatures](arerror/code/insufficientfeatures.md)
  An error that indicates the framework requires more features to complete a task.
- [ARError.Code.invalidCollaborationData](arerror/code/invalidcollaborationdata.md)
  An error that indicates the framework fails to parse collaboration data the app receives over the network.
- [ARError.Code.invalidConfiguration](arerror/code/invalidconfiguration.md)
  An error that indicates the configuration contains ambiguous or erroneous data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arerror/code/invalidreferenceimage)*