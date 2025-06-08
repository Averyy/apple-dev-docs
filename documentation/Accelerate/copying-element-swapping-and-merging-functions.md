# Copying, element swapping, and merging functions

**Framework**: Accelerate

Copy, swap, and merge the elements of two vectors.

## Topics

### Vector copying functions
- [static func copy(DSPSplitComplex, to: inout DSPSplitComplex, count: Int)](vdsp/copy(_:to:count:)-96jr5.md)
  Copies a complex single-precision vector.
- [static func copy(DSPDoubleSplitComplex, to: inout DSPDoubleSplitComplex, count: Int)](vdsp/copy(_:to:count:)-7zpro.md)
  Copies a complex double-precision vector.
- [vDSP_zvmov](vdsp_zvmov.md)
  Moves a complex single-precision vector.
- [vDSP_zvmovD](vdsp_zvmovd.md)
  Moves a complex double-precision vector.
### Vector-to-vector element swapping functions
- [static func swapElements<T, U>(inout T, inout U)](vdsp/swapelements(_:_:)-96xn7.md)
  Swaps the elements of two single-precision vectors.
- [static func swapElements<T, U>(inout T, inout U)](vdsp/swapelements(_:_:)-62wvt.md)
  Swaps the elements of two double-precision vectors.
- [vDSP_vswap](vdsp_vswap.md)
  Swaps the elements of two single-precision vectors using the specified stride.
- [vDSP_vswapD](vdsp_vswapd.md)
  Swaps the elements of two double-precision vectors using the specified stride.
### Vector-to-vector merging functions
- [static func taperedMerge<T, U>(T, U) -> [Float]](vdsp/taperedmerge(_:_:)-5dhoj.md)
  Returns the result of a tapered merge between two single-precision vectors.
- [static func taperedMerge<T, U>(T, U) -> [Double]](vdsp/taperedmerge(_:_:)-9s9j5.md)
  Returns the result of a tapered merge between two double-precision vectors.
- [static func taperedMerge<T, U, V>(T, U, result: inout V)](vdsp/taperedmerge(_:_:result:)-74fuy.md)
  Computes the result of a tapered merge between two single-precision vectors.
- [static func taperedMerge<T, U, V>(T, U, result: inout V)](vdsp/taperedmerge(_:_:result:)-9361o.md)
  Computes the result of a tapered merge between two double-precision vectors.
- [vDSP_vtmerg](vdsp_vtmerg.md)
  Performs a tapered merge between two single-precision vectors.
- [vDSP_vtmergD](vdsp_vtmergd.md)
  Performs a tapered merge between two double-precision vectors.

## See Also

- [Compression and gathering functions](compression-and-gathering-functions.md)
  Compress vectors based on the nonzero elements in a gating vector, or gather vectors based on a separate vector that contains indices.
- [Reversing and sorting functions](reversing-and-sorting-functions.md)
  Perform in-place reverse and sort operations on a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/copying-element-swapping-and-merging-functions)*