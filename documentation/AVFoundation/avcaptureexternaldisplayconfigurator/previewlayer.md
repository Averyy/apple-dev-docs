# previewLayer

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, weak, readonly, nullable) CALayer * previewLayer;
```

#### Discussion

The value of this property is the `CALayer` instance that you provided when instantiating the configurator. You may specify either an [`AVCaptureVideoPreviewLayer`](../avcapturevideopreviewlayer.md) or another `CALayer` instance that displays a camera’s video preview. [`AVCaptureExternalDisplayConfigurator`](../avcaptureexternaldisplayconfigurator.md)holds a weak reference to the layer. If the layer is released, this property returns `nil`.

## See Also

### Inspecting the configurator
- [var activeExternalDisplayFrameRate: Double](./activeexternaldisplayframerate.md)
  The currently configured frame rate on the external display that’s displaying the preview layer.
- [var device: AVCaptureDevice?](./device.md)
  The device for which the coordinator configures the preview layer.
- [var isActive: Bool](./isactive.md)
  This property tells you whether the configurator is actively configuring the external display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/previewlayer)*