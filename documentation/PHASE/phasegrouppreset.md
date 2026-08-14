# PHASEGroupPreset

**Framework**: PHASE  
**Kind**: class

A collection of settings for groups.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEGroupPreset
```

#### Overview

Group presets pair groups with audio settings that your app can apply to specific sounds at a particular time in your app’s life cycle. This class enables many predefined group settings to take effect all at once.

##### Toggle Between Group Presets

The group preset’s utility materializes when you switch between settings. The following example creates two group presets: one for an in-game experience and another for a menu that displays when the user pauses the app.

**Swift**:

```swift
// Create sound group objects.
let bgmGroup = PHASEGroup(identifier:"backgroundMusicGroup")
let voGroup = PHASEGroup(identifier:"voiceOverGroup")
let menuGroup = PHASEGroup(identifier:"menuSoundsGroup")

// Register the groups with the engine.
bgmGroup.register(engine: myEngine)
voGroup.register(engine: myEngine)
menuGroup.register(engine: myEngine)
        
// Create settings for the groups.
let groupSettingFullVolume = PHASEGroupPresetSetting(gain: 1.0, rate: 1.0, gainCurveType: .linear, rateCurveType: .linear)
let groupSettingZeroVolume = PHASEGroupPresetSetting(gain: 0.0, rate: 1.0, gainCurveType: .linear, rateCurveType: .linear)
        
// Create a dictionary for the `settings` argument of the group preset initializer.
var pauseMenuDictionary: [String : PHASEGroupPresetSetting] = [:]
        
// Enable volume only for menu group sounds.
pauseMenuDictionary[menuGroup.identifier] = groupSettingFullVolume
pauseMenuDictionary[bgmGroup.identifier] = groupSettingZeroVolume
pauseMenuDictionary[voGroup.identifier] = groupSettingZeroVolume
let pauseMenuPreset = PHASEGroupPreset(engine: myEngine, settings: pauseMenuDictionary, timeToTarget: 1.0, timeToReset: 1.0)
        
// Create a settings dictionary for the in-game experience.
var inGameDictionary: [String : PHASEGroupPresetSetting] = [:]

// Enable volume only for in-game sounds.
inGameDictionary[menuGroup.identifier] = groupSettingZeroVolume
inGameDictionary[bgmGroup.identifier] = groupSettingFullVolume
inGameDictionary[voGroup.identifier] = groupSettingFullVolume
let inGamePreset = PHASEGroupPreset(engine: myEngine, settings: inGameDictionary, timeToTarget: 1.0, timeToReset: 1.0)
        
// Activate the pause menu preset when the user pauses the app.
pauseMenuPreset.activate()

// Activate the in-game preset when the user resumes the app.
inGamePreset.activate()

// Clear the current preset by deactivating it.
if let groupPreset = myEngine.activeGroupPreset {
    groupPreset.deactivate()
}
```

**Objective-C**:

```objc
// Create groups for the sounds. 
PHASEGroup* bgmGroup = [[PHASEGroup alloc] initWithEngine:_objects->mEngine uid:@"backgroundMusicGroup"];
PHASEGroup* voGroup = [[PHASEGroup alloc] initWithEngine:_objects->mEngine uid:@"voiceOverGroup"];
PHASEGroup* menuGroup = [[PHASEGroup alloc] initWithEngine:_objects->mEngine uid:@"menuSoundsGroup"];

// Create settings for the groups.
PHASEGroupPresetSetting* groupSettingFullVolume = [PHASEGroupPresetSetting alloc] initWithGain:1
    rate:1 gainCurveType:PHASECurveTypeLinear rateCurveType:PHASECurveTypeLinear];
                                                
PHASEGroupPresetSetting* groupSettingZeroVolume = [PHASEGroupPresetSetting alloc] initWithGain:0
    rate:1 gainCurveType:PHASECurveTypeLinear rateCurveType:PHASECurveTypeLinear];

// Create a dictionary for the `settings` argument of the group preset initializer.
NSMutableDictionary<PHASEGroup*, PHASEGroupPresetSetting*> pauseMenuDictionary;

// Enable volume only for menu group sounds.
[pauseMenuDictionary setObject:groupSettingFullVolume forKey:menuGroup]
[pauseMenuDictionary setObject:groupSettingZeroVolume forKey:bgmGroup]
[pauseMenuDictionary setObject:groupSettingZeroVolume forKey:voGroup]
PHASEGroupPreset* pauseMenuPreset = [[PHASEGroupPreset alloc] initWithEngine:myPHASEEngine
    settings:pauseMenuDictionary timeToTarget:1 timeToReset:1];

// Create a settings dictionary for the in-game experience.
NSMutableDictionary<PHASEGroup*, PHASEGroupPresetSetting*> inGameDictionary;

// Enable volume only for in-game sounds.
[inGameDictionary setObject:groupSettingZeroVolume forKey:menuGroup]
[inGameDictionary setObject:groupSettingFullVolume forKey:bgmGroup]
[inGameDictionary setObject:groupSettingFullVolume forKey:voGroup]
PHASEGroupPreset* inGamePreset = [[PHASEGroupPreset alloc] initWithEngine:myPHASEEngine
    settings:inGameDictionary timeToTarget:1 timeToReset:1];

// Activate the pause menu preset when the user pauses the app.
[pauseMenuPreset activate];

// Activate the in-game preset when the user resumes the app. 
[inGamePreset activate];

// Clear the current preset by deactivating it.
[myPHASEEngine.activeGroupPreset deactivate]

```

## Topics

### Creating a Group Preset
- [init(engine: PHASEEngine, settings: [String : PHASEGroupPresetSetting], timeToTarget: Double, timeToReset: Double)](phasegrouppreset/init(engine:settings:timetotarget:timetoreset:).md)
  Creates a group preset with the designated engine, settings, and fade parameters.
### Applying Settings
- [var settings: [String : PHASEGroupPresetSetting]](phasegrouppreset/settings.md)
  A dictionary with preset setting values and group objects as keys.
### Fading Between Settings
- [var timeToTarget: Double](phasegrouppreset/timetotarget.md)
  A duration in which the engine fades the settings from their original value to their new value.
- [var timeToReset: Double](phasegrouppreset/timetoreset.md)
  A duration in which the framework restores the group’s original state.
### Activating a Group Preset
- [func activate()](phasegrouppreset/activate.md)
  Applies settings to the designated groups.
- [func activate(timeToTargetOverride: Double)](phasegrouppreset/activate(timetotargetoverride:).md)
  Applies settings with an overriden fade duration.
### Deactivating a Group Preset
- [func deactivate()](phasegrouppreset/deactivate.md)
  Reverts settings for the preset’s groups.
- [func deactivate(timeToResetOverride: Double)](phasegrouppreset/deactivate(timetoresetoverride:).md)
  Reverts settings for the preset’s groups using a timed adjustment.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class PHASEGroup](phasegroup.md)
  A container that shares audio parameters with a collection of sounds.
- [class PHASEGroupPresetSetting](phasegrouppresetsetting.md)
  Settings for group presets.
- [class PHASEDucker](phaseducker.md)
  An object that manages competing sounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppreset)*