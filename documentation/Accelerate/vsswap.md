# vSswap(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Interchanges the elements of two vectors.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vSswap(_ n: Int32, _ x: UnsafeMutablePointer<vFloat>, _ y: UnsafeMutablePointer<vFloat>)
```

#### Discussion

Each element of vector `x` is replaced by the corresponding element of `y`, and vice versa.

## Parameters

- `n`: Number of elements in vectors   and  ; must be a multiple of 4.
- `x`: Vector with   elements of type  .
- `y`: Vector with   elements of type  .

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsswap(_:_:_:))*