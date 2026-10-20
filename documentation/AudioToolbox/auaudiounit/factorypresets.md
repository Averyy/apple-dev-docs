# factoryPresets

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

A collection of presets provided by the audio unit’s developer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var factoryPresets: [AUAudioUnitPreset]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<AUAudioUnitPreset *> * factoryPresets;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<AUAudioUnitPreset *> * factoryPresets;
```

#### Discussion

A preset provides audio unit users with an easily-selectable, fine-tuned set of parameters defined by the developer.

This version 3 property is bridged to the version 2 `kAudioUnitProperty_FactoryPresets` API.

## See Also

### Managing Presets
- [var fullState: [String : Any]?](./fullstate.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving as a user preset.
- [var fullStateForDocument: [String : Any]?](./fullstatefordocument.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving in a user’s document.
- [var currentPreset: AUAudioUnitPreset?](./currentpreset.md)
  The audio unit’s last-selected preset.
- [var supportsUserPresets: Bool](./supportsuserpresets.md)
- [var userPresets: [AUAudioUnitPreset]](./userpresets.md)
- [func saveUserPreset(AUAudioUnitPreset) throws](./saveuserpreset%28_%29.md)
- [func deleteUserPreset(AUAudioUnitPreset) throws](./deleteuserpreset%28_%29.md)
- [func presetState(for: AUAudioUnitPreset) throws -> [String : Any]](./presetstate%28for%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/factorypresets)*