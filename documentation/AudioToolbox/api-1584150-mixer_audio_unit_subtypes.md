# Mixer Audio Unit Subtypes

**Framework**: Audio Toolbox  
**Role**: API Collection

Audio mixing audio unit subtypes for audio units provided by Apple.

## Topics

### Constants
- [var kAudioUnitSubType_MatrixMixer: UInt32](./kaudiounitsubtype_matrixmixer.md)
- [var kAudioUnitSubType_MultiChannelMixer: UInt32](./kaudiounitsubtype_multichannelmixer.md)
  An audio unit that can have any number of input buses, with any number of channels on each input bus, and one output bus. In macOS, the output bus can have any number of channels. In iOS, the output bus always has two channels.
- [var kAudioUnitSubType_SpatialMixer: UInt32](./kaudiounitsubtype_spatialmixer.md)

## See Also

### Mixers
- [Audio Unit Mixer Subtypes](./api-1584146-audio-unit-mixer-subtypes.md)
- [enum AUSpatialMixerAttenuationCurve](./auspatialmixerattenuationcurve.md)
- [struct AUSpatialMixerRenderingFlags](./auspatialmixerrenderingflags.md)
- [AUSpatialMixer Parameters](./api-1390073-auspatialmixer-parameters.md)
- [Panner Audio Unit Parameters](./api-1389991-panner-audio-unit-parameters.md)
- [AUMatrixMixer Parameters](./api-1390003-aumatrixmixer-parameters.md)
- [AUMultiChannelMixer Parameters](./api-1389739-aumultichannelmixer_parameters.md)
  Parameters for the Multichannel Mixer unit.
- [Spatial Mixer Property IDs](./api-1534150-spatial-mixer-property-ids.md)
- [Stereo Mixer Unit Parameters](./api-1389928-stereo-mixer-unit-parameters.md)
- [Mixer Audio Unit Properties](./api-1534041-mixer_audio_unit_properties.md)
  Properties for Apple mixer audio units.
- [enum AUSpatialMixerOutputType](./auspatialmixeroutputtype.md)
- [enum AUSpatialMixerPointSourceInHeadMode](./auspatialmixerpointsourceinheadmode.md)
- [enum AUSpatialMixerSourceMode](./auspatialmixersourcemode.md)
- [3D Mixer Unit Parameters](./api-1389763-3d_mixer_unit_parameters.md)
  Parameters for the 3D Mixer unit.
- [enum AU3DMixerAttenuationCurve](./au3dmixerattenuationcurve.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1584150-mixer_audio_unit_subtypes)*