# Audio Format Flags

**Framework**: Core Audio Types

Commonly used combinations of data format flags for an audio stream description.

#### Overview

Prefer using fixed-point formats in [`iOS`](https://developer.apple.com/documentation/PackageDescription/Platform/iOS) and floating-point formats in [`macOS`](https://developer.apple.com/documentation/PackageDescription/Platform/macOS).

## Topics

### Format flags
- [var kAppleLosslessFormatFlag_16BitSourceData: AudioFormatFlags](kapplelosslessformatflag_16bitsourcedata.md)
  A flag that indicates Apple Lossless data sourced from 16-bit native endian signed integer data.
- [var kAppleLosslessFormatFlag_20BitSourceData: AudioFormatFlags](kapplelosslessformatflag_20bitsourcedata.md)
  A flag that indicates Apple Lossless data sourced from 20-bit native endian signed integer data aligned high in 24 bits.
- [var kAppleLosslessFormatFlag_24BitSourceData: AudioFormatFlags](kapplelosslessformatflag_24bitsourcedata.md)
  A flag that indicates Apple Lossless data sourced from 24-bit native endian signed integer data.
- [var kAppleLosslessFormatFlag_32BitSourceData: AudioFormatFlags](kapplelosslessformatflag_32bitsourcedata.md)
  A flag that indicates Apple Lossless data sourced from 32-bit native endian signed integer data.
- [var kAudioFormatFlagIsAlignedHigh: AudioFormatFlags](kaudioformatflagisalignedhigh.md)
  A flag that indicates whether placement of the sample bits is with the high or low bits of the channel.
- [var kAudioFormatFlagIsBigEndian: AudioFormatFlags](kaudioformatflagisbigendian.md)
  A flag that indicates whether the format is big or little endian.
- [var kAudioFormatFlagIsFloat: AudioFormatFlags](kaudioformatflagisfloat.md)
  A flag that indicates whether the format is floating point or integer.
- [var kAudioFormatFlagIsNonInterleaved: AudioFormatFlags](kaudioformatflagisnoninterleaved.md)
  A flag that indicates whether the samples for each channel or frame are continguously located, and whether the layout of the channels or frames is end-to-end.
- [var kAudioFormatFlagIsNonMixable: AudioFormatFlags](kaudioformatflagisnonmixable.md)
  A flag that indicates the format is nonmixable.
- [var kAudioFormatFlagIsPacked: AudioFormatFlags](kaudioformatflagispacked.md)
  A flag that indicates whether placement of the sample bits occupy the entire available bits of the channel.
- [var kAudioFormatFlagIsSignedInteger: AudioFormatFlags](kaudioformatflagissignedinteger.md)
  A flag that indicates whether the format is signed or unsigned integer.
- [var kAudioFormatFlagsAreAllClear: AudioFormatFlags](kaudioformatflagsareallclear.md)
  A flag that indicates whether all the flags are clear.
- [var kAudioFormatFlagsNativeEndian: AudioFormatFlags](kaudioformatflagsnativeendian.md)
  A flag that specifies whether the format is big endian, depending on the endianness of the processor at build time.
- [var kAudioFormatFlagsNativeFloatPacked: AudioFormatFlags](kaudioformatflagsnativefloatpacked.md)
  The flags for the canonical format of fully packed, native endian floating-point data.
- [var kLinearPCMFormatFlagIsAlignedHigh: AudioFormatFlags](klinearpcmformatflagisalignedhigh.md)
  A flag that indicates whether placement of the sample bits is with the high or low bits of the channel.
- [var kLinearPCMFormatFlagIsBigEndian: AudioFormatFlags](klinearpcmformatflagisbigendian.md)
  A flag that indicates whether the format is big or little endian.
- [var kLinearPCMFormatFlagIsFloat: AudioFormatFlags](klinearpcmformatflagisfloat.md)
  A flag that indicates whether the format is floating point or integer.
- [var kLinearPCMFormatFlagIsNonInterleaved: AudioFormatFlags](klinearpcmformatflagisnoninterleaved.md)
  A flag that indicates whether the samples for each channel or frame are continguously located, and whether the layout of the channels or frames is end-to-end.
- [var kLinearPCMFormatFlagIsNonMixable: AudioFormatFlags](klinearpcmformatflagisnonmixable.md)
  A flag that indicates the format is nonmixable.
- [var kLinearPCMFormatFlagIsPacked: AudioFormatFlags](klinearpcmformatflagispacked.md)
  A flag that indicates whether placement of the sample bits occupy the entire available bits of the channel.
- [var kLinearPCMFormatFlagIsSignedInteger: AudioFormatFlags](klinearpcmformatflagissignedinteger.md)
  A flag that indicates whether the format is signed or unsigned integer.
- [var kLinearPCMFormatFlagsAreAllClear: AudioFormatFlags](klinearpcmformatflagsareallclear.md)
  A flag that indicates whether all the flags are clear.
- [var kLinearPCMFormatFlagsSampleFractionMask: AudioFormatFlags](klinearpcmformatflagssamplefractionmask.md)
  A flag that indicates the sample fraction mask.
- [var kLinearPCMFormatFlagsSampleFractionShift: AudioFormatFlags](klinearpcmformatflagssamplefractionshift.md)
  A flag that indicates the bit position of the PCM flag’s 6-bit bitfield.
- [var kAudioFormatFlagsAudioUnitCanonical: AudioFormatFlags](kaudioformatflagsaudiounitcanonical.md)
  The flags for the canonical audio unit and processing sample type.
- [var kAudioFormatFlagsCanonical: AudioFormatFlags](kaudioformatflagscanonical.md)
  The set of flags for the canonical input-output audio sample type.

## See Also

- [struct AudioStreamBasicDescription](audiostreambasicdescription.md)
  A format specification for an audio stream.
- [struct AudioStreamPacketDescription](audiostreampacketdescription.md)
  A value that describes a packet in a buffer of audio data.
- [typealias AudioFormatFlags](audioformatflags.md)
  A type definition for audio format flags.
- [typealias AudioFormatID](audioformatid.md)
  A type definition for audio format identifiers.
- [Audio Format Identifiers](audio-format-identifiers.md)
  Identifiers for supported audio formats.
- [let kAudioStreamAnyRate: Float64](kaudiostreamanyrate.md)
  A value that indicates that an audio stream can use any sample rate.
- [enum MPEG4ObjectID](mpeg4objectid.md)
  Constants that define the type of MPEG-4 audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audio-format-flags)*