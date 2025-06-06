# currentPreset

**Framework**: Audio Toolbox  
**Kind**: property

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

#### Discussion

Hosts can let the user select a preset by setting this property. When getting this property, the preset does not reflect whether parameters may have been modified since it was selected.

This version 3 property is bridged to the version 2 `kAudioUnitProperty_PresentPreset` API.

## See Also

- [var fullState: [String : Any]?](auaudiounit/fullstate.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving as a user preset.
- [var fullStateForDocument: [String : Any]?](auaudiounit/fullstatefordocument.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving in a user’s document.
- [var factoryPresets: [AUAudioUnitPreset]?](auaudiounit/factorypresets.md)
  A collection of presets provided by the audio unit’s developer.
- [var supportsUserPresets: Bool](auaudiounit/supportsuserpresets.md)
- [var userPresets: [AUAudioUnitPreset]](auaudiounit/userpresets.md)
- [func saveUserPreset(AUAudioUnitPreset) throws](auaudiounit/saveuserpreset(_:).md)
- [func deleteUserPreset(AUAudioUnitPreset) throws](auaudiounit/deleteuserpreset(_:).md)
- [func presetState(for: AUAudioUnitPreset) throws -> [String : Any]](auaudiounit/presetstate(for:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/currentpreset)*