# kAudioFormatFlagIsPacked

**Framework**: Core Audio Types  
**Kind**: var

A flag that indicates whether placement of the sample bits occupy the entire available bits of the channel.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var kAudioFormatFlagIsPacked: AudioFormatFlags { get }
```

#### Discussion

Set this flag to indicate placement of the sample bits occupy the entire available bits of the channel. Clear this flag to indicate placement of the sample bits either with the high or low bits of the channel.

> ❗ **Important**:  Even if this flag is clear, it’s still implied as set if the description’s fields have this relationship: `((mBitsPerSample / 8) * mChannelsPerFrame) == mBytesPerFrame`.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/kaudioformatflagispacked)*