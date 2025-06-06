# AVCaptureDevice.DiscoverySession

**Framework**: AVFoundation  
**Kind**: class

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

## Mentions

- [Choosing a Capture Device](choosing-a-capture-device.md)

#### Overview

After creating a device discovery session, query its [`devices`](avcapturedevice/discoverysession/devices.md) property to find a device to use for capture. You can also key-value observe this property to monitor changes to the list of available devices.

## Topics

### Creating a Session
- [convenience init(deviceTypes: [AVCaptureDevice.DeviceType], mediaType: AVMediaType?, position: AVCaptureDevice.Position)](avcapturedevice/discoverysession/init(devicetypes:mediatype:position:).md)
  Creates a discovery session that finds devices that match the specified criteria.
### Finding Devices
- [var devices: [AVCaptureDevice]](avcapturedevice/discoverysession/devices.md)
  A list of devices that match the search criteria of the discovery session.
- [var supportedMultiCamDeviceSets: [Set<AVCaptureDevice>]](avcapturedevice/discoverysession/supportedmulticamdevicesets.md)
  Sets of capture devices that you can use simultaneously in a multi-camera session.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class func `default`(AVCaptureDevice.DeviceType, for: AVMediaType?, position: AVCaptureDevice.Position) -> AVCaptureDevice?](avcapturedevice/default(_:for:position:).md)
  Returns the default device for the specified device type, media type, and position.
- [class func `default`(for: AVMediaType) -> AVCaptureDevice?](avcapturedevice/default(for:).md)
  Returns the default device that captures the specified media type.
- [init?(uniqueID: String)](avcapturedevice/init(uniqueid:).md)
  Creates an object that represents a device with the specified identifier.
- [class let wasConnectedNotification: NSNotification.Name](avcapturedevice/wasconnectednotification.md)
  A notification the system posts when a new capture device becomes available.
- [class let wasDisconnectedNotification: NSNotification.Name](avcapturedevice/wasdisconnectednotification.md)
  A notification the system posts when an existing device becomes unavailable.
- [class func devices(for: AVMediaType) -> [AVCaptureDevice]](avcapturedevice/devices(for:).md)
  Returns devices capable of capturing media of the specified type.
- [class func devices() -> [AVCaptureDevice]](avcapturedevice/devices.md)
  Returns all available capture devices on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/discoverysession)*