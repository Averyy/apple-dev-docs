# PHASE

**Framework**: PHASE  
**Kind**: module

Create dynamic audio experiences in your game or app that react to events and cues in the environment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

#### Overview

Use PHASE (Physical Audio Spatialization Engine) to provide complex, dynamic audio experiences in your games and apps. With PHASE, you can control sound layers and adjust audio parameters in real time. As you develop your app, dynamic integration with your app’s visual scene enables audio to react to logic and visual changes automatically. The framework supports various audio hardware, which enables your app to provide a consistent spatial audio experience across platforms and output devices like headphones and speakers.

![Illustration of in-game scenes that demonstrate PHASE features. At left, a polygon contains a dragon with a callout that reads Volumetric sound source. A sound wave emits from the dragon to a hero. A tree structure extends outward from the dragon with a callout that reads Sound event hierarchy. The tree structure highlights a specific path from its root node to one of its leaf nodes. The leaf node contains a sound wave, which indicates a particular sound wave that emits from the dragon. At right, a dragon fireball collides with a rock. Sound waves emit outward from the fireball, except in the area behind the rock. A callout extends from the area that reads Geometric sound occlusion.](https://docs-assets.developer.apple.com/published/41e1fab50a65e7a67ff5ebdbbf5af38e/media-3855995%402x.png)

> **Note**:  If the audio in your game or app doesn’t incorporate environmental events or cues, you can use [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation) or [`Core Audio`](https://developer.apple.com/documentation/CoreAudio).

##### Integrate Audio with Visual Simulation

Apps and games that model a detailed environment involve substantial revision during development. When you provide PHASE with a basic understanding of your app’s scene, audio plays in accordance with the scene’s characteristics. As you modify the scene, such as by adding a game level, the audio follows along by accommodating the level’s visual shape and properties. PHASE couples sound with visuals and minimizes your app’s audio maintenance by:

- Accepting scene geometry and reducing the volume of obstructed, sound-emitting scene objects. For example, PHASE lowers the volume of an incoming fireball when the player takes cover behind a wall.
- Offering complex sound events that play in reaction to your app’s runtime state.
- Adding sound effects that emanate from a shape. When you provide the shape of a scene object to PHASE, the sound’s volume scales based on the player’s distance and orientation relative to the shape.
- Adding reverberation and timed audio reflection to create environmental effects and simulate indoor scenes.

## Topics

### Essentials
- [Playing sound from a location in a 3D scene](playing-sound-from-a-location-in-a-3d-scene.md)
  Position sound from a specific direction and automatically raise or lower volume based on the environment.
- [Personalizing spatial audio in your app](personalizing-spatial-audio-in-your-app.md)
  Enhance the realism of spatial audio output by tracking a person’s head movement and accounting for their personal spatial audio profile.
- [PHASE updates](../Updates/PHASE.md)
  Learn about important changes to PHASE.
### Setup
- [class PHASEEngine](phaseengine.md)
  An object that manages audio assets, controls playback, and configures environmental effects.
- [PHASEEngine.UpdateMode](phaseengine/updatemode.md)
  Modes that determine when the framework consumes API calls and updates internal state.
- [PHASEEngine.RenderingMode](phaseengine/renderingmode.md)
  Modes that determine whether the system renders audio in process or out of process.
- [class PHASEAssetRegistry](phaseassetregistry.md)
  A central repository of audio assets.
- [enum PHASENormalizationMode](phasenormalizationmode.md)
  Options that determine whether the framework adjusts a sound asset’s loudness for the user’s output device.
- [enum PHASESpatializationMode](phasespatializationmode.md)
  The manner in which PHASE outputs spatial audio.
- [enum PHASEReverbPreset](phasereverbpreset.md)
  The manner in which PHASE diffuses resonating sound.
- [class PHASEMedium](phasemedium.md)
  A property or quality of the environment that affects how sound travels.
### Soundscape Creation
- [class PHASESource](phasesource.md)
  An object that plays audio from a 3D location and orientation in a scene.
- [class PHASEListener](phaselistener.md)
  A central point of reference that defines the location within the scene that’s most audible to the user.
- [class PHASEOccluder](phaseoccluder.md)
  An object with a shape and position that blocks audio from reaching the listener.
- [class PHASEObject](phaseobject.md)
  An object in the scene.
- [class PHASEShape](phaseshape.md)
  A collection of points that connect to form a 3D volume.
- [PHASEShape.Element](phaseshape/element.md)
  An object that describes the characteristics of a physical surface.
- [class PHASEMaterial](phasematerial.md)
  Surface characteristics that determine the acoustic properties of an object.
- [enum PHASEMaterialPreset](phasematerialpreset.md)
  A collection of physical surfaces that each add a unique acoustic quality to your app’s audio.
- [class PHASEMixerParameters](phasemixerparameters.md)
  An object that specifies a mixer for sound events and orients them in 3D space.
### Audio Selection and Playback
- [class PHASESoundAsset](phasesoundasset.md)
  A sound resource stored in the asset registry.
- [class PHASESoundEvent](phasesoundevent.md)
  An object that determines which audio to play.
- [PHASESoundEvent.RenderingState](phasesoundevent/renderingstate-swift.enum.md)
  The playback status of audio.
- [class PHASESoundEventNodeDefinition](phasesoundeventnodedefinition.md)
  A base class for sound event nodes that connect to form a node hierarchy.
- [class PHASESoundEventNodeAsset](phasesoundeventnodeasset.md)
  A template object for sounds that can play in reaction to environmental state.
- [class PHASEAsset](phaseasset.md)
  A base class that adds a name to framework assets.
- [Sound Event Nodes](sound-event-nodes.md)
  Objects that connect to form a hierarchical tree of audio actions.
### Audio Layering and Effects
- [class PHASEChannelMixerDefinition](phasechannelmixerdefinition.md)
  An audio-layering object that routes sound directly to the device’s output.
- [class PHASEAmbientMixerDefinition](phaseambientmixerdefinition.md)
  An audio-layering object that outputs sound in a particular direction in 3D space.
- [class PHASEMixerDefinition](phasemixerdefinition.md)
  An object to initialize a mixer with a given configuration.
- [class PHASEMixer](phasemixer.md)
  An object that combines multiple audio signals into a single signal.
- [class PHASEDefinition](phasedefinition.md)
  A base class that adds a name to framework definitions.
- [Spatial Mixing](spatial-mixing.md)
  Define environmental characteristics that determine how sound plays in your app’s 3D soundscape.
### Dynamic Sound Control
- [class PHASEEnvelope](phaseenvelope.md)
  A collection of segments that connect to graph a complex curve over a linear input.
- [class PHASEEnvelopeSegment](phaseenvelopesegment.md)
  A curved portion of an envelope.
- [enum PHASECurveType](phasecurvetype.md)
  Options that apply a mathematical function to an input value.
- [class PHASENumericPair](phasenumericpair.md)
  An ordered pair that defines a bounding box for an envelope.
- [Playback Parameterization](playback-parameterization.md)
  Change the characteristics of in-flight audio by adjusting its properties at runtime.
### Sound Grouping and Management
- [class PHASEGroup](phasegroup.md)
  A container that shares audio parameters with a collection of sounds.
- [class PHASEGroupPreset](phasegrouppreset.md)
  A collection of settings for groups.
- [class PHASEGroupPresetSetting](phasegrouppresetsetting.md)
  Settings for group presets.
- [class PHASEDucker](phaseducker.md)
  An object that manages competing sounds.
### Errors
- [PHASE Errors](phase-errors.md)
  Errors that the PHASE framework reports.
### Classes
- [class PHASEPullStreamNode](phasepullstreamnode.md)
- [class PHASEPullStreamNodeDefinition](phasepullstreamnodedefinition.md)
- [class PHASEStreamNode](phasestreamnode.md)
### Structures
- [struct PHASEAutomaticHeadTrackingFlags](phaseautomaticheadtrackingflags.md)
### Type Aliases
- [typealias PHASEPullStreamRenderHandler](phasepullstreamrenderhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/PHASE)*