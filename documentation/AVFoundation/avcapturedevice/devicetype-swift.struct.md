# AVCaptureDevice.DeviceType

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A structure that defines the device types the framework supports.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
struct DeviceType
```

```c
typedef NSString * AVCaptureDeviceType;
```

## Discussion

Use the device type constants to retrieve devices using an [`AVCaptureDevice.DiscoverySession`](./discoverysession.md) object, or when calling the [`default(_:for:position:)`](./default%28_,for,position%29.md) method.

## Topics

### Cameras
- [static let builtInWideAngleCamera: AVCaptureDevice.DeviceType](./devicetype-swift.struct/builtinwideanglecamera.md)
  A built-in wide-angle camera device type.
- [static let builtInUltraWideCamera: AVCaptureDevice.DeviceType](./devicetype-swift.struct/builtinultrawidecamera.md)
  A built-in camera device type with a shorter focal length than a wide-angle camera.
- [static let builtInTelephotoCamera: AVCaptureDevice.DeviceType](./devicetype-swift.struct/builtintelephotocamera.md)
  A built-in camera device type with a longer focal length than a wide-angle camera.
- [static let builtInDualCamera: AVCaptureDevice.DeviceType](./devicetype-swift.struct/builtindualcamera.md)
  A built-in camera device type that consists of a wide-angle and telephoto camera.
- [static let builtInDualWideCamera: AVCaptureDevice.DeviceType](./devicetype-swift.struct/builtindualwidecamera.md)
  A built-in camera device type that consists of two cameras of fixed focal length, one ultrawide angle and one wide angle.
- [static let builtInTripleCamera: AVCaptureDevice.DeviceType](./devicetype-swift.struct/builtintriplecamera.md)
  A built-in camera device type that consists of three cameras of fixed focal length, one ultrawide angle, one wide angle, and one telephoto.
- [static let continuityCamera: AVCaptureDevice.DeviceType](./devicetype-swift.struct/continuitycamera.md)
  A Continuity Camera device type.
- [static let builtInDuoCamera: AVCaptureDevice.DeviceType](./devicetype-swift.struct/builtinduocamera.md)
  A built-in dual camera device type.
### Microphones
- [static let microphone: AVCaptureDevice.DeviceType](./devicetype-swift.struct/microphone.md)
  A microphone device type.
- [static let builtInMicrophone: AVCaptureDevice.DeviceType](./devicetype-swift.struct/builtinmicrophone.md)
  A built-in microphone.
### External devices
- [static let external: AVCaptureDevice.DeviceType](./devicetype-swift.struct/external.md)
  An external device type.
- [static let externalUnknown: AVCaptureDevice.DeviceType](./devicetype-swift.struct/externalunknown.md)
  An unknown external device type.
### Desk View
- [static let deskViewCamera: AVCaptureDevice.DeviceType](./devicetype-swift.struct/deskviewcamera.md)
  A virtual overhead camera that captures a user’s desk.
### Depth sensing
- [static let builtInLiDARDepthCamera: AVCaptureDevice.DeviceType](./devicetype-swift.struct/builtinlidardepthcamera.md)
  A device that consists of two cameras, one LiDAR and one YUV.
- [static let builtInTrueDepthCamera: AVCaptureDevice.DeviceType](./devicetype-swift.struct/builtintruedepthcamera.md)
  A device that consists of two cameras, one Infrared and one YUV.
### Initializers
- [init(rawValue: String)](./devicetype-swift.struct/init%28rawvalue%29.md)
  Creates a capture device type with a string value.
### Type Properties
- [static let builtInInnerUltraWideCamera: AVCaptureDevice.DeviceType](./devicetype-swift.struct/builtininnerultrawidecamera.md)
- [static let builtInOuterUltraWideCamera: AVCaptureDevice.DeviceType](./devicetype-swift.struct/builtinouterultrawidecamera.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Identifying a device
- [var uniqueID: String](./uniqueid.md)
  An identifier that uniquely identifies the device.
- [var modelID: String](./modelid.md)
  A model identifier for the device.
- [var localizedName: String](./localizedname.md)
  A localized device name for display in the user interface.
- [var manufacturer: String](./manufacturer.md)
  A human-readable string for the manufacturer of the device.
- [var deviceType: AVCaptureDevice.DeviceType](./devicetype-swift.property.md)
  The type of device, such as a built-in microphone or wide-angle camera.
- [var position: AVCaptureDevice.Position](./position-swift.property.md)
  The physical position of the capture device hardware.
- [AVCaptureDevice.Position](./position-swift.enum.md)
  Constants that indicate the physical position of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct)*