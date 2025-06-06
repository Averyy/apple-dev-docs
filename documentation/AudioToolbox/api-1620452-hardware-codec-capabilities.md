# Hardware Codec Capabilities

**Framework**: Audio Toolbox

A constant to determine which hardware codecs can be used.

#### Overview

Use this property to determine whether a desired set of codecs can be simultaneously instantiated.

Hardware-based codecs can be used only when playing or recording using Audio Queue Services or using interfaces, such as AVFoundation, which use Audio Queue Services. In particular, you cannot use hardware-based audio codecs with OpenAL or when using the I/O audio unit.

When describing the presence of a hardware codec, the system does not consider the current audio session category. Some categories disallow the use of hardware codecs. A set of hardware codecs is considered available, by this constant, based only on whether the hardware supports the specified combination of codecs.

Some codecs may be available in both hardware and software implementations. Use the [`kAudioFormatProperty_Encoders`](kaudioformatproperty_encoders.md) and [`kAudioFormatProperty_Decoders`](kaudioformatproperty_decoders.md) constants to determine whether a given codec is present, and whether it is hardware or software-based.

Software-based codecs can always be instantiated, so there is no need to use this constant when using software encoding or decoding.

The following code example illustrates how to check whether or not a hardware AAC encoder and a hardware AAC decoder are available, in that order of priority:

```objc
AudioClassDescription requestedCodecs[2] = {
    {
        kAudioEncoderComponentType,
        kAudioFormatAAC,
        kAppleHardwareAudioCodecManufacturer
    },
    {
        kAudioDecoderComponentType,
        kAudioFormatAAC,
        kAppleHardwareAudioCodecManufacturer
    }
};
 
UInt32 successfulCodecs = 0;
size = sizeof (successfulCodecs);
OSStatus result =   AudioFormatGetProperty (
                        kAudioFormatProperty_HardwareCodecCapabilities,
                        requestedCodecs,
                        sizeof (requestedCodecs),
                        &size,
                        &successfulCodecs
                    );
switch (successfulCodecs) {
    case 0:
        // aac hardware encoder is unavailable. aac hardware decoder availability
        // is unknown; could ask again for only aac hardware decoding
    case 1:
        // aac hardware encoder is available but, while using it, no hardware
        // decoder is available.
    case 2:
        // hardware encoder and decoder are available simultaneously
}
```

See also [`Audio Codec Component Constants`](1494086-audio-codec-component-constants.md) and [`Audio Codec Manufacturer and Implementation Types`](1620448-audio-codec-manufacturer-and-imp.md).

## Topics

### Constants
- [var kAudioFormatProperty_HardwareCodecCapabilities: AudioFormatPropertyID](kaudioformatproperty_hardwarecodeccapabilities.md)
  A `UInt32` value indicating the number of codecs from the specified list that can be used, if the application were to begin using them in the specified order. Set the `inSpecifier` parameter to an array of `AudioClassDescription` structures that describes a set of one or more audio codecs. If the property value is the same as the size of the array in the `inSpecifier` parameter, all of the specified codecs can be used.

## See Also

- [Audio Unit Attenuation Properties](1534112-audio-unit-attenuation-propertie.md)
- [Audio Unit Instrument Errors](1584141-audio-unit-instrument-errors.md)
- [Anonymous](1534019-anonymous.md)
- [Anonymous](1534074-anonymous.md)
- [Audio Graph Errors](1537630-audio-graph-errors.md)
- [Audio Converter Property ID](1624333-audio-converter-property-id.md)
- [Anonymous](1621044-anonymous.md)
- [Anonymous](1618426-anonymous.md)
- [Anonymous](1618742-anonymous.md)
- [Anonymous](1619479-anonymous.md)
- [Anonymous](1619504-anonymous.md)
- [Anonymous](1533960-anonymous.md)
- [Anonymous](1534225-anonymous.md)
- [Music Device Properties](1534089-music-device-properties.md)
- [3D Mixer Audio Unit Properties](1534063-3d_mixer_audio_unit_properties.md)
  Properties for the Apple 3D Mixer audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1620452-hardware-codec-capabilities)*