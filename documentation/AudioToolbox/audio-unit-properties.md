# Audio Unit Properties

**Framework**: Audio Toolbox

Obtain information about the built-in mixers, equalizers, filters, effects, and other Audio Unit app extensions.

## Topics

### General
- [Other Plug-In Formats](1534082-other-plug-in-formats.md)
- [RenderQuality](1534177-renderquality.md)
  Render quality settings for audio units.
- [General Audio Unit Properties](general-audio-unit-properties.md)
  Properties that apply to any audio unit.
- [struct HostCallbackInfo](hostcallbackinfo.md)
  The time- and transport-related callback functions for an audio unit.
### Mixers
- [Audio Unit Mixer Subtypes](1584146-audio-unit-mixer-subtypes.md)
- [enum AUSpatialMixerAttenuationCurve](auspatialmixerattenuationcurve.md)
- [struct AUSpatialMixerRenderingFlags](auspatialmixerrenderingflags.md)
- [AUSpatialMixer Parameters](1390073-auspatialmixer-parameters.md)
- [Panner Audio Unit Parameters](1389991-panner-audio-unit-parameters.md)
- [AUMatrixMixer Parameters](1390003-aumatrixmixer-parameters.md)
- [AUMultiChannelMixer Parameters](1389739-aumultichannelmixer_parameters.md)
  Parameters for the Multichannel Mixer unit.
- [Spatial Mixer Property IDs](1534150-spatial-mixer-property-ids.md)
- [Stereo Mixer Unit Parameters](1389928-stereo-mixer-unit-parameters.md)
- [Mixer Audio Unit Properties](1534041-mixer_audio_unit_properties.md)
  Properties for Apple mixer audio units.
- [Mixer Audio Unit Subtypes](1584150-mixer_audio_unit_subtypes.md)
  Audio mixing audio unit subtypes for audio units provided by Apple.
- [enum AUSpatialMixerOutputType](auspatialmixeroutputtype.md)
- [enum AUSpatialMixerPointSourceInHeadMode](auspatialmixerpointsourceinheadmode.md)
- [enum AUSpatialMixerSourceMode](auspatialmixersourcemode.md)
- [3D Mixer Unit Parameters](1389763-3d_mixer_unit_parameters.md)
  Parameters for the 3D Mixer unit.
- [enum AU3DMixerAttenuationCurve](au3dmixerattenuationcurve.md)
- [struct AU3DMixerRenderingFlags](au3dmixerrenderingflags.md)
- [struct MixerDistanceParams](mixerdistanceparams.md)
### Equalizers
- [Parametric EQ Unit Parameters](1389950-parametric_eq_unit_parameters.md)
  Parameters for the Parametric EQ unit.
- [Audio Unit Graphic EQ Parameter ID](1389932-audio-unit-graphic-eq-parameter.md)
- [Peak Limiter Unit Parameters](1389597-peak_limiter_unit_parameters.md)
  Parameters for the Peak Limiter unit.
- [Dynamics Processor Unit Parameters](1389787-dynamics_processor_unit_paramete.md)
  Parameters for the Dynamics Processor unit.
- [Frequency Response Constants](1534092-frequency_response_constants.md)
  The maximum number of frequency response bin structures for the `AudioUnitProperty_FrequencyResponse` property.
- [enum AUSpatializationAlgorithm](auspatializationalgorithm.md)
### Filters
- [Audio Unit Filter Subtypes](1584153-audio-unit-filter-subtypes.md)
- [Bandpass Unit Parameters](1390144-bandpass_unit_parameters.md)
  Parameters for the Bandpass unit.
- [AUHipass Parameters](1389948-auhipass_parameters.md)
  Parameters for the Highpass unit.
- [AULowpass Parameters](1389999-aulowpass_parameters.md)
  Parameters for the Lowpass unit.
- [AULowShelf Parameters](1389995-aulowshelf_parameters.md)
  Parameters for the Low Shelf Filter unit.
- [AUHighShelfFilter Parameters](1389967-auhighshelffilter_parameters.md)
  Parameters for the High Shelf Filter unit.
- [AUNBandEQ Filter Types](1389965-aunbandeq_filter_types.md)
  Values for the filter type parameter of the Multitype EQ (NBandEQ) unit.
