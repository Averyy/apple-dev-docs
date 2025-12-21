# Audio Engine

**Framework**: AVFAudio

Perform advanced real-time and offline audio processing, implement 3D spatialization, and work with MIDI and samplers.

#### Overview

The audio engine provides a powerful, feature-rich API to simplify audio generation, processing, and input/output tasks. The engine contains a group of nodes that connect to form an audio signal processing chain. These nodes perform a variety of tasks on a signal before rendering to an output destination.

Audio Engine helps you achieve simple, as well as complex, audio processing tasks. With Audio Engine, your apps can:

- Play audio using files and buffers
- Capture audio at any point during the processing chain
- Add built-in effects like reverb, delay, distortion, and your custom effects
- Perform stereo and 3D mixing
- Provide MIDI playback and control over sampler instruments

## Topics

### Essentials
- [class AVAudioEngine](avaudioengine.md)
  An object that manages a graph of audio nodes, controls playback, and configures real-time rendering constraints.
### Nodes
- [class AVAudioNode](avaudionode.md)
  An object you use for audio generation, processing, or an I/O block.
- [class AVAudioInputNode](avaudioinputnode.md)
  An object that connects to the system’s audio input.
- [class AVAudioOutputNode](avaudiooutputnode.md)
  An object that connects to the system’s audio output.
- [class AVAudioIONode](avaudioionode.md)
  An object that performs audio input or output in the engine.
### Playback
- [Playing custom audio with your own player](playing-custom-audio-with-your-own-player.md)
  Construct an audio player to play your custom audio data, and optionally take advantage of the advanced features of AirPlay 2.
- [Using voice processing](using-voice-processing.md)
  Add voice-processing capabilities to your app by using audio engine.
- [class AVAudioPlayerNode](avaudioplayernode.md)
  An object for scheduling the playback of buffers or segments of audio files.
### MIDI
- [class AVAudioSequencer](avaudiosequencer.md)
  An object that plays audio from a collection of MIDI events the system organizes into music tracks.
- [class AVAudioUnitSampler](avaudiounitsampler.md)
  An object that you configure with one or more instrument samples, based on Apple’s Sampler audio unit.
### Mixing
- [class AVAudioMixerNode](avaudiomixernode.md)
  An object that takes any number of inputs and converts them into a single output.
- [protocol AVAudioMixing](avaudiomixing.md)
  A collection of properties that are applicable to the input bus of a mixer node.
### Effects
- [Creating custom audio effects](creating-custom-audio-effects.md)
  Add custom audio-effect processing to apps like Logic Pro X and GarageBand by creating Audio Unit (AU) plug-ins.
- [Audio Units](audio-units.md)
  The data type for a plug-in component that provides audio processing or audio data generation.
### Rendering
- [Building a signal generator](building-a-signal-generator.md)
  Generate audio signals using an audio source node and a custom render callback.
- [Performing offline audio processing](performing-offline-audio-processing.md)
  Add offline audio processing features to your app by enabling offline manual rendering mode.
- [class AVAudioSourceNode](avaudiosourcenode.md)
  An object that supplies audio data.
- [class AVAudioSinkNode](avaudiosinknode.md)
  An object that receives audio data.
### Conversion
- [class AVAudioConverter](avaudioconverter.md)
  An object that converts streams of audio between formats.
### Spatial audio
- [class AVAudioEnvironmentNode](avaudioenvironmentnode.md)
  An object that simulates a 3D audio environment.
- [class AVAudioEnvironmentDistanceAttenuationParameters](avaudioenvironmentdistanceattenuationparameters.md)
  An object that specifies the amount of attenuation distance, the gradual loss in audio intensity, and other characteristics.
- [class AVAudioEnvironmentReverbParameters](avaudioenvironmentreverbparameters.md)
  A class that encapsulates the parameters that you use to control the reverb of the environment node class.
- [protocol AVAudio3DMixing](avaudio3dmixing.md)
  A collection of properties that define 3D mixing properties.
- [struct AVAudio3DPoint](avaudio3dpoint.md)
  A structure that represents a point in 3D space.
- [struct AVAudio3DVectorOrientation](avaudio3dvectororientation.md)
  A structure that represents two orthogonal vectors that describe the orientation of the listener in 3D space.
- [struct AVAudio3DAngularOrientation](avaudio3dangularorientation.md)
  A structure that represents the angular orientation of the listener in 3D space.
- [enum AVAudio3DMixingSourceMode](avaudio3dmixingsourcemode.md)
  The source modes for the input bus of the audio environment node.
- [enum AVAudio3DMixingRenderingAlgorithm](avaudio3dmixingrenderingalgorithm.md)
  The types of rendering algorithms available per input bus of the environment node.
- [enum AVAudioEnvironmentOutputType](avaudioenvironmentoutputtype.md)
  The output types for using with the automatic 3D mixing rendering algorithm.
- [enum AVAudio3DMixingPointSourceInHeadMode](avaudio3dmixingpointsourceinheadmode.md)
  The in-head modes for a point source.
- [typealias AVAudio3DVector](avaudio3dvector.md)
  A structure that represents a vector in 3D space, in degrees.
### Supporting data types
- [class AVAudioBuffer](avaudiobuffer.md)
  An object that represents a buffer of audio data with a format.
- [class AVAudioFile](avaudiofile.md)
  An object that represents an audio file that the system can open for reading or writing.
- [class AVAudioTime](avaudiotime.md)
  An object you use to represent a moment in time.
- [Audio settings](audio-settings.md)
  Configure audio processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/audio-engine)*