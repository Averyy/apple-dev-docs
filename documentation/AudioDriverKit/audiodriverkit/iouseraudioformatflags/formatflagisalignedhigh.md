# FormatFlagIsAlignedHigh

**Framework**: AudioDriverKit  
**Kind**: case

A flag to indicate whether sample bits use the high bits of the channel.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
FormatFlagIsAlignedHigh
```

#### Discussion

Set this value if sample bits use the high end of the channel; clear it to use the low end. This flag is only valid if [`FormatFlagIsPacked`](audiodriverkit/iouseraudioformatflags/formatflagispacked.md) is clear.

## See Also

- [LinearPCMFormatFlagIsAlignedHigh](audiodriverkit/iouseraudioformatflags/linearpcmformatflagisalignedhigh.md)
  A flag to indicate whether PCM sample bits use the high bits of the channel.
- [FormatFlagIsPacked](audiodriverkit/iouseraudioformatflags/formatflagispacked.md)
  A flag to indicate whether sample bits use all available bits of the channel.
- [LinearPCMFormatFlagIsPacked](audiodriverkit/iouseraudioformatflags/linearpcmformatflagispacked.md)
  A flag to indicate whether PCM sample bits use all available bits of the channel.
- [FormatFlagsNativeFloatPacked](audiodriverkit/iouseraudioformatflags/formatflagsnativefloatpacked.md)
  A flag indicating native-endian packed floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioformatflags/formatflagisalignedhigh)*