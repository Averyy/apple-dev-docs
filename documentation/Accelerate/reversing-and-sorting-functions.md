# Reversing and sorting functions

**Framework**: Accelerate

Perform in-place reverse and sort operations on a vector.

## Topics

### Vector reversing functions
- [static func reverse<V>(inout V)](vdsp/reverse(_:)-38ptd.md)
  Reverses a vector of single-precision values in-place.
- [static func reverse<V>(inout V)](vdsp/reverse(_:)-3aq38.md)
  Reverses a vector of double-precision values in-place.
- [vDSP_vrvrs](vdsp_vrvrs.md)
  Performs an in-place reversal of a single-precision vector.
- [vDSP_vrvrsD](vdsp_vrvrsd.md)
  Performs an in-place reversal of a double-precision vector.
### Vector sorting functions
- [static func sort<V>(inout V, sortOrder: vDSP.SortOrder)](vdsp/sort(_:sortorder:)-wx0w.md)
  Sorts a vector of single-precision values in-place.
- [static func sort<V>(inout V, sortOrder: vDSP.SortOrder)](vdsp/sort(_:sortorder:)-418g0.md)
  Sorts a vector of double-precision values in-place.
- [vDSP.SortOrder](vdsp/sortorder.md)
  Constants that specify the sorting order.
- [vDSP_vsort](vdsp_vsort.md)
  Performs an in-place sort of a single-precision vector.
- [vDSP_vsortD](vdsp_vsortd.md)
  Performs an in-place sort of a double-precision vector.
- [vDSP_vsorti](vdsp_vsorti.md)
  Performs an in-place sort of the indices into a single-precision vector.
- [vDSP_vsortiD](vdsp_vsortid.md)
  Performs an in-place sort of the indices into a double-precision vector.

## See Also

- [Compression and gathering functions](compression-and-gathering-functions.md)
  Compress vectors based on the nonzero elements in a gating vector, or gather vectors based on a separate vector that contains indices.
- [Copying, element swapping, and merging functions](copying-element-swapping-and-merging-functions.md)
  Copy, swap, and merge the elements of two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/reversing-and-sorting-functions)*