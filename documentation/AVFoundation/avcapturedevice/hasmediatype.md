# hasMediaType(_:)

**Framework**: AVFoundation  
**Kind**: method

Returns a Boolean value that indicates whether the device captures media of a particular type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func hasMediaType(_ mediaType: AVMediaType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the device captures media of the specified type; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `mediaType`: A media type, such as  ,  , or  .

## See Also

- [var isVirtualDevice: Bool](avcapturedevice/isvirtualdevice.md)
  A Boolean value that indicates whether the device consists of two or more physical devices.
- [var constituentDevices: [AVCaptureDevice]](avcapturedevice/constituentdevices.md)
  An array of physical devices that make up a virtual device.
- [var transportType: Int32](avcapturedevice/transporttype.md)
  The transport type of the device.
- [func supportsSessionPreset(AVCaptureSession.Preset) -> Bool](avcapturedevice/supportssessionpreset(_:).md)
  Returns a Boolean value that indicates whether you can use the device with capture session configured with the specified preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/hasmediatype(_:))*