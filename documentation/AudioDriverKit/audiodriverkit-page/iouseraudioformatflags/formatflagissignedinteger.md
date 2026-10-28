# FormatFlagIsSignedInteger

**Framework**: AudioDriverKit  
**Kind**: case  
**Role**: Enumeration Case

A flag to indicate whether samples are signed or unsigned integers.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
FormatFlagIsSignedInteger
```

## Discussion

Set this value for signed integers; clear it for unsigned. This flag is only valid if [`FormatFlagIsFloat`](./formatflagisfloat.md) is clear.

## See Also

### Numeric Representation Flags
- [FormatFlagIsFloat](./formatflagisfloat.md)
  A flag to indicate whether samples are floating-point values.
- [LinearPCMFormatFlagIsFloat](./linearpcmformatflagisfloat.md)
  A flag to indicate whether PCM samples are floating-point values.
- [LinearPCMFormatFlagIsSignedInteger](./linearpcmformatflagissignedinteger.md)
  A flag to indicate whether PCM samples are signed or unsigned integers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioformatflags/formatflagissignedinteger)*