# AVCaptureDeviceDirectionMap

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

An object that groups the cameras a coordinator tracks by the direction they face.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+

## Declaration

```swift
class AVCaptureDeviceDirectionMap
```

```objc
@interface AVCaptureDeviceDirectionMap : NSObject
```

## Mentions

- [Choosing a camera by the direction it faces](./choosing-a-camera-by-the-direction-it-faces.md)

## Overview

You don’t create instances of `AVCaptureDeviceDirectionMap` directly. An [`AVCaptureDeviceDirectionCoordinator`](./avcapturedevicedirectioncoordinator.md) object creates a map for the view you give it, and passes an updated map to your change handler each time a camera changes direction.

A map groups the device types you gave the coordinator into two arrays, using the view as the point of reference. The [`forwardFacingDeviceDescriptors`](./avcapturedevicedirectionmap/forwardfacingdevicedescriptors.md) array describes the cameras that face the same direction as the view, toward the person looking at it. The [`backwardFacingDeviceDescriptors`](./avcapturedevicedirectionmap/backwardfacingdevicedescriptors.md) array describes the cameras that face the other way, toward the scene beyond it. Each array holds [`AVCaptureDeviceDescriptor`](./avcapturedevicedescriptor.md) values rather than capture devices.

> **Note**: Either array can be empty when no camera is available or applicable for the current configuration.

## Topics

### Reading the camera directions
- [var forwardFacingDeviceDescriptors: [AVCaptureDeviceDescriptor]](./avcapturedevicedirectionmap/forwardfacingdevicedescriptors.md)
  Descriptions of the capture devices that face the same direction as the view.
- [var backwardFacingDeviceDescriptors: [AVCaptureDeviceDescriptor]](./avcapturedevicedirectionmap/backwardfacingdevicedescriptors.md)
  Descriptions of the capture devices that face away from the view.

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
- [class AVCaptureDeviceDescriptor](./avcapturedevicedescriptor.md)
  An object that identifies a capture device and is safe to pass between actors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedirectionmap)*