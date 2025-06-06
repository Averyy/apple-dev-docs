# Audio Stream Basic Description Flags

**Framework**: Core Audio Types

The standard format flags for an audio stream basic description.

#### Overview

When you use an [`AudioStreamBasicDescription`](audiostreambasicdescription.md), the fields describe the complete layout of the sample data in the buffers that the description represents, whereas, typically, an [`AudioBuffer`](audiobuffer.md) in an [`AudioBufferList`](audiobufferlist.md) represents those buffers.

However, when a description has the [`kAudioFormatFlagIsNonInterleaved`](kaudioformatflagisnoninterleaved.md) flag, the audio buffer list has a different structure and semantic. In this case, the description fields describe the format of one of the audio buffers in the list, and each audio buffer in the list has a single (mono) channel of audio data. Then the description’s [`mChannelsPerFrame`](audiostreambasicdescription/mchannelsperframe.md) indicates the total number of audio buffers in the audio buffer list, and each buffer contains one channel. This is primarily for use with the audio unit and audio converter representation of this list, and not the audio hardware usage.

## Topics

### Constants
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

## See Also

- [Anonymous](2962796-anonymous.md)
- [Anonymous](4278542-anonymous.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audio-stream-basic-description-flags)*