# hypot(x0:x1:y0:y1:result:)

**Framework**: Accelerate  
**Kind**: method

Calculates the double-precision hypotenuses of right triangles with legs that are the differences of corresponding elements of two pairs of vectors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
static func hypot<R, S, T, U, V>(x0: R, x1: S, y0: T, y1: U, result: inout V) where R : AccelerateBuffer, S : AccelerateBuffer, T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, R.Element == Double, S.Element == Double, T.Element == Double, U.Element == Double, V.Element == Double
```

#### Discussion

This function calculates the length of the hypotenuse of  number of triangles, where  is the number of elements in the supplied vectors. The differences between corresponding elements of vectors `x0` and `x1` and vectors `y0` and `y1` define the lengths of the two legs of each triangle.

The functions use the following operation:

```swift
for (n = 0; n < N; ++n)
    E[n] = sqrt((x0[n]-x1[n])**2 + (y0[n]-y1[n])**2);
```

For example, the following code calculates the hypotenuse of four Pythagorean triples:

```swift
    let x0: [Double] = [3, 6, 5, 9]
    let x1: [Double] = [0, 0, 0, 0]
    
    let y0: [Double] = [0, 0, 0, 0]
    let y1: [Double] = [4, 8, 12, 12]
    
    let hypotenuses = [Double](
        unsafeUninitializedCapacity: x0.count) {
            buffer, initializedCount in
            
            vDSP.hypot(x0: x0, x1: x1,
                       y0: y0, y1: y1,
                       result: &buffer)
            
            initializedCount = x0.count
        }
    
    // Prints "[5.0, 10.0, 13.0, 15.0]".
    print(hypotenuses)
```

## Parameters

- `x0`: An array that contains the first values of the first set of legs of the triangles.
- `x1`: An array that contains the second values of the first set of legs of the triangles.
- `y0`: An array that contains the first values of the second set of legs of the triangles.
- `y1`: An array that contains the second values of the second set of legs of the triangles.
- `result`: An array that receives the result of the calculation.

## See Also

- [vDSP_vpythg](vdsp_vpythg.md)
  Calculates the single-precision hypotenuses of right triangles with legs that are the differences of corresponding elements of two pairs of vectors.
- [static func absolute<U>(U) -> [Double]](vdsp/absolute(_:)-9c3ge.md)
  Returns the absolute value of each element in the supplied double-precision vector.
- [static func absolute<U>(U) -> [Float]](vdsp/absolute(_:)-5ehc1.md)
  Returns the absolute value of each element in the supplied single-precision vector.
- [static func absolute<V>(DSPSplitComplex, result: inout V)](vdsp/absolute(_:result:)-9x5jn.md)
  Calculates the absolute value of each element in the supplied single-precision complex vector.
- [static func absolute<V>(DSPDoubleSplitComplex, result: inout V)](vdsp/absolute(_:result:)-1wu9x.md)
  Calculates the absolute value of each element in the supplied double-precision complex vector.
- [static func absolute<U, V>(U, result: inout V)](vdsp/absolute(_:result:)-657bd.md)
  Calculates the absolute value of each element in the supplied double-precision vector.
- [static func absolute<U, V>(U, result: inout V)](vdsp/absolute(_:result:)-4pigo.md)
  Calculates the absolute value of each element in the supplied single-precision vector.
- [static func add<U>(Double, U) -> [Double]](vdsp/add(_:_:)-9mv1a.md)
  Returns the double-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U>(T, U) -> [Double]](vdsp/add(_:_:)-2ftxc.md)
  Returns the double-precision element-wise sum of two vectors.
- [static func add<U>(Float, U) -> [Float]](vdsp/add(_:_:)-53nh9.md)
  Returns the single-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U>(T, U) -> [Float]](vdsp/add(_:_:)-7swvf.md)
  Returns the single-precision element-wise sum of two vectors.
- [static func add<U, V>(Double, U, result: inout V)](vdsp/add(_:_:result:)-2531u.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value.
- [static func add<U, V>(Float, U, result: inout V)](vdsp/add(_:_:result:)-2w0o9.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U, V>(T, U, result: inout V)](vdsp/add(_:_:result:)-338hl.md)
  Calculates the double-precision element-wise sum of two vectors.
- [static func add<T, U, V>(T, U, result: inout V)](vdsp/add(_:_:result:)-3vzwi.md)
  Calculates the single-precision element-wise sum of two vectors.
- [static func add(DSPSplitComplex, to: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](vdsp/add(_:to:count:result:)-g1dk.md)
  Calculates the single-precision elementwise sum of the supplied complex vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/hypot(x0:x1:y0:y1:result:)-4pizr)*