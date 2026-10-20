# availableOutputSettingsPresets()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns an array of preset values to use to initialize an output settings assistant.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func availableOutputSettingsPresets() -> [AVOutputSettingsPreset]
```

```objc
+ (NSArray<NSString *> *) availableOutputSettingsPresets;
```

#### Return Value

An array of available output settings presets.

## See Also

### Creating an assistant
- [convenience init?(preset: AVOutputSettingsPreset)](./init%28preset%29.md)
  Creates an output setting assistant with a preset configuration.
- [struct AVOutputSettingsPreset](../avoutputsettingspreset.md)
  A structure that defines preset configurations for an output settings assistant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/availableoutputsettingspresets())*