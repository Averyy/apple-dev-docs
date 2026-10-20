# default(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns the default device that captures the specified media type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
class func `default`(for mediaType: AVMediaType) -> AVCaptureDevice?
```

```objc
+ (AVCaptureDevice *) defaultDeviceWithMediaType:(AVMediaType) mediaType;
```

#### Return Value

The default device, or `nil` if no device with that media type exists.

## Parameters

- `mediaType`: A media type for the device.

## See Also

### Finding and monitoring devices
- [AVCaptureDevice.DiscoverySession](./discoverysession.md)
  An object that finds capture devices that match specific search criteria.
- [class func `default`(AVCaptureDevice.DeviceType, for: AVMediaType?, position: AVCaptureDevice.Position) -> AVCaptureDevice?](./default%28_,for,position%29.md)
  Returns the default device for the specified device type, media type, and position.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/default(for:))*