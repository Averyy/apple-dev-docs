# Audio Toolbox

**Framework**: Audio Toolbox  
**Kind**: module

Record or play audio, convert formats, parse audio streams, and configure your audio session.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

#### Overview

The AudioToolbox framework provides interfaces for recording, playback, and stream parsing. In iOS, the framework provides additional interfaces for managing audio sessions.

## Topics

### Essentials
- [Porting your audio code to Apple silicon](../Apple-Silicon/porting-your-audio-code-to-apple-silicon.md)
  Eliminate issues in your audio-specific code when running on Apple silicon Mac computers.
### Audio Units
- [Generating spatial audio from a multichannel audio stream](generating-spatial-audio-from-a-multichannel-audio-stream.md)
  Convert 8-channel audio to 2-channel spatial audio by using a spatial mixer audio unit.
- [Audio Unit v3 Plug-Ins](audio-unit-v3-plug-ins.md)
  Deliver custom audio effects, instruments, and other audio behaviors using an Audio Unit v3 app extension.
- [Audio Components](audio-components.md)
  Find, load, and configure audio components, such as Audio Units and audio codecs.
- [Audio Unit v2 (C) API](audio-unit-v2-c-api.md)
  Configure an Audio Unit and prepare it to render audio.
- [Audio Unit Properties](audio-unit-properties.md)
  Obtain information about the built-in mixers, equalizers, filters, effects, and other Audio Unit app extensions.
- [Audio Unit Voice I/O](audio-unit-voice-i-o.md)
  Configure system voice processing and respond to speech events.
### Playback and Recording
- [Audio Queue Services](audio-queue-services.md)
  Connect to audio hardware and manage the recording or playback process.
- [Audio Services](audio-services.md)
  Play short sounds or trigger a vibration effect on iOS devices with the appropriate hardware.
- [Music Player](music-player.md)
  Create and play a sequence of tracks, and manage aspects of playback in response to standard events.
### Audio Files and Formats
- [Audio Format Services](audio-format-services.md)
  Access information about audio formats and codecs.
- [Audio File Services](audio-file-services.md)
  Read or write a variety of audio data to or from disk or a memory buffer.
- [Extended Audio File Services](extended-audio-file-services.md)
  Read and write compressed files and linear PCM audio files using a simplified interface.
- [Audio File Stream Services](audio-file-stream-services.md)
  Parse streamed audio files as the data arrives on the user’s computer.
- [Audio File Components](audio-file-components.md)
  Get information about audio file formats, and about files containing audio data.
- [Core Audio File Format](core-audio-file-format.md)
  Parse the structure of Core Audio files.
### Utilities
- [Analyzing audio performance with Instruments](analyzing-audio-performance-with-instruments.md)
  Ensure a smooth and immersive audio experience in your apps using Audio System Trace.
- [Audio Converter Services](audio-converter-services.md)
  Convert between linear PCM audio formats, and between linear PCM and compressed formats.
- [Audio Session Support](audio-session-support.md)
  Describe the properties that you associate with audio sessions and audio routes.
- [Audio Toolbox Debugging](audio-toolbox-debugging.md)
  Obtain the internal state of Core Audio objects during the development and debugging of your code.
- [Workgroup Management](workgroup-management.md)
  Coordinate the activity of custom real-time audio threads with those of the system and other processes.
- [Audio Codec](audio-codec.md)
  Translate audio data from one format to another.
- [Clock Utilities](clock-utilities.md)
  Manage time-related information associated with audio playback.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Reference
- [AudioToolbox Structures](audiotoolbox-structures.md)
- [AudioToolbox Enumerations](audiotoolbox-enumerations.md)
- [AudioToolbox Constants](audiotoolbox-constants.md)
- [AudioToolbox Functions](audiotoolbox-functions.md)
- [AudioToolbox Data Types](audiotoolbox-data-types.md)
### Macros
- [Macros](audiotoolbox-macros.md)
### Variables
- [var kAudioUnitErr_MultipleVoiceProcessors: OSStatus](kaudiouniterr_multiplevoiceprocessors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AudioToolbox)*