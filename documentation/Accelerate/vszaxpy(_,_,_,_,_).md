# vSzaxpy(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Multiplies a vector by a scalar, adds it to a second vector, and stores the result in a third vector.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use vDSP_vsma instead

## Declaration

```swift
func vSzaxpy(_ n: Int32, _ alpha: Float, _ x: UnsafePointer<vFloat>, _ y: UnsafePointer<vFloat>, _ z: UnsafeMutablePointer<vFloat>)
```

```c
extern void vSzaxpy(int32_t n, float alpha, const vFloat *x, const vFloat *y, vFloat *z);
```

## Discussion

Each element of vector `x` is multiplied by `alpha`, then the corresponding element of `yY` is added. Results are stored in the corresponding elements of `z`.

## Parameters

- `n`: Number of elements in vectors `x`, `y`, and `z`; must be a multiple of 4.
- `alpha`: Multiplier.
- `x`: Source vector with `n` elements of type `float`.
- `y`: Source vector with `n` elements of type `float`.
- `z`: Source vector with `n` elements of type `float`.

## See Also

### Vector-Scalar Linear Algebra Functions (from vectorOps.h)
- [func vIsamax(Int32, UnsafePointer<vFloat>) -> Int32](./visamax%28_,_%29.md)
  Finds the position of the first vector element having the largest absolute value.
- [func vIsamin(Int32, UnsafePointer<vFloat>) -> Int32](./visamin%28_,_%29.md)
  Finds the position of the first vector element having the smallest absolute value.
- [func vIsmax(Int32, UnsafePointer<vFloat>) -> Int32](./vismax%28_,_%29.md)
  Finds the position of the first vector element having the maximum value.
- [func vIsmin(Int32, UnsafePointer<vFloat>) -> Int32](./vismin%28_,_%29.md)
  Finds the position of the first vector element having the minimum value.
- [func vSasum(Int32, UnsafePointer<vFloat>) -> Float](./vsasum%28_,_%29.md)
  Finds the sum of the absolute values of the elements in a vector.
- [func vSsum(Int32, UnsafePointer<vFloat>) -> Float](./vssum%28_,_%29.md)
  Finds the sum of the values of the elements in a vector.
- [func vSaxpy(Int32, Float, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](./vsaxpy%28_,_,_,_%29.md)
  Multiplies a vector by a scalar , adds it to a second vector , and stores the result in the second vector.
- [func vSnaxpy(Int32, Int32, UnsafePointer<vFloat>, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](./vsnaxpy%28_,_,_,_,_%29.md)
  Performs the computation of `vSaxpy` `n` times, using a different multiplier each time.
- [func vScopy(Int32, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](./vscopy%28_,_,_%29.md)
  Copies one vector to another.
- [func vSdot(Int32, UnsafePointer<vFloat>, UnsafePointer<vFloat>) -> Float](./vsdot%28_,_,_%29.md)
  Computes the dot product of two vectors.
- [func vSndot(Int32, Int32, UnsafeMutablePointer<Float>, Int32, UnsafePointer<vFloat>, UnsafePointer<vFloat>)](./vsndot%28_,_,_,_,_,_%29.md)
  Computes the dot products of n pairs of vectors, accumulating or storing the results in an array of `n` `float` values.
- [func vSnrm2(Int32, UnsafePointer<vFloat>) -> Float](./vsnrm2%28_,_%29.md)
  Finds the Euclidean length of a vector.
- [func vSnorm2(Int32, UnsafePointer<vFloat>) -> Float](./vsnorm2%28_,_%29.md)
  Finds the Euclidean length of a vector.
- [func vSrot(Int32, UnsafeMutablePointer<vFloat>, UnsafeMutablePointer<vFloat>, Float, Float)](./vsrot%28_,_,_,_,_%29.md)
  Applies planar rotation to a set of n points whose x and y coordinates are contained in two arrays of vectors.
- [func vSscal(Int32, Float, UnsafeMutablePointer<vFloat>)](./vsscal%28_,_,_%29.md)
  Scales a vector in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vszaxpy(_:_:_:_:_:))*