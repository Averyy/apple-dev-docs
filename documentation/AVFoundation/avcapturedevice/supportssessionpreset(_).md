# supportsSessionPreset(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) supportsAVCaptureSessionPreset:(AVCaptureSessionPreset) preset;
```

#### Return Value

[`true`](../../Swift/true.md) if you can use the device; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `preset`: A capture session preset.

## See Also

### Inspecting device characteristics
- [var isVirtualDevice: Bool](./isvirtualdevice.md)
  A Boolean value that indicates whether the device consists of two or more physical devices.
- [var constituentDevices: [AVCaptureDevice]](./constituentdevices.md)
  An array of physical devices that make up a virtual device.
- [func hasMediaType(AVMediaType) -> Bool](./hasmediatype%28_%29.md)
  Returns a Boolean value that indicates whether the device captures media of a particular type.
- [var transportType: Int32](./transporttype.md)
  The transport type of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/supportssessionpreset(_:))*