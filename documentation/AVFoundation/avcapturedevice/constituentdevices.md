# constituentDevices

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of physical devices that make up a virtual device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var constituentDevices: [AVCaptureDevice] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVCaptureDevice *> * constituentDevices;
```

#### Discussion

The value of this property is an empty array when called on a device whose [`isVirtualDevice`](./isvirtualdevice.md) property is [`false`](../../Swift/false.md).

## See Also

### Inspecting device characteristics
- [var isVirtualDevice: Bool](./isvirtualdevice.md)
  A Boolean value that indicates whether the device consists of two or more physical devices.
- [func hasMediaType(AVMediaType) -> Bool](./hasmediatype%28_%29.md)
  Returns a Boolean value that indicates whether the device captures media of a particular type.
- [var transportType: Int32](./transporttype.md)
  The transport type of the device.
- [func supportsSessionPreset(AVCaptureSession.Preset) -> Bool](./supportssessionpreset%28_%29.md)
  Returns a Boolean value that indicates whether you can use the device with capture session configured with the specified preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/constituentdevices)*