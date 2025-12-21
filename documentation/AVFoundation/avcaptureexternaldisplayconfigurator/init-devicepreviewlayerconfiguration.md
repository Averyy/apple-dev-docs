# init(device:previewLayer:configuration:)

**Framework**: AVFoundation  
**Kind**: init

An external display configurator instance that attempts to synchronize the preview layer configuration with the device capture configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
init(device: AVCaptureDevice, previewLayer: CALayer, configuration: AVCaptureExternalDisplayConfiguration)
```

#### Return Value

An [`AVCaptureExternalDisplayConfigurator`](avcaptureexternaldisplayconfigurator.md) instance.

#### Discussion

An [`AVCaptureExternalDisplayConfigurator`](avcaptureexternaldisplayconfigurator.md) is only applicable to external displays. It determines which properties to configure on the external display based on your provided configuration (see [`AVCaptureExternalDisplayConfiguration`](avcaptureexternaldisplayconfiguration.md)). The configurator observes changes to your camera’‘s configuration, and when changes are observed, it modifies the external display’s properties to match.

If multiple configurators are linked to the same external display ,the last one created becomes the active configurator for the external display (see [`isActive`](avcaptureexternaldisplayconfigurator/isactive.md)).

> ❗ **Important**: An `NSInvalidArgumentException` is thrown if any of the [`AVCaptureExternalDisplayConfiguration`](avcaptureexternaldisplayconfiguration.md) options are not supported.

## Parameters

- `device`: The device for which to monitor the configuration.
- `previewLayer`: The layer that is being used on an external display for displaying the camera preview.
- `configuration`: A configuration specifying which aspects of the camera’s active format to monitor and configure on the external display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/init(device:previewlayer:configuration:))*