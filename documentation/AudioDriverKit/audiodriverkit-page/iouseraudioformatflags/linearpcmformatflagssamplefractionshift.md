# LinearPCMFormatFlagsSampleFractionShift

**Framework**: AudioDriverKit  
**Kind**: case  
**Role**: Enumeration Case

A mask used to calculate the number of fractional bits in the flags field.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
LinearPCMFormatFlagsSampleFractionShift
```

## Discussion

This value completes the following relationship:

```c++
number_fractional_bits = (mFormatFlags & LinearPCMFormatFlagsSampleFractionMask) >> LinearPCMFormatFlagsSampleFractionShift
```

## See Also

### Sample Fraction Flags
- [LinearPCMFormatFlagsSampleFractionMask](./linearpcmformatflagssamplefractionmask.md)
  A constant that indicates the bit position of a bit field within the flags, for use with fixed-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioformatflags/linearpcmformatflagssamplefractionshift)*