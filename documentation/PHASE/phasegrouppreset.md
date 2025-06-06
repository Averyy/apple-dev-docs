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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASEGroup](phasegroup.md)
  A container that shares audio parameters with a collection of sounds.
- [class PHASEGroupPresetSetting](phasegrouppresetsetting.md)
  Settings for group presets.
- [class PHASEDucker](phaseducker.md)
  An object that manages competing sounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppreset)*