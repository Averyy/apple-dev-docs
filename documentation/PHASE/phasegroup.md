# PHASEGroup

**Framework**: PHASE  
**Kind**: class

A container that shares audio parameters with a collection of sounds.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEGroup
```

#### Overview

With all the sounds it contains, a group shares settings like gain, playback rate, mute, and solo. Groups are nonhierarchical and don’t overlap — that is, each sound event associates with only one group.

##### Apply Group Settings to Sounds

You can apply settings to the sounds a group contains. For instance, an app can share volume settings with various sound effects and dialogue audio groups. The following example creates a group for background audio, such as environmental sound layers played with ambient music. By interpolating the group’s gain setting, the audio fade applies to every sound in the group.

## Topics

### Creating a Group
- [init(identifier: String)](phasegroup/init(identifier:).md)
  Creates a group with a unique name.
### Identifying the Group
- [var identifier: String](phasegroup/identifier.md)
  A unique name for the group.
### Defining the Group
- [func register(engine: PHASEEngine)](phasegroup/register(engine:).md)
  Adds the group to the engine’s dictionary.
- [func unregisterFromEngine()](phasegroup/unregisterfromengine.md)
  Removes the group from the engine’s dictionary.
### Conrolling Loudness
- [var gain: Double](phasegroup/gain.md)
  Modifies the volume of the group’s sounds.
- [func fadeGain(gain: Double, duration: Double, curveType: PHASECurveType)](phasegroup/fadegain(gain:duration:curvetype:).md)
  Adjusts the volume of the sounds in a group gradually.
### Adjusting Playback Speed
- [var rate: Double](phasegroup/rate.md)
  The group’s playback speed.
- [func fadeRate(rate: Double, duration: Double, curveType: PHASECurveType)](phasegroup/faderate(rate:duration:curvetype:).md)
  Adjusts the playback speed of the sounds in a group gradually.
### Silencing Sounds
- [func mute()](phasegroup/mute.md)
  Silences the group.
- [func unmute()](phasegroup/unmute.md)
  Restores the group’s volume.
- [var isMuted: Bool](phasegroup/ismuted.md)
  A Boolean value that indicates whether the app silences the group.
- [func solo()](phasegroup/solo.md)
  Silences all other groups.
- [func unsolo()](phasegroup/unsolo.md)
  Restores the other groups’ volume.
- [var isSoloed: Bool](phasegroup/issoloed.md)
  A Boolean value that indicates whether the app silences all groups other than this group.

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

- [class PHASEGroupPreset](phasegrouppreset.md)
  A collection of settings for groups.
- [class PHASEGroupPresetSetting](phasegrouppresetsetting.md)
  Settings for group presets.
- [class PHASEDucker](phaseducker.md)
  An object that manages competing sounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegroup)*