# init(uniqueID:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates an object that represents a device with the specified identifier.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
init?(uniqueID deviceUniqueID: String)
```

```objc
+ (AVCaptureDevice *) deviceWithUniqueID:(NSString *) deviceUniqueID;
```

## Return Value

A capture device, or `nil` if no device with the specified identifier exists.

## Discussion

Every capture device has a unique identifier that persists on a system across device connections, app restarts, and reboots of the system itself.

## Parameters

- `deviceUniqueID`: An identifier that uniquely identifies the device.

## See Also

### Finding and monitoring devices
- [AVCaptureDevice.DiscoverySession](./discoverysession.md)
  An object that finds capture devices that match specific search criteria.
- [class func `default`(AVCaptureDevice.DeviceType, for: AVMediaType?, position: AVCaptureDevice.Position) -> AVCaptureDevice?](./default%28_,for,position%29.md)
  Returns the default device for the specified device type, media type, and position.
- [class func `default`(for: AVMediaType) -> AVCaptureDevice?](./default%28for%29.md)
  Returns the default device that captures the specified media type.
- [class let wasConnectedNotification: NSNotification.Name](./wasconnectednotification.md)
  A notification the system posts when a new capture device becomes available.
- [class let wasDisconnectedNotification: NSNotification.Name](./wasdisconnectednotification.md)
  A notification the system posts when an existing device becomes unavailable.
- [class func devices(for: AVMediaType) -> [AVCaptureDevice]](./devices%28for%29.md)
  Returns devices capable of capturing media of the specified type.
- [class func devices() -> [AVCaptureDevice]](./devices%28%29.md)
  Returns all available capture devices on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/init(uniqueid:))*