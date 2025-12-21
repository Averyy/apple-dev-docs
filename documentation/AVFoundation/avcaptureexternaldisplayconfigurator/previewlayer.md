# previewLayer

**Framework**: AVFoundation  
**Kind**: property

The layer for which the configurator adjusts display properties to match the device’s state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
weak var previewLayer: CALayer? { get }
```

#### Discussion

The value of this property is the `CALayer` instance that you provided when instantiating the configurator. You may specify either an [`AVCaptureVideoPreviewLayer`](avcapturevideopreviewlayer.md) or another `CALayer` instance that displays a camera’s video preview. [`AVCaptureExternalDisplayConfigurator`](avcaptureexternaldisplayconfigurator.md)holds a weak reference to the layer. If the layer is released, this property returns `nil`.

## See Also

- [var activeExternalDisplayFrameRate: Double](avcaptureexternaldisplayconfigurator/activeexternaldisplayframerate.md)
  The currently configured frame rate on the external display that’s displaying the preview layer.
- [var device: AVCaptureDevice?](avcaptureexternaldisplayconfigurator/device.md)
  The device for which the coordinator configures the preview layer.
- [var isActive: Bool](avcaptureexternaldisplayconfigurator/isactive.md)
  This property tells you whether the configurator is actively configuring the external display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/previewlayer)*