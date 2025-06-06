# init(preset:)

**Framework**: AVFoundation  
**Kind**: init

Creates an output setting assistant with a preset configuration.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(preset presetIdentifier: AVOutputSettingsPreset)
```

#### Discussion

- presetIdentifier: A preset configuration for the object.

## See Also

- [struct AVOutputSettingsPreset](avoutputsettingspreset.md)
  A structure that defines preset configurations for an output settings assistant.
- [class func availableOutputSettingsPresets() -> [AVOutputSettingsPreset]](avoutputsettingsassistant/availableoutputsettingspresets.md)
  Returns an array of preset values to use to initialize an output settings assistant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/init(preset:))*