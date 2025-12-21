# ChannelAudioComponent

**Framework**: RealityKit  
**Kind**: struct

A component that configures channel-based rendering of sounds from an entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct ChannelAudioComponent
```

#### Overview

Channel audio sources route the audio resource’s channels directly to the device’s output without any spatialization or reverberation applied. Neither the position nor orientation of the entity is taken into consideration for channel rendering. For example, the left channel is heard from the left, and the right channel is heard from the right, regardless of where the user is oriented.

The channels of multichannel audio resources are panned according to their channel layout, including rear channels.

```swift
let entity = Entity()
let resource = try AudioFileResource.load(named: "MyAudioFile")
entity.channelAudio = ChannelAudioComponent()
entity.playAudio(resource)
```

The `ChannelAudioComponent` allows you to set the overall level of all sounds played from the entity with the `gain` property, in relative Decibels, in the range `-.infinity ... .zero` where `-infinity` is silent and `.zero` is nominal.

```swift
entity.channelAudio?.gain = -10
```

Channel audio sources are well suited to play back sounds not associated with any visual elements in a scene.

## Topics

### Initializers
- [init(gain: Audio.Decibel)](channelaudiocomponent/init(gain:).md)
  Configure the behavior of a channel audio source.
### Instance Properties
- [var gain: Audio.Decibel](channelaudiocomponent/gain.md)
  The overall level for all sounds emitted from an entity. In relative Decibels, in the range  `-.infinity ... .zero` where `.zero` is the default.

## Relationships

### Conforms To
- [Component](component.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Creating a Spaceship game](creating-a-spaceship-game.md)
  Build an immersive game using RealityKit audio, simulation, and rendering features.
- [struct SpatialAudioComponent](spatialaudiocomponent.md)
  A component that configures how sounds emit from an entity into a person’s environment.
- [struct AmbientAudioComponent](ambientaudiocomponent.md)
  A component that configures the ambient rendering of sounds from an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/channelaudiocomponent)*