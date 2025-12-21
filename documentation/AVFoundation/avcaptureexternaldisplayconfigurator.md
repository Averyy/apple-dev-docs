# AVCaptureExternalDisplayConfigurator

**Framework**: AVFoundation  
**Kind**: class

A configurator class allowing you to configure properties of an external display to match the camera’s active video format.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
class AVCaptureExternalDisplayConfigurator
```

#### Overview

An [`AVCaptureExternalDisplayConfigurator`](avcaptureexternaldisplayconfigurator.md) allows you to configure a connected external display to output a clean feed using a `CALayer`. Using the configurator, you can opt into automatic adjustment of the external display’s color space and / or frame rate to match your device’s capture configuration. These adjustments are only applied to the external display, not to the device.

> **Note**: Not all displays support the same configuration options as the device’s capture formats. Your adjustments to the external display are applied with utmost effort to accurately represent the capture device. When your capture device’s [`activeFormat`](avcapturedevice/activeformat.md) is unavailable on the external display, the configurator automatically chooses the closest available format.

## Topics

### Determining configuration support
- [class var isMatchingFrameRateSupported: Bool](avcaptureexternaldisplayconfigurator/ismatchingframeratesupported.md)
  Whether the external display supports matching frame rate to a capture device.
- [class var isPreferredResolutionSupported: Bool](avcaptureexternaldisplayconfigurator/ispreferredresolutionsupported.md)
  Whether the external display supports configuration to your preferred resolution.
- [class var isBypassingColorSpaceConversionSupported: Bool](avcaptureexternaldisplayconfigurator/isbypassingcolorspaceconversionsupported.md)
  Whether the external display supports bypassing color space conversion.
### Creating an external display configurator
- [init(device: AVCaptureDevice, previewLayer: CALayer, configuration: AVCaptureExternalDisplayConfiguration)](avcaptureexternaldisplayconfigurator/init(device:previewlayer:configuration:).md)
  An external display configurator instance that attempts to synchronize the preview layer configuration with the device capture configuration.
### Inspecting the configurator
- [var activeExternalDisplayFrameRate: Double](avcaptureexternaldisplayconfigurator/activeexternaldisplayframerate.md)
  The currently configured frame rate on the external display that’s displaying the preview layer.
- [var device: AVCaptureDevice?](avcaptureexternaldisplayconfigurator/device.md)
  The device for which the coordinator configures the preview layer.
- [var isActive: Bool](avcaptureexternaldisplayconfigurator/isactive.md)
  This property tells you whether the configurator is actively configuring the external display.
- [var previewLayer: CALayer?](avcaptureexternaldisplayconfigurator/previewlayer.md)
  The layer for which the configurator adjusts display properties to match the device’s state.
### Stopping configuration
- [func stop()](avcaptureexternaldisplayconfigurator/stop.md)
  Forces the external display configurator to asynchronously stop configuring the external display.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVCaptureExternalDisplayConfiguration](avcaptureexternaldisplayconfiguration.md)
  A class you use to specify a configuration to your external display configurator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator)*