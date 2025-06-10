# vectorOps

**Framework**: Accelerate

Perform vector and matrix BLAS functions on arrays of 128-bit vectors.

#### Overview

vectorOps.h declares a set of vector and matrix BLAS functions on arrays of 128-bit vectors containing single-precision floating-point values. The arrays can be of any desired length, but the number of `float` elements must be a multiple of 4.

## Topics

### Vector-Scalar Linear Algebra Functions (from vectorOps.h)
- [func vIsamax(Int32, UnsafePointer<vFloat>) -> Int32](visamax(_:_:).md)
  Finds the position of the first vector element having the largest absolute value.
- [func vIsamin(Int32, UnsafePointer<vFloat>) -> Int32](visamin(_:_:).md)
  Finds the position of the first vector element having the smallest absolute value.
- [func vIsmax(Int32, UnsafePointer<vFloat>) -> Int32](vismax(_:_:).md)
  Finds the position of the first vector element having the maximum value.
- [func vIsmin(Int32, UnsafePointer<vFloat>) -> Int32](vismin(_:_:).md)
  Finds the position of the first vector element having the minimum value.
- [func vSasum(Int32, UnsafePointer<vFloat>) -> Float](vsasum(_:_:).md)
  Finds the sum of the absolute values of the elements in a vector.
- [func vSsum(Int32, UnsafePointer<vFloat>) -> Float](vssum(_:_:).md)
  Finds the sum of the values of the elements in a vector.
- [func vSaxpy(Int32, Float, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsaxpy(_:_:_:_:).md)
  Multiplies a vector by a scalar , adds it to a second vector , and stores the result in the second vector.
- [func vSnaxpy(Int32, Int32, UnsafePointer<vFloat>, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsnaxpy(_:_:_:_:_:).md)
  Performs the computation of `vSaxpy` `n` times, using a different multiplier each time.
- [func vScopy(Int32, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vscopy(_:_:_:).md)
  Copies one vector to another.
- [func vSdot(Int32, UnsafePointer<vFloat>, UnsafePointer<vFloat>) -> Float](vsdot(_:_:_:).md)
  Computes the dot product of two vectors.
- [func vSndot(Int32, Int32, UnsafeMutablePointer<Float>, Int32, UnsafePointer<vFloat>, UnsafePointer<vFloat>)](vsndot(_:_:_:_:_:_:).md)
  Computes the dot products of n pairs of vectors, accumulating or storing the results in an array of `n` `float` values.
- [func vSnrm2(Int32, UnsafePointer<vFloat>) -> Float](vsnrm2(_:_:).md)
  Finds the Euclidean length of a vector.
- [func vSnorm2(Int32, UnsafePointer<vFloat>) -> Float](vsnorm2(_:_:).md)
  Finds the Euclidean length of a vector.
- [func vSrot(Int32, UnsafeMutablePointer<vFloat>, UnsafeMutablePointer<vFloat>, Float, Float)](vsrot(_:_:_:_:_:).md)
  Applies planar rotation to a set of n points whose x and y coordinates are contained in two arrays of vectors.
- [func vSscal(Int32, Float, UnsafeMutablePointer<vFloat>)](vsscal(_:_:_:).md)
  Scales a vector in place.
- [func vSswap(Int32, UnsafeMutablePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsswap(_:_:_:).md)
  Interchanges the elements of two vectors.
- [func vSyax(Int32, Float, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsyax(_:_:_:_:).md)
  Multiplies each element of a vector and stores the results in a second vector.
- [func vSzaxpy(Int32, Float, UnsafePointer<vFloat>, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vszaxpy(_:_:_:_:_:).md)
  Multiplies a vector by a scalar, adds it to a second vector, and stores the result in a third vector.
### Matrix-Vector Linear Algebra Functions (from vectorOps.h)
- [func vSgemv(CChar, Int32, Int32, Float, UnsafePointer<vFloat>, UnsafePointer<vFloat>, Float, UnsafeMutablePointer<vFloat>)](vsgemv(_:_:_:_:_:_:_:_:).md)
  Multiplies a vector by a scalar. Multiplies a matrix by another scalar, then by a second vector, and adds the resulting vector to the first vector. This function can also perform the calculation with the transpose of the original matrix instead of the matrix itself. A selector parameter determines whether the transpose is used.
- [func vSgemx(Int32, Int32, Float, UnsafePointer<vFloat>, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsgemx(_:_:_:_:_:_:).md)
  Multiplies a matrix by a scalar and then by a vector, and adds the resulting vector to a second vector.
- [func vSgemtx(Int32, Int32, Float, UnsafePointer<vFloat>, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsgemtx(_:_:_:_:_:_:).md)
  Forms the transpose of a matrix, multiplies it by a scalar and then by a vector, and adds the resulting vector to a second vector.
### Matrix Operations (from vectorOps.h)
- [func vSgeadd(Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](vsgeadd(_:_:_:_:_:_:_:).md)
  Adds two general matrices or their transposes.
- [func vSgesub(Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](vsgesub(_:_:_:_:_:_:_:).md)
  Subtracts two general matrices or their transposes.
- [func vSgemul(Int32, Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](vsgemul(_:_:_:_:_:_:_:_:).md)
  Multiplies two general matrices or their transposes.
- [func vSgemm(Int32, Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>, Float, Float, UnsafeMutablePointer<vFloat>)](vsgemm(_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiples two general matrices or their transposes, then scales and adds a third.
- [func vSgetmi(Int32, UnsafeMutablePointer<vFloat>)](vsgetmi(_:_:).md)
  Transposes a matrix in place.
- [func vSgetmo(Int32, Int32, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsgetmo(_:_:_:_:).md)
  Transposes a matrix out of place.
- [func vSgevv(Int32, Int32, UnsafePointer<vFloat>, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsgevv(_:_:_:_:_:).md)
  Produces the outer product of two vectors and places the results into a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vectorops)*