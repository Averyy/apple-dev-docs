# LinearPCMFormatFlagsSampleFractionShift

**Framework**: AudioDriverKit  
**Kind**: case

A mask used to calculate the number of fractional bits in the flags field.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
LinearPCMFormatFlagsSampleFractionShift
```

#### Discussion

This value completes the following relationship:

```c++
number_fractional_bits = (mFormatFlags & LinearPCMFormatFlagsSampleFractionMask) >> LinearPCMFormatFlagsSampleFractionShift
```

## See Also

- [LinearPCMFormatFlagsSampleFractionMask](audiodriverkit/iouseraudioformatflags/linearpcmformatflagssamplefractionmask.md)
  A constant that indicates the bit position of a bit field within the flags, for use with fixed-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioformatflags/linearpcmformatflagssamplefractionshift)*