# hasMediaType(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) hasMediaType:(AVMediaType) mediaType;
```

#### Return Value

[`true`](../../Swift/true.md) if the device captures media of the specified type; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `mediaType`: A media type, such as [`video`](../avmediatype/video.md), [`audio`](../avmediatype/audio.md), or [`muxed`](../avmediatype/muxed.md).

## See Also

### Inspecting device characteristics
- [var isVirtualDevice: Bool](./isvirtualdevice.md)
  A Boolean value that indicates whether the device consists of two or more physical devices.
- [var constituentDevices: [AVCaptureDevice]](./constituentdevices.md)
  An array of physical devices that make up a virtual device.
- [var transportType: Int32](./transporttype.md)
  The transport type of the device.
- [func supportsSessionPreset(AVCaptureSession.Preset) -> Bool](./supportssessionpreset%28_%29.md)
  Returns a Boolean value that indicates whether you can use the device with capture session configured with the specified preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/hasmediatype(_:))*