# Audio

**Framework**: RealityKit

Create personalized and realistic spatial audio experiences.

#### Overview

Creating a compelling audio experience with RealityKit is as simple as playing audio on your existing RealityKit entities. Use RealityKit’s default audio settings to create a personalized and realistic experience or utilize advanced customization options to tailor the audio for the needs of your application. Utilizing acoustic ray tracing and a personalized HRTF, RealityKit provides lifelike and high-quality sound.

You can load and configure audio with an [`AudioResource`](audioresource.md) subclass, such as [`AudioFileResource`](audiofileresource.md), and adjust the spatial rendering with [`SpatialAudioComponent`](spatialaudiocomponent.md), [`AmbientAudioComponent`](ambientaudiocomponent.md), [`ChannelAudioComponent`](channelaudiocomponent.md). Control the audio resource playback with [`AudioPlaybackController`](audioplaybackcontroller.md). For real-time audio playback you can prepare a [`Audio.GeneratorRenderHandler`](audio/generatorrenderhandler.md) and control playback with [`AudioGeneratorController`](audiogeneratorcontroller.md). You can control the playback levels of multiple resources at once with [`AudioMixGroup`](audiomixgroup.md) and [`AudioMixGroupsComponent`](audiomixgroupscomponent.md).

## Topics

### Audio source components
- [Creating a Spaceship game](creating-a-spaceship-game.md)
  Build an immersive game using RealityKit audio, simulation, and rendering features.
- [struct SpatialAudioComponent](spatialaudiocomponent.md)
  A component that configures how sounds emit from an entity into a person’s environment.
- [struct AmbientAudioComponent](ambientaudiocomponent.md)
  A component that configures the ambient rendering of sounds from an entity.
- [struct ChannelAudioComponent](channelaudiocomponent.md)
  A component that configures channel-based rendering of sounds from an entity.
### Playback controllers
- [class AudioPlaybackController](audioplaybackcontroller.md)
  A controller that manages an audio playback instance.
- [class AudioGeneratorController](audiogeneratorcontroller.md)
  A controller that manages the playback of a real-time audio stream.
- [struct AudioGeneratorConfiguration](audiogeneratorconfiguration.md)
  A container for various settings for preparing and playing an AudioGeneratorController.
- [enum AudioEvents](audioevents.md)
  Events associated with audio playback.
- [struct PlayAudioAction](playaudioaction.md)
  An action which plays an audio resource on the given target entity.
### Audio resources
- [class AudioFileResource](audiofileresource.md)
  An audio resource that you load from a file or from a URL.
- [class AudioFileGroupResource](audiofilegroupresource.md)
  An audio file group.
- [class AudioBufferResource](audiobufferresource.md)
  An audio resource that you load from an [`AVAudioBuffer`](https://developer.apple.com/documentation/AVFAudio/AVAudioBuffer).
- [struct AudioLibraryComponent](audiolibrarycomponent.md)
  A container for audio resources that you can look up by user-defined names.
- [class AudioResource](audioresource.md)
  A playable audio resource
- [AudioResource.Calibration](audioresource/calibration.md)
  A container for different calibration modes that can be applied for playback.
- [AudioResource.Normalization](audioresource/normalization.md)
  Normalization adjusts the level of an audio file or buffer to be at a defined target.
### Reverb
- [struct Reverb](reverb.md)
  The reverberation RealityKit applies to spatial audio sources.
- [Reverb.Preset](reverb/preset.md)
  Reverbs defined by a preset environment.
- [struct ReverbComponent](reverbcomponent.md)
  A component that defines the reverberation of spatial audio sources.
### Audio mixing
- [struct AudioMixGroup](audiomixgroup.md)
  A group that manages the playback properties of multiple playing sounds.
- [struct AudioMixGroupsComponent](audiomixgroupscomponent.md)
  A component that provides functionality for controlling the playback of audio you assign to mix groups in a scene.
### Audio types
- [enum Audio](audio.md)
  A namespace for types that are used commonly in audio.
- [typealias Decibel](audio/decibel.md)
  The unit for measuring intensity of sound on a logarithmic scale.
- [Audio.Directivity](audio/directivity.md)
  The radiation pattern of sound emitted from an entity.
- [Audio.DistanceAttenuation](audio/distanceattenuation.md)
  The different ways that audio intensity diminishes as the distance between the listener and the sound source increases.

## See Also

- [Hello World](../visionOS/World.md)
  Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Enabling video reflections in an immersive environment](../visionOS/enabling-video-reflections-in-an-immersive-environment.md)
  Create a more immersive experience by adding video reflections in a custom environment.
- [Creating a spatial drawing app with RealityKit](creating-a-spatial-drawing-app-with-realitykit.md)
  Use low-level mesh and texture APIs to achieve fast updates to a person’s brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Generating interactive geometry with RealityKit](generating-interactive-geometry-with-realitykit.md)
  Create an interactive mesh with low-level mesh and low-level texture.
- [Combining 2D and 3D views in an immersive app](combining-2d-and-3d-views-in-an-immersive-app.md)
  Use attachments to place 2D content relative to 3D content in your visionOS app.
- [Transforming RealityKit entities using gestures](transforming-realitykit-entities-with-gestures.md)
  Build a RealityKit component to support standard visionOS gestures on any entity.
- [Models and meshes](scene-content-models-and-meshes.md)
  Display virtual objects in your scene with mesh-based models.
- [Materials, textures, and shaders](scene-content-materials-and-shaders.md)
  Apply textures to the surface of your scene’s 3D objects to give each object a unique appearance.
- [Anchors](scene-content-anchors.md)
  Lock virtual content to the real world.
- [Lights and cameras](scene-content-lights-and-cameras.md)
  Control the lighting and point of view for a scene.
- [Content synchronization](scene-content-content-synchronization.md)
  Synchronize the contents of entities locally or across the network.
- [Videos](scene-content-videos.md)
  Present videos in your RealityKit experiences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene-content-audio)*