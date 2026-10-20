# IOUserAudioFormatFlags

**Framework**: AudioDriverKit  
**Kind**: enum  
**Role**: Enumeration

Flag values that provide more information about the format used by an audio stream basic description.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
enum IOUserAudioFormatFlags : uint32_t;
```

## Topics

### Numeric Representation Flags
- [FormatFlagIsFloat](./iouseraudioformatflags/formatflagisfloat.md)
  A flag to indicate whether samples are floating-point values.
- [LinearPCMFormatFlagIsFloat](./iouseraudioformatflags/linearpcmformatflagisfloat.md)
  A flag to indicate whether PCM samples are floating-point values.
- [FormatFlagIsSignedInteger](./iouseraudioformatflags/formatflagissignedinteger.md)
  A flag to indicate whether samples are signed or unsigned integers.
- [LinearPCMFormatFlagIsSignedInteger](./iouseraudioformatflags/linearpcmformatflagissignedinteger.md)
  A flag to indicate whether PCM samples are signed or unsigned integers.
### Bitwise Layout Flags
- [FormatFlagIsAlignedHigh](./iouseraudioformatflags/formatflagisalignedhigh.md)
  A flag to indicate whether sample bits use the high bits of the channel.
- [LinearPCMFormatFlagIsAlignedHigh](./iouseraudioformatflags/linearpcmformatflagisalignedhigh.md)
  A flag to indicate whether PCM sample bits use the high bits of the channel.
- [FormatFlagIsPacked](./iouseraudioformatflags/formatflagispacked.md)
  A flag to indicate whether sample bits use all available bits of the channel.
- [LinearPCMFormatFlagIsPacked](./iouseraudioformatflags/linearpcmformatflagispacked.md)
  A flag to indicate whether PCM sample bits use all available bits of the channel.
- [FormatFlagsNativeFloatPacked](./iouseraudioformatflags/formatflagsnativefloatpacked.md)
  A flag indicating native-endian packed floating-point values.
### Endianness Flags
- [FormatFlagIsBigEndian](./iouseraudioformatflags/formatflagisbigendian.md)
  A flag to indicate whether samples use big-endian values.
- [LinearPCMFormatFlagIsBigEndian](./iouseraudioformatflags/linearpcmformatflagisbigendian.md)
  A flag to indicate whether PCM samples use big-endian values.
- [FormatFlagsNativeEndian](./iouseraudioformatflags/formatflagsnativeendian.md)
  A flag to indicate whether samples use the platform’s native endianness for its values.
### Apple Lossless Flags
- [AppleLosslessFormatFlag_16BitSourceData](./iouseraudioformatflags/applelosslessformatflag_16bitsourcedata.md)
  A flag to indicate Apple Lossless data that originated from 16-bit native endian-signed integer data.
- [AppleLosslessFormatFlag_20BitSourceData](./iouseraudioformatflags/applelosslessformatflag_20bitsourcedata.md)
  A flag to indicate Apple Lossless data that originated from 20-bit native endian-signed integer data.
- [AppleLosslessFormatFlag_24BitSourceData](./iouseraudioformatflags/applelosslessformatflag_24bitsourcedata.md)
  A flag to indicate Apple Lossless data that originated from 24-bit native endian-signed integer data.
- [AppleLosslessFormatFlag_32BitSourceData](./iouseraudioformatflags/applelosslessformatflag_32bitsourcedata.md)
  A flag to indicate Apple Lossless data that originated from 32-bit native endian-signed integer data.
### Channel Layout Flags
- [FormatFlagIsNonInterleaved](./iouseraudioformatflags/formatflagisnoninterleaved.md)
  A flag to indicate whether the channels interleave their samples in the data.
- [LinearPCMFormatFlagIsNonInterleaved](./iouseraudioformatflags/linearpcmformatflagisnoninterleaved.md)
  A flag to indicate whether PCM channels interleave their samples in the data.
### Mixability Flags
- [FormatFlagIsNonMixable](./iouseraudioformatflags/formatflagisnonmixable.md)
  A flag to indicate whether the format can’t mix.
- [LinearPCMFormatFlagIsNonMixable](./iouseraudioformatflags/linearpcmformatflagisnonmixable.md)
  A flag to indicate whether the PCM format can’t mix.
### Sample Fraction Flags
- [LinearPCMFormatFlagsSampleFractionMask](./iouseraudioformatflags/linearpcmformatflagssamplefractionmask.md)
  A constant that indicates the bit position of a bit field within the flags, for use with fixed-point values.
- [LinearPCMFormatFlagsSampleFractionShift](./iouseraudioformatflags/linearpcmformatflagssamplefractionshift.md)
  A mask used to calculate the number of fractional bits in the flags field.
### Special Purpose Flags
- [FormatFlagsAreAllClear](./iouseraudioformatflags/formatflagsareallclear.md)
  A value indicating that all format flags are clear.
- [LinearPCMFormatFlagsAreAllClear](./iouseraudioformatflags/linearpcmformatflagsareallclear.md)
  A value indicating that all PCM format flags are clear.

## See Also

### Identifying the Format
- [mFormatID](./iouseraudiostreambasicdescription/mformatid.md)
  The audio format identifier indicating the general kind of data in the stream.
- [IOUserAudioFormatID](./iouseraudioformatid.md)
  An enumeration of four character codes used to identify distinct audio data formats.
- [mFormatFlags](./iouseraudiostreambasicdescription/mformatflags.md)
  Audio format flags for the stream’s format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioformatflags)*