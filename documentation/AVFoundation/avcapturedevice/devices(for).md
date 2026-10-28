# devices(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns devices capable of capturing media of the specified type.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.15

> **Deprecated**: Use the [`AVCaptureDevice.DiscoverySession`](./discoverysession.md) class instead.

## Declaration

```swift
class func devices(for mediaType: AVMediaType) -> [AVCaptureDevice]
```

```objc
+ (NSArray<AVCaptureDevice *> *) devicesWithMediaType:(AVMediaType) mediaType;
```

## Return Value

An array of devices, or an empty array of none exist.

## Parameters

- `mediaType`: A media type for the device.

## See Also

### Finding and monitoring devices
- [AVCaptureDevice.DiscoverySession](./discoverysession.md)
  An object that finds capture devices that match specific search criteria.
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
- [class func devices() -> [AVCaptureDevice]](./devices%28%29.md)
  Returns all available capture devices on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devices(for:))*