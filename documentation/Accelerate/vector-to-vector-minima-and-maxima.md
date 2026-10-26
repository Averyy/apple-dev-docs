# Vector-to-vector minima and maxima

**Framework**: Accelerate  
**Role**: API Collection

Compute the element-wise minimum or maximum values or magnitudes in a vector.

## Topics

### Vector-to-Vector Minima
- [static func minimum<U>(U, U) -> [Double]](./vdsp/minimum%28_,_%29-9t6e4.md)
  Returns a double-precision array containing the minimum of the corresponding values of two vectors.
- [static func minimum<U>(U, U) -> [Float]](./vdsp/minimum%28_,_%29-1rpb2.md)
  Returns a single-precision array containing the minimum of the corresponding values of two vectors.
- [static func minimum<U, V>(U, U, result: inout V)](./vdsp/minimum%28_,_,result%29-1bdzw.md)
  Calculates the double-precision minimum of the corresponding values of two vectors.
- [static func minimum<U, V>(U, U, result: inout V)](./vdsp/minimum%28_,_,result%29-3eh5g.md)
  Calculates the single-precision minimum of the corresponding values of two vectors.
- [vDSP_vmin](./vdsp_vmin.md)
  Calculates the single-precision minimum of the corresponding values of two vectors using specified strides.
- [vDSP_vminD](./vdsp_vmind.md)
  Calculates the double-precision minimum of the corresponding values of two vectors using specified strides.
- [vDSP_vminmg](./vdsp_vminmg.md)
  Calculates the single-precision minimum magnitude of the corresponding values of two vectors using specified strides.
- [vDSP_vminmgD](./vdsp_vminmgd.md)
  Calculates the double-precision minimum magnitude of the corresponding values of two vectors using specified strides.
### Vector-to-Vector Maxima
- [static func maximum<U>(U, U) -> [Double]](./vdsp/maximum%28_,_%29-4sao3.md)
  Returns a double-precision array containing the maximum of the corresponding values of two vectors.
- [static func maximum<U>(U, U) -> [Float]](./vdsp/maximum%28_,_%29-6306m.md)
  Returns a single-precision array containing the maximum of the corresponding values of two vectors.
- [static func maximum<U, V>(U, U, result: inout V)](./vdsp/maximum%28_,_,result%29-1rxz4.md)
  Calculates the maximum of the corresponding double-precision values of two vectors.
- [static func maximum<U, V>(U, U, result: inout V)](./vdsp/maximum%28_,_,result%29-4021u.md)
  Calculates the maximum of the corresponding single-precision values of two vectors.
- [vDSP_vmax](./vdsp_vmax.md)
  Calculates the single-precision maximum of the corresponding values of two vectors using specified strides.
- [vDSP_vmaxD](./vdsp_vmaxd.md)
  Calculates the double-precision maximum of the corresponding values of two vectors using specified strides.
- [vDSP_vmaxmg](./vdsp_vmaxmg.md)
  Calculates the single-precision maximum magnitude of the corresponding values of two vectors using specified strides.
- [vDSP_vmaxmgD](./vdsp_vmaxmgd.md)
  Calculates the double-precision maximum magnitude of the corresponding values of two vectors using specified strides.

## See Also

### Vector-to-vector extrema functions
- [Extrema finding functions](./extrema-finding-functions.md)
  Extract the values from a vector that fall outside a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vector-to-vector-minima-and-maxima)*