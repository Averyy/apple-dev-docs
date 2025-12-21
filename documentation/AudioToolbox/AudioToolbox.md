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
- [Anchoring sound to a window or volume](spatializing-sound-from-a-uiscene.md)
  Provide unique app experiences by attaching sounds to windows and volumes in 3D space.
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
### Protocols
- [protocol SpatialAudioExperience](spatialaudioexperience.md)
  Configure an audio stream for spatial computing.
### Structures
- [struct AutomaticSpatialAudio](automaticspatialaudio.md)
  A spatial audio experience determined by the system.
- [struct BypassedSpatialAudio](bypassedspatialaudio.md)
  An experience in which the system does not apply spatial processing to the audio stream.
- [struct FixedSpatialAudio](fixedspatialaudio.md)
  A spatial experience that does not take user motion into account.
- [struct HeadTrackedSpatialAudio](headtrackedspatialaudio.md)
  A spatial experience that takes user motion into account.
### Variables
- [var kAUAudioMixParameter_RemixAmount: AudioUnitParameterID](kauaudiomixparameter_remixamount.md)
- [var kAUAudioMixParameter_Style: AudioUnitParameterID](kauaudiomixparameter_style.md)
- [var kAUAudioMixProperty_EnableSpatialization: AudioUnitPropertyID](kauaudiomixproperty_enablespatialization.md)
- [var kAUAudioMixProperty_SpatialAudioMixMetadata: AudioUnitPropertyID](kauaudiomixproperty_spatialaudiomixmetadata.md)
- [var kAudioCodecContentSource_AV_Spatial_Live: Int32](kaudiocodeccontentsource_av_spatial_live.md)
- [var kAudioCodecContentSource_AV_Spatial_Offline: Int32](kaudiocodeccontentsource_av_spatial_offline.md)
- [var kAudioCodecContentSource_AV_Traditional_Live: Int32](kaudiocodeccontentsource_av_traditional_live.md)
- [var kAudioCodecContentSource_AV_Traditional_Offline: Int32](kaudiocodeccontentsource_av_traditional_offline.md)
- [var kAudioCodecContentSource_AppleAV_Spatial_Live: Int32](kaudiocodeccontentsource_appleav_spatial_live.md)
- [var kAudioCodecContentSource_AppleAV_Spatial_Offline: Int32](kaudiocodeccontentsource_appleav_spatial_offline.md)
- [var kAudioCodecContentSource_AppleAV_Traditional_Live: Int32](kaudiocodeccontentsource_appleav_traditional_live.md)
- [var kAudioCodecContentSource_AppleAV_Traditional_Offline: Int32](kaudiocodeccontentsource_appleav_traditional_offline.md)
- [var kAudioCodecContentSource_AppleCapture_Spatial: Int32](kaudiocodeccontentsource_applecapture_spatial.md)
- [var kAudioCodecContentSource_AppleCapture_Spatial_Enhanced: Int32](kaudiocodeccontentsource_applecapture_spatial_enhanced.md)
- [var kAudioCodecContentSource_AppleCapture_Traditional: Int32](kaudiocodeccontentsource_applecapture_traditional.md)
- [var kAudioCodecContentSource_AppleMusic_Spatial: Int32](kaudiocodeccontentsource_applemusic_spatial.md)
- [var kAudioCodecContentSource_AppleMusic_Traditional: Int32](kaudiocodeccontentsource_applemusic_traditional.md)
- [var kAudioCodecContentSource_ApplePassthrough: Int32](kaudiocodeccontentsource_applepassthrough.md)
- [var kAudioCodecContentSource_Capture_Spatial: Int32](kaudiocodeccontentsource_capture_spatial.md)
- [var kAudioCodecContentSource_Capture_Spatial_Enhanced: Int32](kaudiocodeccontentsource_capture_spatial_enhanced.md)
- [var kAudioCodecContentSource_Capture_Traditional: Int32](kaudiocodeccontentsource_capture_traditional.md)
- [var kAudioCodecContentSource_Music_Spatial: Int32](kaudiocodeccontentsource_music_spatial.md)
- [var kAudioCodecContentSource_Music_Traditional: Int32](kaudiocodeccontentsource_music_traditional.md)
- [var kAudioCodecContentSource_Passthrough: Int32](kaudiocodeccontentsource_passthrough.md)
- [var kAudioCodecContentSource_Reserved: Int32](kaudiocodeccontentsource_reserved.md)
- [var kAudioCodecContentSource_Unspecified: Int32](kaudiocodeccontentsource_unspecified.md)
- [var kAudioCodecDynamicRangeControlConfiguration_Capture: UInt32](kaudiocodecdynamicrangecontrolconfiguration_capture.md)
- [var kAudioCodecDynamicRangeControlConfiguration_Movie: UInt32](kaudiocodecdynamicrangecontrolconfiguration_movie.md)
- [var kAudioCodecDynamicRangeControlConfiguration_Music: UInt32](kaudiocodecdynamicrangecontrolconfiguration_music.md)
- [var kAudioCodecDynamicRangeControlConfiguration_None: UInt32](kaudiocodecdynamicrangecontrolconfiguration_none.md)
- [var kAudioCodecDynamicRangeControlConfiguration_Speech: UInt32](kaudiocodecdynamicrangecontrolconfiguration_speech.md)
- [var kAudioCodecPropertyASPFrequency: AudioCodecPropertyID](kaudiocodecpropertyaspfrequency.md)
- [var kAudioCodecPropertyContentSource: AudioCodecPropertyID](kaudiocodecpropertycontentsource.md)
- [var kAudioCodecPropertyDynamicRangeControlConfiguration: AudioCodecPropertyID](kaudiocodecpropertydynamicrangecontrolconfiguration.md)
- [var kAudioConverterPropertyChannelMixMap: AudioConverterPropertyID](kaudioconverterpropertychannelmixmap.md)
- [var kAudioConverterPropertyPerformDownmix: AudioConverterPropertyID](kaudioconverterpropertyperformdownmix.md)
- [var kAudioUnitErr_MultipleVoiceProcessors: OSStatus](kaudiouniterr_multiplevoiceprocessors.md)
- [var kAudioUnitSubType_AUAudioMix: UInt32](kaudiounitsubtype_auaudiomix.md)
### Functions
- [func AudioConverterFillComplexBufferRealtimeSafe(AudioConverterRef, AudioConverterComplexInputDataProcRealtimeSafe, UnsafeMutableRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<AudioStreamPacketDescription>?) -> OSStatus](audioconverterfillcomplexbufferrealtimesafe(_:_:_:_:_:_:).md)
- [func AudioConverterFillComplexBufferWithPacketDependencies(AudioConverterRef, AudioConverterComplexInputDataProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<AudioStreamPacketDescription>?, UnsafeMutablePointer<AudioStreamPacketDependencyDescription>) -> OSStatus](audioconverterfillcomplexbufferwithpacketdependencies(_:_:_:_:_:_:_:).md)
- [func AudioFileWritePacketsWithDependencies(AudioFileID, Bool, UInt32, UnsafePointer<AudioStreamPacketDescription>?, UnsafePointer<AudioStreamPacketDependencyDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](audiofilewritepacketswithdependencies(_:_:_:_:_:_:_:_:).md)
- [func AudioServicesPlayAlertSound(SystemSoundID, spatialExperience: any SpatialAudioExperience) async](audioservicesplayalertsound(_:spatialexperience:).md)
  Play an alert sound with the provided spatial audio experience.
- [func AudioServicesPlaySystemSound(SystemSoundID, spatialExperience: any SpatialAudioExperience) async](audioservicesplaysystemsound(_:spatialexperience:).md)
  Play a system sound with the provided spatial audio experience.
### Type Aliases
- [typealias AudioConverterComplexInputDataProcRealtimeSafe](audioconvertercomplexinputdataprocrealtimesafe.md)
### Enumerations
- [enum AUAudioMixRenderingStyle](auaudiomixrenderingstyle.md)
- [enum SpatialAudioExperiences](spatialaudioexperiences.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AudioToolbox)*