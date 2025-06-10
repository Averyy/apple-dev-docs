# vSaxpy(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Multiplies a vector by a scalar , adds it to a second vector , and stores the result in the second vector.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vSaxpy(_ n: Int32, _ alpha: Float, _ x: UnsafePointer<vFloat>, _ y: UnsafeMutablePointer<vFloat>)
```

#### Discussion

The elements of `x` are multiplied by `alpha` and added to the corresponding elements of `y`.  The results are stored in `y`.

## Parameters

- `n`: Number of elements in each of the vectors   and  ; must be a multiple of 4.
- `alpha`: A multiplier for the vector  .
- `x`: A vector array of   values.
- `y`: A second vector array of   values.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsaxpy(_:_:_:_:))*