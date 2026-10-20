# device

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The device for which the coordinator configures the preview layer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
weak var device: AVCaptureDevice? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) AVCaptureDevice * device;
```

#### Discussion

The value of this property is the [`AVCaptureDevice`](../avcapturedevice.md) instance you provided when instantiating the configurator. [`AVCaptureExternalDisplayConfigurator`](../avcaptureexternaldisplayconfigurator.md) holds a weak reference to the device. If the device is released, this property returns `nil`.

## See Also

### Inspecting the configurator
- [var activeExternalDisplayFrameRate: Double](./activeexternaldisplayframerate.md)
  The currently configured frame rate on the external display that’s displaying the preview layer.
- [var isActive: Bool](./isactive.md)
  This property tells you whether the configurator is actively configuring the external display.
- [var previewLayer: CALayer?](./previewlayer.md)
  The layer for which the configurator adjusts display properties to match the device’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/device)*