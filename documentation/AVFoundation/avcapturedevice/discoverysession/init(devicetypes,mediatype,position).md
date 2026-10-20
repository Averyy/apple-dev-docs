# init(deviceTypes:mediaType:position:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a discovery session that finds devices that match the specified criteria.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
convenience init(deviceTypes: [AVCaptureDevice.DeviceType], mediaType: AVMediaType?, position: AVCaptureDevice.Position)
```

```objc
+ (instancetype) discoverySessionWithDeviceTypes:(NSArray<NSString *> *) deviceTypes mediaType:(AVMediaType) mediaType position:(AVCaptureDevicePosition) position;
```

#### Return Value

A new discovery session.

#### Discussion

After creating a discovery session, query its [`devices`](./devices.md) property to examine matching devices and choose one for capture.

## Parameters

- `deviceTypes`: A list of device types to search for, such as [`builtInWideAngleCamera`](../devicetype-swift.struct/builtinwideanglecamera.md) and [`builtInMicrophone`](../devicetype-swift.struct/builtinmicrophone.md). The array must contain at least one valid [`AVCaptureDevice.DeviceType`](../devicetype-swift.struct.md) value.
- `mediaType`: The media type to capture, such as [`video`](../../avmediatype/video.md) or [`audio`](../../avmediatype/audio.md). Pass `nil` to search for devices regardless of supported media types.
- `position`: The position of capture device to search for, relative to system hardware (front- or back-facing). Pass [`AVCaptureDevice.Position.unspecified`](../position-swift.enum/unspecified.md) to search for devices regardless of position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/discoverysession/init(devicetypes:mediatype:position:))*