# VideoReaderError.missingVideoTrack(_:)

**Framework**: Create ML Components  
**Kind**: case  
**Role**: Case

An error that indicates that the VideoReader cannot find a video track.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case missingVideoTrack(URL)
```

## See Also

### Analyzing the error
- [VideoReaderError.cameraAuthorizationDenied](./cameraauthorizationdenied.md)
  An error that indicates that the camera authorization status is denied. The user has explicitly denied permission for media capture.
- [VideoReaderError.cameraAuthorizationRestricted](./cameraauthorizationrestricted.md)
  An error that indicates that the camera authorization status is restricted. The user is not allowed to access media capture devices.
- [VideoReaderError.frameRateNotSupported(_:)](./frameratenotsupported%28_%29.md)
  An error that indicates that the frame rate is not supported by the input camera.
- [VideoReaderError.sourceCameraNotAvailable](./sourcecameranotavailable.md)
  An error that indicates that no cameras are available.
- [VideoReaderError.captureSessionStopped](./capturesessionstopped.md)
  An error that indicates that the capture session stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreadererror/missingvideotrack(_:))*