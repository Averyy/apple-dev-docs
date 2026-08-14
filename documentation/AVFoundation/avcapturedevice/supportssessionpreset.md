# supportsSessionPreset(_:)

**Framework**: AVFoundation  
**Kind**: method

Returns a Boolean value that indicates whether you can use the device with capture session configured with the specified preset.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
func supportsSessionPreset(_ preset: AVCaptureSession.Preset) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if you can use the device; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `preset`: A capture session preset.

## See Also

- [var isVirtualDevice: Bool](avcapturedevice/isvirtualdevice.md)
  A Boolean value that indicates whether the device consists of two or more physical devices.
- [var constituentDevices: [AVCaptureDevice]](avcapturedevice/constituentdevices.md)
  An array of physical devices that make up a virtual device.
- [func hasMediaType(AVMediaType) -> Bool](avcapturedevice/hasmediatype(_:).md)
  Returns a Boolean value that indicates whether the device captures media of a particular type.
- [var transportType: Int32](avcapturedevice/transporttype.md)
  The transport type of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/supportssessionpreset(_:))*