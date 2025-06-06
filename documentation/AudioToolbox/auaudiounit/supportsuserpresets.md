# supportsUserPresets

**Framework**: Audio Toolbox  
**Kind**: property

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var supportsUserPresets: Bool { get }
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
- [var userPresets: [AUAudioUnitPreset]](auaudiounit/userpresets.md)
- [func saveUserPreset(AUAudioUnitPreset) throws](auaudiounit/saveuserpreset(_:).md)
- [func deleteUserPreset(AUAudioUnitPreset) throws](auaudiounit/deleteuserpreset(_:).md)
- [func presetState(for: AUAudioUnitPreset) throws -> [String : Any]](auaudiounit/presetstate(for:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/supportsuserpresets)*