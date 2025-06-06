# UIDeviceOrientation

**Framework**: UIKit  
**Kind**: enum

Constants that describe the physical orientation of the device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
enum UIDeviceOrientation
```

#### Overview

The [`orientation`](uidevice/orientation.md) property uses these constants to identify the device orientation. These constants identify the physical orientation of the device and aren’t tied to the orientation of your app’s user interface.

## Topics

### Device orientations
- [UIDeviceOrientation.unknown](uideviceorientation/unknown.md)
  The orientation of the device can’t be determined.
- [UIDeviceOrientation.portrait](uideviceorientation/portrait.md)
  The device is in portrait mode, with the device held upright and the front-facing camera at the top.
- [UIDeviceOrientation.portraitUpsideDown](uideviceorientation/portraitupsidedown.md)
  The device is in portrait mode but upside down, with the device held upright and the front-facing camera at the bottom.
- [UIDeviceOrientation.landscapeLeft](uideviceorientation/landscapeleft.md)
  The device is in landscape mode, with the device held upright and the front-facing camera on the left side.
- [UIDeviceOrientation.landscapeRight](uideviceorientation/landscaperight.md)
  The device is in landscape mode, with the device held upright and the front-facing camera on the right side.
- [UIDeviceOrientation.faceUp](uideviceorientation/faceup.md)
  The device is held parallel to the ground with the screen facing upwards.
- [UIDeviceOrientation.faceDown](uideviceorientation/facedown.md)
  The device is held parallel to the ground with the screen facing downwards.
### Orientation testing
- [var isPortrait: Bool](uideviceorientation/isportrait.md)
  A Boolean value that indicates whether the device is in a portrait orientation.
- [var isLandscape: Bool](uideviceorientation/islandscape.md)
  A Boolean value that indicates whether the device is in a landscape orientation.
- [var isFlat: Bool](uideviceorientation/isflat.md)
  A Boolean value that indicates whether the specified orientation is face up or face down.
- [var isValidInterfaceOrientation: Bool](uideviceorientation/isvalidinterfaceorientation.md)
  A Boolean value that indicates whether the specified orientation is one of the portrait or landscape orientations.
### Initializers
- [init?(rawValue: Int)](uideviceorientation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var orientation: UIDeviceOrientation](uidevice/orientation.md)
  The physical orientation of the device.
- [var isGeneratingDeviceOrientationNotifications: Bool](uidevice/isgeneratingdeviceorientationnotifications.md)
  A Boolean value that indicates whether the device generates orientation notifications.
- [func beginGeneratingDeviceOrientationNotifications()](uidevice/begingeneratingdeviceorientationnotifications.md)
  Begins the generation of notifications of device orientation changes.
- [func endGeneratingDeviceOrientationNotifications()](uidevice/endgeneratingdeviceorientationnotifications.md)
  Ends the generation of notifications of device orientation changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uideviceorientation)*