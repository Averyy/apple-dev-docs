# currentPreset

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The audio unit’s last-selected preset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var currentPreset: AUAudioUnitPreset? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, retain, nullable) AUAudioUnitPreset * currentPreset;
```

*macOS*

```objc
@property (atomic, retain, nullable) AUAudioUnitPreset * currentPreset;
```

## Discussion

Hosts can let the user select a preset by setting this property. When getting this property, the preset does not reflect whether parameters may have been modified since it was selected.

This version 3 property is bridged to the version 2 `kAudioUnitProperty_PresentPreset` API.

## See Also

### Managing Presets
- [var fullState: [String : Any]?](./fullstate.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving as a user preset.
- [var fullStateForDocument: [String : Any]?](./fullstatefordocument.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving in a user’s document.
- [var factoryPresets: [AUAudioUnitPreset]?](./factorypresets.md)
  A collection of presets provided by the audio unit’s developer.
- [var supportsUserPresets: Bool](./supportsuserpresets.md)
- [var userPresets: [AUAudioUnitPreset]](./userpresets.md)
- [func saveUserPreset(AUAudioUnitPreset) throws](./saveuserpreset%28_%29.md)
- [func deleteUserPreset(AUAudioUnitPreset) throws](./deleteuserpreset%28_%29.md)
- [func presetState(for: AUAudioUnitPreset) throws -> [String : Any]](./presetstate%28for%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/currentpreset)*