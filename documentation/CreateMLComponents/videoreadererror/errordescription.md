# errorDescription

**Framework**: Create ML Components  
**Kind**: property

A localized message describing what error occurred.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var errorDescription: String? { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreadererror/errordescription)*