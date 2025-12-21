# AVCaptureExternalDisplayConfiguration

**Framework**: AVFoundation  
**Kind**: class

A class you use to specify a configuration to your external display configurator.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
class AVCaptureExternalDisplayConfiguration
```

#### Overview

Using an [`AVCaptureExternalDisplayConfiguration`](avcaptureexternaldisplayconfiguration.md), you direct your [`AVCaptureExternalDisplayConfigurator`](avcaptureexternaldisplayconfigurator.md) how to configure an external display to match your device’s active video format.

## Topics

### Modifying the configuration
- [var bypassColorSpaceConversion: Bool](avcaptureexternaldisplayconfiguration/bypasscolorspaceconversion.md)
  A property indicating whether the color space of the configurator’s preview layer should be preserved on the output display by avoiding color space conversions.
- [var preferredResolution: CMVideoDimensions](avcaptureexternaldisplayconfiguration/preferredresolution.md)
  Your preferred external display resolution.
- [var shouldMatchFrameRate: Bool](avcaptureexternaldisplayconfiguration/shouldmatchframerate.md)
  A property indicating whether the frame rate of the external display should be configured to match the camera’s frame rate.

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

- [class AVCaptureExternalDisplayConfigurator](avcaptureexternaldisplayconfigurator.md)
  A configurator class allowing you to configure properties of an external display to match the camera’s active video format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfiguration)*