# AudioMixGroupsComponent

**Framework**: RealityKit  
**Kind**: struct

A component that provides functionality for controlling the playback of audio you assign to mix groups in a scene.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct AudioMixGroupsComponent
```

#### Overview

When defining an [`AudioMixGroup`](audiomixgroup.md) for a scene in the Audio Mixer section of Reality Composer Pro, this component exists on the first descendant [`Entity`](entity.md) in the scene at runtime.

A common use case for `AudioMixGroupsComponent` is to simultaneously control the playback volume of every [`AudioResource`](audioresource.md) in an `AudioMixGroup`, such as the sound effects in a scene. The following example sets the playback volume of every `AudioResource` in the `AudioMixGroup` named SFX:

```swift
let sceneEntity = Entity(named: "ContainsAudio", in: realityKitContentBundle)

// AudioMixGroupsComponent exists on the first descendant Entity in a scene.
var audioMixGroupsEntity = sceneEntity.children[0]

// If no audio mix groups are configured for this scene in Reality Composer Pro, this component won't exist.
guard var audioMixGroupsComponent = audioMixGroupsEntity.components[AudioMixGroupsComponent.self], 
    var sfxGroup = audioMixGroupsComponent.mixGroup(named: "SFX") else {
    return
}

// This code remaps a percent value between 0 and 100 to a decibel value between -60.0 and 0.0.
// Because -60.0 dB is near the low-end of human hearing ability, this is a good value to use in this example.
let volumePercent: Float = 50
let decibels = Audio.Decibel(-40.0 + (20 * log10(volumePercent)))

// Control the playback volume with the gain property on an AudioMixGroup.
sfxGroup.gain = decibels

audioMixGroupsComponent.set(sfxGroup)
audioMixGroupsEntity.components.set(audioMixGroupsComponent)
```

To completely silence an `AudioMixGroup`, use the [`isMuted`](audiomixgroup/ismuted.md) property.

Use [`fade(to:duration:)`](audiomixgroup/fade(to:duration:).md) to fade the volume of an `AudioMixGroup` over time.

## Topics

### Initializers
- [init(mixGroups: [AudioMixGroup])](audiomixgroupscomponent/init(mixgroups:).md)
  Initializes an `AudioMixGroupsComponent`.
### Instance Methods
- [func mixGroup(named: String) -> AudioMixGroup?](audiomixgroupscomponent/mixgroup(named:).md)
  Returns the audio mix group with the given name, if it exists.
- [func remove(named: String)](audiomixgroupscomponent/remove(named:).md)
  Removes the audio mix group with the given name, if it exists, from the component.
- [func set(AudioMixGroup)](audiomixgroupscomponent/set(_:).md)
  Adds the given `AudioMixGroup` to the component.
### Default Implementations
- [Component Implementations](audiomixgroupscomponent/component-implementations.md)
- [Equatable Implementations](audiomixgroupscomponent/equatable-implementations.md)
- [Hashable Implementations](audiomixgroupscomponent/hashable-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct AudioMixGroup](audiomixgroup.md)
  A group that manages the playback properties of multiple playing sounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiomixgroupscomponent)*