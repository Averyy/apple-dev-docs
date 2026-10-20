# vSndot(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Computes the dot products of n pairs of vectors, accumulating or storing the results in an array of `n` `float` values.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use cblas_sdot or vDSP_dotpr in a loop instead

## Declaration

```swift
func vSndot(_ n: Int32, _ m: Int32, _ s: UnsafeMutablePointer<Float>, _ isw: Int32, _ x: UnsafePointer<vFloat>, _ y: UnsafePointer<vFloat>)
```

```c
extern void vSndot(int32_t n, int32_t m, float *s, int32_t isw, const vFloat *x, const vFloat *y);
```

#### Discussion

For i = 0 to n-1, the dot product of vectors `x`[i] and `y`[i] is computed.  The dot product is accumulated or stored in `s`[i], according to the value of `isw`:

- if `isw` = 1, the dot product is stored in `s`[i].
- if `isw` = 2, the dot product is negated and then stored in `s`[i].
- if `isw` = 3, the dot product is added to the value in `s`[i].
- if `isw` = 4, the dot product is negated and then added to the value in `s`[i].

## Parameters

- `n`: Number of dot products to compute, and number of elements in vector `s` ; must be a multiple of 4.
- `m`: Number of elements in the vectors whose dot products are computed; must be a multiple of 4.
- `s`: Destination vector; the `n` dot products are accumulated or stored here.
- `isw`: A key that selects one of the four variants of this function: see Discussion below.
- `x`: A matrix whose rows are `n` floating-point vectors, each containing `m` values.
- `y`: A second matrix whose rows are `n` floating-point vectors, each containing `m` values.

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
- [func vSnrm2(Int32, UnsafePointer<vFloat>) -> Float](./vsnrm2%28_,_%29.md)
  Finds the Euclidean length of a vector.
- [func vSnorm2(Int32, UnsafePointer<vFloat>) -> Float](./vsnorm2%28_,_%29.md)
  Finds the Euclidean length of a vector.
- [func vSrot(Int32, UnsafeMutablePointer<vFloat>, UnsafeMutablePointer<vFloat>, Float, Float)](./vsrot%28_,_,_,_,_%29.md)
  Applies planar rotation to a set of n points whose x and y coordinates are contained in two arrays of vectors.
- [func vSscal(Int32, Float, UnsafeMutablePointer<vFloat>)](./vsscal%28_,_,_%29.md)
  Scales a vector in place.
- [func vSswap(Int32, UnsafeMutablePointer<vFloat>, UnsafeMutablePointer<vFloat>)](./vsswap%28_,_,_%29.md)
  Interchanges the elements of two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsndot(_:_:_:_:_:_:))*