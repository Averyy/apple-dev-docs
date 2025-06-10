# AudioMixGroup

**Framework**: RealityKit  
**Kind**: struct

A group that manages the playback properties of multiple playing sounds.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct AudioMixGroup
```

#### Overview

A mix group component manages the playback parameters for a collection of different [`AudioPlaybackController`](audioplaybackcontroller.md) and [`AudioGeneratorController`](audiogeneratorcontroller.md) instances. Properties such as [`gain`](audiomixgroup/gain.md), [`fade(to:duration:)`](audiomixgroup/fade(to:duration:).md), and [`speed`](audiomixgroup/speed.md) are multiplicative with the parameters you set on the controller.

You  associate audio resources to a mix group by setting the `mixGroupName` parameter in the resource’s configuration. For an example, see `AudioFileResource/Configuration-swift.struct/mixGroupName`. Enable a mix group by adding it to an [`AudioMixGroupsComponent`](audiomixgroupscomponent.md) structure on an entity in the scene. The scene where the component belongs limits the scope of the mix group.

```swift
var mixGroup = AudioMixGroup(name: "myMixGroup")
entity.components.set(AudioMixGroupsComponent(mixGroups: [mixGroup]))
```

## Topics

### Initializers
- [init(name: String)](audiomixgroup/init(name:).md)
  Creates a mix group.
### Instance Properties
- [var gain: Audio.Decibel](audiomixgroup/gain.md)
  The overall level for all sounds of an audio mix group in relative decibels.
- [var isMuted: Bool](audiomixgroup/ismuted.md)
  A Boolean value that indicates whether an audio mix group emits any sound.
- [let name: String](audiomixgroup/name.md)
  The name of an audio mix group.
- [var speed: Double](audiomixgroup/speed.md)
  The rate of playback for an audio mix group.
### Instance Methods
- [func fade(to: Audio.Decibel, duration: TimeInterval)](audiomixgroup/fade(to:duration:).md)
  Transitions the gain to a value over a time interval using a linear curve.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct AudioMixGroupsComponent](audiomixgroupscomponent.md)
  A component that provides functionality for controlling the playback of audio you assign to mix groups in a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiomixgroup)*