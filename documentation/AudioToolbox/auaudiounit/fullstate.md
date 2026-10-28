# fullState

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

A persistable snapshot of the audio unit’s properties and parameters, suitable for saving as a user preset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var fullState: [String : Any]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, nullable) NSDictionary<NSString *,id> * fullState;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSDictionary<NSString *,id> * fullState;
```

## Discussion

Hosts may use this property to save and restore the state of an audio unit being used in a user preset or document. The audio unit should not persist transitory properties such as stream formats, but should save and restore all other properties.

The base class implementation of this property saves the values of all parameters currently in the parameter tree. A subclass which dynamically produces multiple variants of the parameter tree needs to be aware that the serialization method does a depth-first preorder traversal of the tree.

This version 3 property is bridged to the version 2 `kAudioUnitProperty_ClassInfo` API.

## See Also

### Managing Presets
- [var fullStateForDocument: [String : Any]?](./fullstatefordocument.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving in a user’s document.
- [var factoryPresets: [AUAudioUnitPreset]?](./factorypresets.md)
  A collection of presets provided by the audio unit’s developer.
- [var currentPreset: AUAudioUnitPreset?](./currentpreset.md)
  The audio unit’s last-selected preset.
- [var supportsUserPresets: Bool](./supportsuserpresets.md)
- [var userPresets: [AUAudioUnitPreset]](./userpresets.md)
- [func saveUserPreset(AUAudioUnitPreset) throws](./saveuserpreset%28_%29.md)
- [func deleteUserPreset(AUAudioUnitPreset) throws](./deleteuserpreset%28_%29.md)
- [func presetState(for: AUAudioUnitPreset) throws -> [String : Any]](./presetstate%28for%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/fullstate)*