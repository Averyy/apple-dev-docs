# CameraFrameProvider

**Framework**: ARKit  
**Kind**: class

An object that provides camera streams.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final class CameraFrameProvider
```

#### Overview

You use `CameraFrameProvider` to receive camera images for selected video formats.

## Topics

### Creating a camera frame provider
- [init()](cameraframeprovider/init.md)
  Creates a camera frame provider.
### Getting information about the camera frame provider
- [var description: String](cameraframeprovider/description.md)
  A textual representation of this camera frame provider.
- [var state: DataProviderState](cameraframeprovider/state.md)
  The state of a camera frame provider.
### Getting camera frame updates
- [func cameraFrameUpdates(for: CameraVideoFormat) -> CameraFrameProvider.CameraFrameUpdates?](cameraframeprovider/cameraframeupdates(for:).md)
  Gets a sequence of camera frame updates for a given video format.
- [CameraFrameProvider.CameraFrameUpdates](cameraframeprovider/cameraframeupdates.md)
  A sequence of camera frames.
### Enumerations
- [CameraFrameProvider.CameraPosition](cameraframeprovider/cameraposition.md)
  Values that describe possible camera positions.
- [CameraFrameProvider.CameraType](cameraframeprovider/cameratype.md)
  Values that describe possible camera types.
### Type Properties
- [static var isSupported: Bool](cameraframeprovider/issupported.md)
  A Boolean value that indicates whether this device supports the camera frame provider.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](cameraframeprovider/requiredauthorizations.md)
  The authorization types you need to use the camera frame provider.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CameraFrame](cameraframe.md)
  The representation of a camera frame.
- [struct CameraVideoFormat](cameravideoformat.md)
  A structure that represents a camera video format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframeprovider)*