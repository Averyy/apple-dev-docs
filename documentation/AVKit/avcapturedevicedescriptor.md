# AVCaptureDeviceDescriptor

**Framework**: AVKit  
**Kind**: class

An object that identifies a capture device and is safe to pass between actors.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
class AVCaptureDeviceDescriptor
```

## Mentions

- [Choosing a camera by the direction it faces](choosing-a-camera-by-the-direction-it-faces.md)

#### Overview

A descriptor is a [`Sendable`](https://developer.apple.com/documentation/swift/sendable) representation of a capture device. An [`AVCaptureDeviceDirectionCoordinator`](avcapturedevicedirectioncoordinator.md) object reports descriptors on the main actor, where the capture APIs in AVFoundation shouldn’t run. Pass a descriptor to a background actor and create the [`AVCaptureDevice`](https://developer.apple.com/documentation/avfoundation/avcapturedevice) there. Read its properties on the main actor to update your interface.

You don’t create `AVCaptureDeviceDescriptor` objects directly. An [`AVCaptureDeviceDirectionMap`](avcapturedevicedirectionmap.md) object reports the cameras facing each direction as arrays of descriptors.

## Topics

### Identifying the device
- [var uniqueID: String](avcapturedevicedescriptor/uniqueid.md)
  An identifier that uniquely identifies the device’s camera.
- [var localizedName: String](avcapturedevicedescriptor/localizedname.md)
  A name for the camera that’s suitable for display in your interface.
### Inspecting the device’s characteristics
- [var deviceType: AVCaptureDevice.DeviceType](avcapturedevicedescriptor/devicetype.md)
  The kind of camera, such as a wide-angle or telephoto camera.
- [var mediaTypes: Set<AVMediaType>](avcapturedevicedescriptor/mediatypes.md)
  The kinds of media the camera captures.
- [var position: AVCaptureDevice.Position](avcapturedevicedescriptor/position.md)
  The physical position of the camera on the device.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Choosing a camera by the direction it faces](choosing-a-camera-by-the-direction-it-faces.md)
  Find out which way each camera faces, and follow the change as someone opens and closes the device.
- [class AVCaptureDeviceDirectionCoordinator](avcapturedevicedirectioncoordinator.md)
  An object that tracks the direction each camera faces in relation to a view.
- [class AVCaptureDeviceDirectionMap](avcapturedevicedirectionmap.md)
  An object that groups the cameras a coordinator tracks by the direction they face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor)*