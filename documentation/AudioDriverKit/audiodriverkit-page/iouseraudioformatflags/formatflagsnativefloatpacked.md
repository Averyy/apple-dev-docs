# FormatFlagsNativeFloatPacked

**Framework**: AudioDriverKit  
**Kind**: case  
**Role**: Enumeration Case

A flag indicating native-endian packed floating-point values.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
FormatFlagsNativeFloatPacked
```

## Discussion

This convienence flag set the [`FormatFlagIsFloat`](./formatflagisfloat.md), [`FormatFlagsNativeEndian`](./formatflagsnativeendian.md), and [`FormatFlagIsPacked`](./formatflagispacked.md) flags.

## See Also

### Bitwise Layout Flags
- [FormatFlagIsAlignedHigh](./formatflagisalignedhigh.md)
  A flag to indicate whether sample bits use the high bits of the channel.
- [LinearPCMFormatFlagIsAlignedHigh](./linearpcmformatflagisalignedhigh.md)
  A flag to indicate whether PCM sample bits use the high bits of the channel.
- [FormatFlagIsPacked](./formatflagispacked.md)
  A flag to indicate whether sample bits use all available bits of the channel.
- [LinearPCMFormatFlagIsPacked](./linearpcmformatflagispacked.md)
  A flag to indicate whether PCM sample bits use all available bits of the channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioformatflags/formatflagsnativefloatpacked)*