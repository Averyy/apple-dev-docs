# fullStateForDocument

**Framework**: Audio Toolbox  
**Kind**: property

A persistable snapshot of the audio unit’s properties and parameters, suitable for saving in a user’s document.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var fullStateForDocument: [String : Any]? { get set }
```

#### Discussion

Hosts may use this property to save and restore the state of an audio unit being used. Some state, such as a parameter value, is suitable for saving in a user preset. Other state, such as a synthesizer’s primary tuning setting, could be considered global state suitable for saving in a user document.

Subclasses that do not implement this property interface with the [`fullState`](auaudiounit/fullstate.md) property instead.

This version 3 property is bridged to the version 2 `kAudioUnitProperty_ClassInfoFromDocument` API.

## See Also

- [var fullState: [String : Any]?](auaudiounit/fullstate.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving as a user preset.
- [var factoryPresets: [AUAudioUnitPreset]?](auaudiounit/factorypresets.md)
  A collection of presets provided by the audio unit’s developer.
- [var currentPreset: AUAudioUnitPreset?](auaudiounit/currentpreset.md)
  The audio unit’s last-selected preset.
- [var supportsUserPresets: Bool](auaudiounit/supportsuserpresets.md)
- [var userPresets: [AUAudioUnitPreset]](auaudiounit/userpresets.md)
- [func saveUserPreset(AUAudioUnitPreset) throws](auaudiounit/saveuserpreset(_:).md)
- [func deleteUserPreset(AUAudioUnitPreset) throws](auaudiounit/deleteuserpreset(_:).md)
- [func presetState(for: AUAudioUnitPreset) throws -> [String : Any]](auaudiounit/presetstate(for:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/fullstatefordocument)*