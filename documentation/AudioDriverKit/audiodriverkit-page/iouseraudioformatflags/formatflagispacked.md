# FormatFlagIsPacked

**Framework**: AudioDriverKit  
**Kind**: case  
**Role**: Enumeration Case

A flag to indicate whether sample bits use all available bits of the channel.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
FormatFlagIsPacked
```

## Discussion

Set this value to use all bits with in the channel; clear to use either the high or low end, as indicated by [`FormatFlagIsAlignedHigh`](./formatflagisalignedhigh.md). Even if this flag is clear, the framework assumes it’s actually set if the [`IOUserAudioStreamBasicDescription`](../iouseraudiostreambasicdescription.md) contains the relationship `((mBitsPerSample / 8) * mChannelsPerFrame) == mBytesPerFrame`.

## See Also

### Bitwise Layout Flags
- [FormatFlagIsAlignedHigh](./formatflagisalignedhigh.md)
  A flag to indicate whether sample bits use the high bits of the channel.
- [LinearPCMFormatFlagIsAlignedHigh](./linearpcmformatflagisalignedhigh.md)
  A flag to indicate whether PCM sample bits use the high bits of the channel.
- [LinearPCMFormatFlagIsPacked](./linearpcmformatflagispacked.md)
  A flag to indicate whether PCM sample bits use all available bits of the channel.
- [FormatFlagsNativeFloatPacked](./formatflagsnativefloatpacked.md)
  A flag indicating native-endian packed floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioformatflags/formatflagispacked)*