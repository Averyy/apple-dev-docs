# AVCaptureDeviceDescriptor

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

An object that identifies a capture device and is safe to pass between actors.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+

## Declaration

```swift
class AVCaptureDeviceDescriptor
```

```objc
@interface AVCaptureDeviceDescriptor : NSObject
```

## Mentions

- [Choosing a camera by the direction it faces](./choosing-a-camera-by-the-direction-it-faces.md)

#### Overview

A descriptor is a [`Sendable`](../Swift/sendable.md) representation of a capture device. An [`AVCaptureDeviceDirectionCoordinator`](./avcapturedevicedirectioncoordinator.md) object reports descriptors on the main actor, where the capture APIs in AVFoundation shouldn’t run. Pass a descriptor to a background actor and create the [`AVCaptureDevice`](../AVFoundation/avcapturedevice.md) there. Read its properties on the main actor to update your interface.

You don’t create `AVCaptureDeviceDescriptor` objects directly. An [`AVCaptureDeviceDirectionMap`](./avcapturedevicedirectionmap.md) object reports the cameras facing each direction as arrays of descriptors.

## Topics

### Identifying the device
- [var uniqueID: String](./avcapturedevicedescriptor/uniqueid.md)
  An identifier that uniquely identifies the device’s camera.
- [var localizedName: String](./avcapturedevicedescriptor/localizedname.md)
  A name for the camera that’s suitable for display in your interface.
### Inspecting the device’s characteristics
- [var deviceType: AVCaptureDevice.DeviceType](./avcapturedevicedescriptor/devicetype.md)
  The kind of camera, such as a wide-angle or telephoto camera.
- [var mediaTypes: Set<AVMediaType>](./avcapturedevicedescriptor/mediatypes.md)
  The kinds of media the camera captures.
- [var position: AVCaptureDevice.Position](./avcapturedevicedescriptor/position.md)
  The physical position of the camera on the device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Camera facing direction
- [Choosing a camera by the direction it faces](./choosing-a-camera-by-the-direction-it-faces.md)
  Find out which way each camera faces, and follow the change as someone opens and closes the device.
- [class AVCaptureDeviceDirectionCoordinator](./avcapturedevicedirectioncoordinator.md)
  An object that tracks the direction each camera faces in relation to a view.
- [class AVCaptureDeviceDirectionMap](./avcapturedevicedirectionmap.md)
  An object that groups the cameras a coordinator tracks by the direction they face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor)*