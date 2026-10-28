# PHASEGroupPresetSetting

**Framework**: PHASE  
**Kind**: class  
**Role**: Class

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

```objc
@interface PHASEGroupPresetSetting : NSObject
```

## Overview

This class defines playback speed and volume rates of change that an app can apply to groups. To create a group preset setting, instantiate an object of this type and pass it to the `settings` parameter of [`init(engine:settings:timeToTarget:timeToReset:)`](./phasegrouppreset/init%28engine,settings,timetotarget,timetoreset%29.md).

For an example of preset settings, see [`PHASEGroupPreset`](./phasegrouppreset.md).

## Topics

### Creating a Setting
- [init(gain: Double, rate: Double, gainCurveType: PHASECurveType, rateCurveType: PHASECurveType)](./phasegrouppresetsetting/init%28gain,rate,gaincurvetype,ratecurvetype%29.md)
  Creates a group preset setting.
### Setting Loudness
- [var gain: Double](./phasegrouppresetsetting/gain.md)
  The volume of audio playback.
- [var gainCurveType: PHASECurveType](./phasegrouppresetsetting/gaincurvetype.md)
  A rate of change for the setting’s volume.
### Setting Playback Speed
- [var rate: Double](./phasegrouppresetsetting/rate.md)
  The playback speed for audio.
- [var rateCurveType: PHASECurveType](./phasegrouppresetsetting/ratecurvetype.md)
  A rate of change for the setting’s playback speed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Sound Grouping and Management
- [class PHASEGroup](./phasegroup.md)
  A container that shares audio parameters with a collection of sounds.
- [class PHASEGroupPreset](./phasegrouppreset.md)
  A collection of settings for groups.
- [class PHASEDucker](./phaseducker.md)
  An object that manages competing sounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppresetsetting)*