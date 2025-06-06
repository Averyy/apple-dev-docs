# LinearPCMFormatFlagsSampleFractionMask

**Framework**: AudioDriverKit  
**Kind**: case

A constant that indicates the bit position of a bit field within the flags, for use with fixed-point values.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
LinearPCMFormatFlagsSampleFractionMask
```

#### Discussion

The linear PCM flags contain a 6-bit bitfield indicating that the framework should interpret an integer format as fixed point. The value indicates the number of bits used to represent the fractional portion of each sample value. This constant indicates the bit position (counting from the right) of the bitfield in the format flags.

## See Also

- [LinearPCMFormatFlagsSampleFractionShift](audiodriverkit/iouseraudioformatflags/linearpcmformatflagssamplefractionshift.md)
  A mask used to calculate the number of fractional bits in the flags field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioformatflags/linearpcmformatflagssamplefractionmask)*