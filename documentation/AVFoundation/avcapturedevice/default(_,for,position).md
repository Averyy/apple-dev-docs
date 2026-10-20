# default(_:for:position:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns the default device for the specified device type, media type, and position.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
class func `default`(_ deviceType: AVCaptureDevice.DeviceType, for mediaType: AVMediaType?, position: AVCaptureDevice.Position) -> AVCaptureDevice?
```

```objc
+ (AVCaptureDevice *) defaultDeviceWithDeviceType:(AVCaptureDeviceType) deviceType mediaType:(AVMediaType) mediaType position:(AVCaptureDevicePosition) position;
```

## Mentions

- [Choosing a capture device](../choosing-a-capture-device.md)

#### Return Value

The default system device, or `nil` if no device currently exists that satisfies the specified criteria.

#### Discussion

Use this method to select the system default capture device for a given scenario. For example, to obtain the dual camera on supported hardware and fall back to the standard wide-angle camera otherwise, call this method twice, as shown below.

```swift
// The app's default camera.
var defaultCamera: AVCaptureDevice? {
    // Find the built-in dual camera, if it exists.
    if let device = AVCaptureDevice.default(.builtInDualCamera,
                                            for: .video,
                                            position: .back) {
        return device
    }
    
    // Find the built-in wide-angle camera, if it exists.
    if let device = AVCaptureDevice.default(.builtInWideAngleCamera,
                                            for: .video,
                                            position: .back) {
        return device
    }
    return nil
}
```

## Parameters

- `deviceType`: The type of capture device to request, such as [`builtInWideAngleCamera`](./devicetype-swift.struct/builtinwideanglecamera.md).
- `mediaType`: The type of media to request capture of, such as [`video`](../avmediatype/video.md) or [`audio`](../avmediatype/audio.md).
- `position`: The position of capture device to request relative to system hardware (front- or back-facing). Pass [`AVCaptureDevice.Position.unspecified`](./position-swift.enum/unspecified.md) to search for devices regardless of position.

## See Also

### Finding and monitoring devices
- [AVCaptureDevice.DiscoverySession](./discoverysession.md)
  An object that finds capture devices that match specific search criteria.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/default(_:for:position:))*