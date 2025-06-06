# AVOutputSettingsPreset

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines preset configurations for an output settings assistant.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct AVOutputSettingsPreset
```

## Topics

### Presets
- [static let preset3840x2160: AVOutputSettingsPreset](avoutputsettingspreset/preset3840x2160.md)
  A preset for H.264 video at 3840 by 2160 pixels.
- [static let preset1920x1080: AVOutputSettingsPreset](avoutputsettingspreset/preset1920x1080.md)
  A preset for H.264 video at 1920 by 1080 pixels.
- [static let preset1280x720: AVOutputSettingsPreset](avoutputsettingspreset/preset1280x720.md)
  A preset for H.264 video at 1280 by 720 pixels.
- [static let preset960x540: AVOutputSettingsPreset](avoutputsettingspreset/preset960x540.md)
  A preset for H.264 video at 960 by 540 pixels.
- [static let preset640x480: AVOutputSettingsPreset](avoutputsettingspreset/preset640x480.md)
  A preset for H.264 video at 640 by 480 pixels.
- [static let hevc7680x4320: AVOutputSettingsPreset](avoutputsettingspreset/hevc7680x4320.md)
  A preset for HEVC video at 7680 by 4320 pixels.
- [static let hevc3840x2160: AVOutputSettingsPreset](avoutputsettingspreset/hevc3840x2160.md)
  A preset for HEVC video at 3840 by 2160 pixels.
- [static let hevc3840x2160WithAlpha: AVOutputSettingsPreset](avoutputsettingspreset/hevc3840x2160withalpha.md)
  A preset for HEVC with Alpha video at 3840 by 2160 pixels.
- [static let hevc1920x1080: AVOutputSettingsPreset](avoutputsettingspreset/hevc1920x1080.md)
  A preset for HEVC video at 1920 by 1080 pixels.
- [static let hevc1920x1080WithAlpha: AVOutputSettingsPreset](avoutputsettingspreset/hevc1920x1080withalpha.md)
  A preset for HEVC with Alpha video at 1920 by 1080 pixels.
- [static let mvhevc1440x1440: AVOutputSettingsPreset](avoutputsettingspreset/mvhevc1440x1440.md)
  A preset for MV-HEVC video at 1440 by 1440 pixels.
- [static let mvhevc960x960: AVOutputSettingsPreset](avoutputsettingspreset/mvhevc960x960.md)
  A preset for MV-HEVC video at 960 by 960 pixels.
### Initializers
- [init(rawValue: String)](avoutputsettingspreset/init(rawvalue:).md)
  Creates a preset with a string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [convenience init?(preset: AVOutputSettingsPreset)](avoutputsettingsassistant/init(preset:).md)
  Creates an output setting assistant with a preset configuration.
- [class func availableOutputSettingsPresets() -> [AVOutputSettingsPreset]](avoutputsettingsassistant/availableoutputsettingspresets.md)
  Returns an array of preset values to use to initialize an output settings assistant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avoutputsettingspreset)*