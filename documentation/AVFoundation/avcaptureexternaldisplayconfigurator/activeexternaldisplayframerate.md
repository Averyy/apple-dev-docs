# activeExternalDisplayFrameRate

**Framework**: AVFoundation  
**Kind**: property

The currently configured frame rate on the external display that’s displaying the preview layer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var activeExternalDisplayFrameRate: Double { get }
```

#### Discussion

Observe this property to determine if the configured frame rate matches the max frame rate ([`activeVideoMinFrameDuration`](avcapturedevice/activevideominframeduration.md)) of the device. When the [`isActive`](avcaptureexternaldisplayconfigurator/isactive.md) property becomes `false`, this property changes to 0.

## See Also

- [var device: AVCaptureDevice?](avcaptureexternaldisplayconfigurator/device.md)
  The device for which the coordinator configures the preview layer.
- [var isActive: Bool](avcaptureexternaldisplayconfigurator/isactive.md)
  This property tells you whether the configurator is actively configuring the external display.
- [var previewLayer: CALayer?](avcaptureexternaldisplayconfigurator/previewlayer.md)
  The layer for which the configurator adjusts display properties to match the device’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/activeexternaldisplayframerate)*