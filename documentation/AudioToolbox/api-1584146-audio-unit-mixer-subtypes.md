# Audio Unit Mixer Subtypes

**Framework**: Audio Toolbox

## Topics

### Constants
- [var kAudioUnitSubType_3DMixer: UInt32](kaudiounitsubtype_3dmixer.md)
  An audio unit that can have any number of input buses and one output bus. Each input bus can be mono, in which case it can be panned using 3D coordinates and parameters. Stereo input buses pass directly through to the output. Four-channel  inputs are rendered to the output configuration. The single output bus can be configured with 2, 4, 5, 6, 7 or 8 channels.
- [var kAudioUnitSubType_StereoMixer: UInt32](kaudiounitsubtype_stereomixer.md)
  An audio unit that can have any number of input buses, each of which is mono or stereo, and one stereo output bus.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1584146-audio-unit-mixer-subtypes)*