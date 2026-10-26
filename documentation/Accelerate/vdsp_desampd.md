# vDSP_desampD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs double-precision FIR filtering with decimation and antialiasing.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_desampD(const double *__A, vDSP_Stride __DF, const double *__F, double *__C, vDSP_Length __N, vDSP_Length __P);
```

## Mentions

- [Resampling a signal with decimation](./resampling-a-signal-with-decimation.md)

#### Discussion

This is the same as [`vDSP_desamp`](./vdsp_desamp.md), except for the types of the `A`, `F`, and `C` parameters.

## See Also

### Real Vectors
- [Resampling a signal with decimation](./resampling-a-signal-with-decimation.md)
  Reduce the sample rate of a signal by specifying a decimation factor and applying a custom antialiasing filter.
- [vDSP_desamp](./vdsp_desamp.md)
  Performs single-precision FIR filtering with decimation and antialiasing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_desampd)*