# isActive

**Framework**: AVFoundation  
**Kind**: property

This property tells you whether the configurator is actively configuring the external display.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isActive: Bool { get }
```

#### Discussion

When this property returns `true`, the external display is successfully configured to match the device. If it returns`false`, the configurator is not making any configuration changes to the external display. If another [`AVCaptureExternalDisplayConfigurator`](avcaptureexternaldisplayconfigurator.md) instance takes over the configuration of the external display, this property returns `false`.

## See Also

- [var activeExternalDisplayFrameRate: Double](avcaptureexternaldisplayconfigurator/activeexternaldisplayframerate.md)
  The currently configured frame rate on the external display that’s displaying the preview layer.
- [var device: AVCaptureDevice?](avcaptureexternaldisplayconfigurator/device.md)
  The device for which the coordinator configures the preview layer.
- [var previewLayer: CALayer?](avcaptureexternaldisplayconfigurator/previewlayer.md)
  The layer for which the configurator adjusts display properties to match the device’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/isactive)*