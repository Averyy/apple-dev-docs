# PHASEGroupPresetSetting

**Framework**: PHASE  
**Kind**: class

Settings for group presets.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEGroupPresetSetting
```

#### Overview

This class defines playback speed and volume rates of change that an app can apply to groups. To create a group preset setting, instantiate an object of this type and pass it to the `settings` parameter of [`init(engine:settings:timeToTarget:timeToReset:)`](phasegrouppreset/init(engine:settings:timetotarget:timetoreset:).md).

For an example of preset settings, see [`PHASEGroupPreset`](phasegrouppreset.md).

## Topics

### Creating a Setting
- [init(gain: Double, rate: Double, gainCurveType: PHASECurveType, rateCurveType: PHASECurveType)](phasegrouppresetsetting/init(gain:rate:gaincurvetype:ratecurvetype:).md)
  Creates a group preset setting.
### Setting Loudness
- [var gain: Double](phasegrouppresetsetting/gain.md)
  The volume of audio playback.
- [var gainCurveType: PHASECurveType](phasegrouppresetsetting/gaincurvetype.md)
  A rate of change for the setting’s volume.
### Setting Playback Speed
- [var rate: Double](phasegrouppresetsetting/rate.md)
  The playback speed for audio.
- [var rateCurveType: PHASECurveType](phasegrouppresetsetting/ratecurvetype.md)
  A rate of change for the setting’s playback speed.

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
- [class PHASEGroupPreset](phasegrouppreset.md)
  A collection of settings for groups.
- [class PHASEDucker](phaseducker.md)
  An object that manages competing sounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppresetsetting)*