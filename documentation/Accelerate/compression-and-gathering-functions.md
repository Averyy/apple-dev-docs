# Compression and gathering functions

**Framework**: Accelerate

Compress vectors based on the nonzero elements in a gating vector, or gather vectors based on a separate vector that contains indices.

## Topics

### Vector compression
- [static func compress<T, U>(T, gatingVector: U, nonZeroGatingCount: Int?) -> [Float]](vdsp/compress(_:gatingvector:nonzerogatingcount:)-3c7yk.md)
  Returns a compressed copy of the specified single-precision vector using the nonzero values in a gating vector.
- [static func compress<T, U>(T, gatingVector: U, nonZeroGatingCount: Int?) -> [Double]](vdsp/compress(_:gatingvector:nonzerogatingcount:)-93v23.md)
  Returns a compressed copy of the specified double-precision vector using the nonzero values in a gating vector.
- [static func compress<T, U, V>(T, gatingVector: U, result: inout V)](vdsp/compress(_:gatingvector:result:)-7fvy9.md)
  Compresses the specified single-precision vector using the nonzero values in a gating vector.
- [static func compress<T, U, V>(T, gatingVector: U, result: inout V)](vdsp/compress(_:gatingvector:result:)-2yse4.md)
  Compresses the specified double-precision vector using the nonzero values in a gating vector.
### Vector gathering functions
- [static func gather<T, U>(T, indices: U) -> [Float]](vdsp/gather(_:indices:)-4jwvh.md)
  Returns a gathered copy of the specified single-precision vector using a vector that defines the indices to keep.
- [static func gather<T, U>(T, indices: U) -> [Double]](vdsp/gather(_:indices:)-4yt3o.md)
  Returns a gathered copy of the specified double-precision vector using a vector that defines the indices to keep.
- [static func gather<T, U, V>(T, indices: U, result: inout V)](vdsp/gather(_:indices:result:)-7erii.md)
  Gathers the specified single-precision vector using a vector that defines the indices to keep.
- [static func gather<T, U, V>(T, indices: U, result: inout V)](vdsp/gather(_:indices:result:)-34yzg.md)
  Gathers the specified double-precision vector using a vector that defines the indices to keep.

## See Also

- [Copying, element swapping, and merging functions](copying-element-swapping-and-merging-functions.md)
  Copy, swap, and merge the elements of two vectors.
- [Reversing and sorting functions](reversing-and-sorting-functions.md)
  Perform in-place reverse and sort operations on a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/compression-and-gathering-functions)*