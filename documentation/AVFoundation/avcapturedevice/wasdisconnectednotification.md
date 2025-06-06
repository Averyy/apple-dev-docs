# wasDisconnectedNotification

**Framework**: AVFoundation  
**Kind**: property

A notification the system posts when an existing device becomes unavailable.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
class let wasDisconnectedNotification: NSNotification.Name
```

#### Discussion

The notification’s [`object`](https://developer.apple.com/documentation/foundation/notification/1779839-object) property contains the capture device that disconnected.

## See Also

- [AVCaptureDevice.DiscoverySession](avcapturedevice/discoverysession.md)
  An object that finds capture devices that match specific search criteria.
- [class func `default`(AVCaptureDevice.DeviceType, for: AVMediaType?, position: AVCaptureDevice.Position) -> AVCaptureDevice?](avcapturedevice/default(_:for:position:).md)
  Returns the default device for the specified device type, media type, and position.
- [class func `default`(for: AVMediaType) -> AVCaptureDevice?](avcapturedevice/default(for:).md)
  Returns the default device that captures the specified media type.
- [init?(uniqueID: String)](avcapturedevice/init(uniqueid:).md)
  Creates an object that represents a device with the specified identifier.
- [class let wasConnectedNotification: NSNotification.Name](avcapturedevice/wasconnectednotification.md)
  A notification the system posts when a new capture device becomes available.
- [class func devices(for: AVMediaType) -> [AVCaptureDevice]](avcapturedevice/devices(for:).md)
  Returns devices capable of capturing media of the specified type.
- [class func devices() -> [AVCaptureDevice]](avcapturedevice/devices.md)
  Returns all available capture devices on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/wasdisconnectednotification)*