# vSndot(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Computes the dot products of n pairs of vectors, accumulating or storing the results in an array of `n` `float` values.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vSndot(_ n: Int32, _ m: Int32, _ s: UnsafeMutablePointer<Float>, _ isw: Int32, _ x: UnsafePointer<vFloat>, _ y: UnsafePointer<vFloat>)
```

#### Discussion

For i = 0 to n-1, the dot product of vectors `x`[i] and `y`[i] is computed.  The dot product is accumulated or stored in `s`[i], according to the value of `isw`:

- if `isw` = 1, the dot product is stored in `s`[i].
- if `isw` = 2, the dot product is negated and then stored in `s`[i].
- if `isw` = 3, the dot product is added to the value in `s`[i].
- if `isw` = 4, the dot product is negated and then added to the value in `s`[i].

## Parameters

- `n`: Number of dot products to compute, and number of elements in vector   ; must be a multiple of 4.
- `m`: Number of elements in the vectors whose dot products are computed; must be a multiple of 4.
- `s`: Destination vector; the   dot products are accumulated or stored here.
- `isw`: A key that selects one of the four variants of this function: see Discussion below.
- `x`: A matrix whose rows are   floating-point vectors, each containing   values.
- `y`: A second matrix whose rows are   floating-point vectors, each containing   values.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsndot(_:_:_:_:_:_:))*