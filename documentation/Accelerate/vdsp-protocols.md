# vDSP Protocols

**Framework**: Accelerate

Protocols that support Swift implementations of vDSP operations.

## Topics

### Essentials
- [protocol AccelerateBuffer](acceleratebuffer.md)
  A type that represents an immutable buffer.
- [protocol AccelerateMutableBuffer](acceleratemutablebuffer.md)
  A type that represents a mutable buffer.
- [protocol AccelerateMatrixBuffer](acceleratematrixbuffer.md)
- [protocol AccelerateMutableMatrixBuffer](acceleratemutablematrixbuffer.md)
- [enum AccelerateMatrixOrder](acceleratematrixorder.md)
### Fourier Transform
- [protocol vDSP_DFTFunctions](vdsp_dftfunctions.md)
  A protocol that defines functions for discrete Fourier transform operations.
- [protocol vDSP_FloatingPointDiscreteFourierTransformable](vdsp_floatingpointdiscretefouriertransformable.md)
  Types that support discrete Fourier transform operations.
- [protocol vDSP_FourierTransformFunctions](vdsp_fouriertransformfunctions.md)
  A protocol that defines functions for fast Fourier transform operations.
- [protocol vDSP_FourierTransformable](vdsp_fouriertransformable.md)
  Types that support fast Fourier transform operations.
- [protocol vDSP_DiscreteFourierTransformable](vdsp_discretefouriertransformable.md)
- [protocol vDSP_DiscreteTransformLifecycleFunctions](vdsp_discretetransformlifecyclefunctions.md)
### Biquadratic Filtering
- [protocol vDSP_BiquadFunctions](vdsp_biquadfunctions.md)
  A protocol that defines functions for biquadratic filtering.
- [protocol vDSP_FloatingPointBiquadFilterable](vdsp_floatingpointbiquadfilterable.md)
  Types that support biquadratic filtering.
### Type Conversion
- [protocol vDSP_FloatingPointConvertable](vdsp_floatingpointconvertable.md)
  Types that are convertible from integer values.
- [protocol vDSP_IntegerConvertable](vdsp_integerconvertable.md)
  Types that are convertible from floating point values.
### Vector Generation
- [protocol vDSP_FloatingPointGeneratable](vdsp_floatingpointgeneratable.md)
  Types that support vectorized window generation.

## See Also

- [enum vDSP](vdsp.md)
  An enumeration that acts as a namespace for Swift overlays to vDSP.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp-protocols)*