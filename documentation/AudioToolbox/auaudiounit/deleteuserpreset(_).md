# deleteUserPreset(_:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) deleteUserPreset:(AUAudioUnitPreset *) userPreset error:(NSError **) outError;
```

## See Also

### Managing Presets
- [var fullState: [String : Any]?](./fullstate.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving as a user preset.
- [var fullStateForDocument: [String : Any]?](./fullstatefordocument.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving in a user’s document.
- [var factoryPresets: [AUAudioUnitPreset]?](./factorypresets.md)
  A collection of presets provided by the audio unit’s developer.
- [var currentPreset: AUAudioUnitPreset?](./currentpreset.md)
  The audio unit’s last-selected preset.
- [var supportsUserPresets: Bool](./supportsuserpresets.md)
- [var userPresets: [AUAudioUnitPreset]](./userpresets.md)
- [func saveUserPreset(AUAudioUnitPreset) throws](./saveuserpreset%28_%29.md)
- [func presetState(for: AUAudioUnitPreset) throws -> [String : Any]](./presetstate%28for%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/deleteuserpreset(_:))*