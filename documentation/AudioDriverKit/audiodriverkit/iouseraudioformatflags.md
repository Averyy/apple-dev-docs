# IOUserAudioFormatFlags

**Framework**: AudioDriverKit  
**Kind**: enum

Flag values that provide more information about the format used by an audio stream basic description.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
enum IOUserAudioFormatFlags : uint32_t;
```

## Topics

### Numeric Representation Flags
- [FormatFlagIsFloat](audiodriverkit/iouseraudioformatflags/formatflagisfloat.md)
  A flag to indicate whether samples are floating-point values.
- [LinearPCMFormatFlagIsFloat](audiodriverkit/iouseraudioformatflags/linearpcmformatflagisfloat.md)
  A flag to indicate whether PCM samples are floating-point values.
- [FormatFlagIsSignedInteger](audiodriverkit/iouseraudioformatflags/formatflagissignedinteger.md)
  A flag to indicate whether samples are signed or unsigned integers.
- [LinearPCMFormatFlagIsSignedInteger](audiodriverkit/iouseraudioformatflags/linearpcmformatflagissignedinteger.md)
  A flag to indicate whether PCM samples are signed or unsigned integers.
### Bitwise Layout Flags
- [FormatFlagIsAlignedHigh](audiodriverkit/iouseraudioformatflags/formatflagisalignedhigh.md)
  A flag to indicate whether sample bits use the high bits of the channel.
- [LinearPCMFormatFlagIsAlignedHigh](audiodriverkit/iouseraudioformatflags/linearpcmformatflagisalignedhigh.md)
  A flag to indicate whether PCM sample bits use the high bits of the channel.
- [FormatFlagIsPacked](audiodriverkit/iouseraudioformatflags/formatflagispacked.md)
  A flag to indicate whether sample bits use all available bits of the channel.
- [LinearPCMFormatFlagIsPacked](audiodriverkit/iouseraudioformatflags/linearpcmformatflagispacked.md)
  A flag to indicate whether PCM sample bits use all available bits of the channel.
- [FormatFlagsNativeFloatPacked](audiodriverkit/iouseraudioformatflags/formatflagsnativefloatpacked.md)
  A flag indicating native-endian packed floating-point values.
### Endianness Flags
- [FormatFlagIsBigEndian](audiodriverkit/iouseraudioformatflags/formatflagisbigendian.md)
  A flag to indicate whether samples use big-endian values.
- [LinearPCMFormatFlagIsBigEndian](audiodriverkit/iouseraudioformatflags/linearpcmformatflagisbigendian.md)
  A flag to indicate whether PCM samples use big-endian values.
- [FormatFlagsNativeEndian](audiodriverkit/iouseraudioformatflags/formatflagsnativeendian.md)
  A flag to indicate whether samples use the platform’s native endianness for its values.
### Apple Lossless Flags
- [AppleLosslessFormatFlag_16BitSourceData](audiodriverkit/iouseraudioformatflags/applelosslessformatflag_16bitsourcedata.md)
  A flag to indicate Apple Lossless data that originated from 16-bit native endian-signed integer data.
- [AppleLosslessFormatFlag_20BitSourceData](audiodriverkit/iouseraudioformatflags/applelosslessformatflag_20bitsourcedata.md)
  A flag to indicate Apple Lossless data that originated from 20-bit native endian-signed integer data.
- [AppleLosslessFormatFlag_24BitSourceData](audiodriverkit/iouseraudioformatflags/applelosslessformatflag_24bitsourcedata.md)
  A flag to indicate Apple Lossless data that originated from 24-bit native endian-signed integer data.
- [AppleLosslessFormatFlag_32BitSourceData](audiodriverkit/iouseraudioformatflags/applelosslessformatflag_32bitsourcedata.md)
  A flag to indicate Apple Lossless data that originated from 32-bit native endian-signed integer data.
### Channel Layout Flags
- [FormatFlagIsNonInterleaved](audiodriverkit/iouseraudioformatflags/formatflagisnoninterleaved.md)
  A flag to indicate whether the channels interleave their samples in the data.
- [LinearPCMFormatFlagIsNonInterleaved](audiodriverkit/iouseraudioformatflags/linearpcmformatflagisnoninterleaved.md)
  A flag to indicate whether PCM channels interleave their samples in the data.
### Mixability Flags
- [FormatFlagIsNonMixable](audiodriverkit/iouseraudioformatflags/formatflagisnonmixable.md)
  A flag to indicate whether the format can’t mix.
- [LinearPCMFormatFlagIsNonMixable](audiodriverkit/iouseraudioformatflags/linearpcmformatflagisnonmixable.md)
  A flag to indicate whether the PCM format can’t mix.
### Sample Fraction Flags
- [LinearPCMFormatFlagsSampleFractionMask](audiodriverkit/iouseraudioformatflags/linearpcmformatflagssamplefractionmask.md)
  A constant that indicates the bit position of a bit field within the flags, for use with fixed-point values.
- [LinearPCMFormatFlagsSampleFractionShift](audiodriverkit/iouseraudioformatflags/linearpcmformatflagssamplefractionshift.md)
  A mask used to calculate the number of fractional bits in the flags field.
### Special Purpose Flags
- [FormatFlagsAreAllClear](audiodriverkit/iouseraudioformatflags/formatflagsareallclear.md)
  A value indicating that all format flags are clear.
- [LinearPCMFormatFlagsAreAllClear](audiodriverkit/iouseraudioformatflags/linearpcmformatflagsareallclear.md)
  A value indicating that all PCM format flags are clear.

## See Also

- [mFormatID](audiodriverkit/iouseraudiostreambasicdescription/mformatid.md)
  The audio format identifier indicating the general kind of data in the stream.
- [IOUserAudioFormatID](audiodriverkit/iouseraudioformatid.md)
  An enumeration of four character codes used to identify distinct audio data formats.
- [mFormatFlags](audiodriverkit/iouseraudiostreambasicdescription/mformatflags.md)
  Audio format flags for the stream’s format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioformatflags)*