- [AUNBandEQ Property IDs](1534022-aunbandeq-property-ids.md)
- [AUNBandEQ Parameters](1389745-aunbandeq-parameters.md)
### Effects
- [Effect Audio Unit Subtypes](1584154-effect_audio_unit_subtypes.md)
  Effect (digital signal processing) audio unit subtypes for audio units provided by Apple.
- [AUMatrixReverb Parameters](1389801-aumatrixreverb-parameters.md)
- [AUDistortion Parameters](1390086-audistortion-parameters.md)
- [Reverb Parameters](1390119-reverb_parameters.md)
  Additional reverb parameters.
- [Reverb Unit Parameters](1615024-reverb_unit_parameters.md)
  Parameters for the Reverb unit.
- [enum AUReverbRoomType](aureverbroomtype.md)
- [Varispeed Unit Parameters](1390014-varispeed_unit_parameters.md)
  Parameters for the Varispeed unit.
- [AUDelay Parameters](1390010-audelay-parameters.md)
- [AUMultibandCompressor Parameters](1389781-aumultibandcompressor-parameters.md)
- [AUDeferredRenderer Properties](1534061-audeferredrenderer-properties.md)
- [AUSampleDelay Parameters](3547050-ausampledelay-parameters.md)
- [AUNewTimePitch Parameters](1389643-aunewtimepitch-parameters.md)
- [AUTimePitch, AUTimePitch (offline), and AUPitch Unit Parameters](1389946-autimepitch_autimepitch_offline.md)
### Input/Output
- [I/O Audio Unit Properties](1534116-i_o_audio_unit_properties.md)
  Properties for Apple I/O audio units (sometimes called output units).
- [Inter-App Output Unit Property IDs](1621039-inter-app-output-unit-property-ids.md)
- [Inter-App Audio Unit Property IDs](1621038-inter-app-audio-unit-property-ids.md)
- [Output Unit Parameters](1389916-output_unit_parameters.md)
- [AUNetReceive Properties](1534109-aunetreceive-properties.md)
- [AUNetSend Properties](1534207-aunetsend-properties.md)
- [AUNetSend Parameters](1389633-aunetsend-parameters.md)
- [AUNetReceive Parameters](1389920-aunetreceive-parameters.md)
- [AUNetSendPresetFormat Properties](1534212-aunetsendpresetformat-properties.md)
- [Net Status Audio Unit Parameters](1389891-net-status-audio-unit-parameters.md)
- [I/O Audio Unit Function Selectors](1585807-i_o_audio_unit_function_selector.md)
  Audio unit component selectors, specific to I/O audio units, that correspond to functions in the audio unit API.
- [struct AudioOutputUnitMIDICallbacks](audiooutputunitmidicallbacks.md)
- [struct AudioOutputUnitStartAtTimeParams](audiooutputunitstartattimeparams.md)
  A timestamp for scheduled starting of an I/O audio unit.
### Generators
- [AURandom Parameters](1389639-aurandom-parameters.md)
- [AUSampler Parameters](1389769-ausampler-parameters.md)
- [AUSampler Property IDs](1534086-ausampler-property-ids.md)
- [AUSampler Properties](1533959-ausampler-properties.md)
- [AURogerBeep Parameters](1389727-aurogerbeep-parameters.md)
- [AUMIDISynth Properties](1534190-aumidisynth-properties.md)
- [AURoundTripAACParam Parameters](1389808-auroundtripaacparam-parameters.md)

## See Also

- [Generating spatial audio from a multichannel audio stream](generating-spatial-audio-from-a-multichannel-audio-stream.md)
  Convert 8-channel audio to 2-channel spatial audio by using a spatial mixer audio unit.
- [Audio Unit v3 Plug-Ins](audio-unit-v3-plug-ins.md)
  Deliver custom audio effects, instruments, and other audio behaviors using an Audio Unit v3 app extension.
- [Audio Components](audio-components.md)
  Find, load, and configure audio components, such as Audio Units and audio codecs.
- [Audio Unit v2 (C) API](audio-unit-v2-c-api.md)
  Configure an Audio Unit and prepare it to render audio.
- [Audio Unit Voice I/O](audio-unit-voice-i-o.md)
  Configure system voice processing and respond to speech events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audio-unit-properties)*