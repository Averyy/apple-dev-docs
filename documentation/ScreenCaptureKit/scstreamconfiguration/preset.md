# SCStreamConfiguration.Preset

**Framework**: ScreenCaptureKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 15.0+

## Declaration

```swift
enum Preset
```

```c
enum SCStreamConfigurationPreset : NSInteger;
```

## Overview

Client can use SCStreamConfigurationPreset to create SCStreamConfiguration with suggested values of properties for various use cases

## Topics

### Enumeration Cases
- [SCStreamConfiguration.Preset.captureHDRRecordingPreservedSDRHDR10](./preset/capturehdrrecordingpreservedsdrhdr10.md)
- [SCStreamConfiguration.Preset.captureHDRScreenshotCanonicalDisplay](./preset/capturehdrscreenshotcanonicaldisplay.md)
- [SCStreamConfiguration.Preset.captureHDRScreenshotLocalDisplay](./preset/capturehdrscreenshotlocaldisplay.md)
- [SCStreamConfiguration.Preset.captureHDRStreamCanonicalDisplay](./preset/capturehdrstreamcanonicaldisplay.md)
- [SCStreamConfiguration.Preset.captureHDRStreamLocalDisplay](./preset/capturehdrstreamlocaldisplay.md)
### Initializers
- [init?(rawValue: Int)](./preset/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [enum SCCaptureDynamicRange](../sccapturedynamicrange.md)
  Specifies whether the captured screen output is standard or high dynamic range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/preset)*