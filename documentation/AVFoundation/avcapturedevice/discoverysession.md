# AVCaptureDevice.DiscoverySession

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that finds capture devices that match specific search criteria.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
class DiscoverySession
```

```objc
@interface AVCaptureDeviceDiscoverySession : NSObject
```

## Mentions

- [Choosing a capture device](../choosing-a-capture-device.md)
- [Adopting smart framing in your camera app](../adopting-smart-framing-in-your-camera-app.md)

## Overview

After creating a device discovery session, query its [`devices`](./discoverysession/devices.md) property to find a device to use for capture. You can also key-value observe this property to monitor changes to the list of available devices.

## Topics

### Creating a session
- [convenience init(deviceTypes: [AVCaptureDevice.DeviceType], mediaType: AVMediaType?, position: AVCaptureDevice.Position)](./discoverysession/init%28devicetypes,mediatype,position%29.md)
  Creates a discovery session that finds devices that match the specified criteria.
### Finding devices
- [var devices: [AVCaptureDevice]](./discoverysession/devices.md)
  A list of devices that match the search criteria of the discovery session.
- [var supportedMultiCamDeviceSets: [Set<AVCaptureDevice>]](./discoverysession/supportedmulticamdevicesets.md)
  Sets of capture devices that you can use simultaneously in a multi-camera session.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Finding and monitoring devices
- [class func `default`(AVCaptureDevice.DeviceType, for: AVMediaType?, position: AVCaptureDevice.Position) -> AVCaptureDevice?](./default%28_,for,position%29.md)
  Returns the default device for the specified device type, media type, and position.
- [class func `default`(for: AVMediaType) -> AVCaptureDevice?](./default%28for%29.md)
  Returns the default device that captures the specified media type.
- [init?(uniqueID: String)](./init%28uniqueid%29.md)
  Creates an object that represents a device with the specified identifier.
- [class let wasConnectedNotification: NSNotification.Name](./wasconnectednotification.md)
  A notification the system posts when a new capture device becomes available.
- [class let wasDisconnectedNotification: NSNotification.Name](./wasdisconnectednotification.md)
  A notification the system posts when an existing device becomes unavailable.
- [class func devices(for: AVMediaType) -> [AVCaptureDevice]](./devices%28for%29.md)
  Returns devices capable of capturing media of the specified type.
- [class func devices() -> [AVCaptureDevice]](./devices%28%29.md)
  Returns all available capture devices on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/discoverysession)*