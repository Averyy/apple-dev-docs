# deleteUserPreset(_:)

**Framework**: Audio Toolbox  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func deleteUserPreset(_ userPreset: AUAudioUnitPreset) throws
```

## See Also

- [var fullState: [String : Any]?](auaudiounit/fullstate.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving as a user preset.
- [var fullStateForDocument: [String : Any]?](auaudiounit/fullstatefordocument.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving in a user’s document.
- [var factoryPresets: [AUAudioUnitPreset]?](auaudiounit/factorypresets.md)
  A collection of presets provided by the audio unit’s developer.
- [var currentPreset: AUAudioUnitPreset?](auaudiounit/currentpreset.md)
  The audio unit’s last-selected preset.
- [var supportsUserPresets: Bool](auaudiounit/supportsuserpresets.md)
- [var userPresets: [AUAudioUnitPreset]](auaudiounit/userpresets.md)
- [func saveUserPreset(AUAudioUnitPreset) throws](auaudiounit/saveuserpreset(_:).md)
- [func presetState(for: AUAudioUnitPreset) throws -> [String : Any]](auaudiounit/presetstate(for:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/deleteuserpreset(_:))*