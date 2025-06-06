# PHASEDucker

**Framework**: PHASE  
**Kind**: class

An object that manages competing sounds.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEDucker
```

#### Overview

When a sound plays in any of the source groups, this class lowers the volume of all the target groups so the listener hears the source sound more clearly. You set the source and target using [`PHASEGroup`](phasegroup.md) objects; see [`sourceGroups`](phaseducker/sourcegroups.md) and [`targetGroups`](phaseducker/targetgroups.md).

##### Lower Background Music During a Monologue

When an app plays a monologue, the background music may need to lower, or , to enhance the clarity of the vocals. The following code demonstrates a ducker that configures a group for background music, and another group for the vocals.

When an app sets up the ducking configuration in advance, PHASE automatically lowers the background music at runtime when the vocals play.

## Topics

### Creating a Ducker
- [init(engine: PHASEEngine, sourceGroups: Set<PHASEGroup>, targetGroups: Set<PHASEGroup>, gain: Double, attackTime: Double, releaseTime: Double, attackCurve: PHASECurveType, releaseCurve: PHASECurveType)](phaseducker/init(engine:sourcegroups:targetgroups:gain:attacktime:releasetime:attackcurve:releasecurve:).md)
  Creates an object that manages competing sounds.
### Specifying Sounds
- [var sourceGroups: Set<PHASEGroup>](phaseducker/sourcegroups.md)
  The sounds that determine volume reduction.
- [var targetGroups: Set<PHASEGroup>](phaseducker/targetgroups.md)
  The sounds that reduce in volume.
### Configuring Volume Reduction
- [var gain: Double](phaseducker/gain.md)
  The amount of volume reduction.
- [var identifier: String](phaseducker/identifier.md)
  A unique value for the ducker.
- [var isActive: Bool](phaseducker/isactive.md)
  A Boolean value that determines whether the ducker reduces sound.
- [var attackTime: Double](phaseducker/attacktime.md)
  The amount of time for sound reduction to reach maximum strength.
- [var attackCurve: PHASECurveType](phaseducker/attackcurve.md)
  A mathematical curve that shapes transition progress as sound reduction begins.
- [var releaseTime: Double](phaseducker/releasetime.md)
  The amount of time to transition from maximum sound reduction to no reduction.
- [var releaseCurve: PHASECurveType](phaseducker/releasecurve.md)
  A mathematical curve that shapes transition progress as sound reduction ends.
### Altering Sound
- [func activate()](phaseducker/activate.md)
  Instructs the ducker to begin altering sound.
- [func deactivate()](phaseducker/deactivate.md)
  Stops the ducker from altering sound.

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
- [class PHASEGroupPresetSetting](phasegrouppresetsetting.md)
  Settings for group presets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseducker)*