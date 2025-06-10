# subtract(multiplication:multiplication:)

**Framework**: Accelerate  
**Kind**: method

Returns the double-precision element-wise difference of the products of two pairs of vectors.

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
static func subtract<R, S, T, U>(multiplication multiplicationAB: (a: T, b: U), multiplication multiplicationCD: (c: R, d: S)) -> [Double] where R : AccelerateBuffer, S : AccelerateBuffer, T : AccelerateBuffer, U : AccelerateBuffer, R.Element == Double, S.Element == Double, T.Element == Double, U.Element == Double
```

#### Return Value

The output vector `E` in `E = (A * B) - (C * D)`.

#### Discussion

This function calculates the differences of the first `N` elements of the product of vectors `A` and `B` and the product of vectors `C` and `D`.

```swift
 for (n = 0; n < N; ++n)
    E[n] = A[n]*B[n] - C[n]*D[n]; 
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A, B, C, and D, with three boxes of each. The second row represents the operations that multiply vectors A and B, and multiply vectors C and D, with three boxes of each. The third row represents the subtraction operation as three boxes.  The bottom row represents the output vector E as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vectors. ](https://docs-assets.developer.apple.com/published/39d89329286f14952e7b03fb1b3f22de/media-4337031%402x.png)

The following code shows an example of using this function:

```swift
    let a: [Double] = [ 1,  2,  3,  4,  5]
    let b: [Double] = [10, 20, 30, 40, 50]
    let c: [Double] = [ 5,  4,  3,  2,  1]
    let d: [Double] = [50, 40, 30, 20, 10]
    
    let e = vDSP.subtract(multiplication: (a, b),
                          multiplication: (c, d))
    
    // Prints "[-240.0, -120.0, 0.0, 120.0, 240.0]".
    print(e)

```

## Parameters

- `multiplicationAB`: A tuple that contains the vectors   and   in  .
- `multiplicationCD`: A tuple that contains the vectors   and   in  .

## See Also

- [static func subtract<T, U>(U, T) -> [Double]](vdsp/subtract(_:_:)-8o5ai.md)
  Returns the double-precision element-wise subtraction of two vectors.
- [static func subtract<T, U>(U, T) -> [Float]](vdsp/subtract(_:_:)-9xmo8.md)
  Returns the single-precision element-wise subtraction of two vectors.
- [static func subtract<T, U, V>(U, T, result: inout V)](vdsp/subtract(_:_:result:)-1ianx.md)
  Calculates the double-precision element-wise subtraction of two vectors.
- [static func subtract<T, U, V>(U, T, result: inout V)](vdsp/subtract(_:_:result:)-2p3fa.md)
  Calculates the single-precision element-wise subtraction of two vectors.
- [static func subtract(DSPSplitComplex, from: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](vdsp/subtract(_:from:count:result:)-4p5xd.md)
  Calculates the single-precision elementwise subtraction of a complex vector from a complex vector.
- [static func subtract(DSPDoubleSplitComplex, from: DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](vdsp/subtract(_:from:count:result:)-80zi9.md)
  Calculates the double-precision elementwise subtraction of a complex vector from a complex vector.
- [static func subtract<T, U>(multiplication: (a: U, b: Double), T) -> [Double]](vdsp/subtract(multiplication:_:)-2hhme.md)
  Calculates the double-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U>(multiplication: (a: T, b: U), S) -> [Double]](vdsp/subtract(multiplication:_:)-9gphg.md)
  Returns the double-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<T, U>(multiplication: (a: U, b: Float), T) -> [Float]](vdsp/subtract(multiplication:_:)-3zm6l.md)
  Calculates the single-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U>(multiplication: (a: T, b: U), S) -> [Float]](vdsp/subtract(multiplication:_:)-6u3sp.md)
  Returns the single-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<T, U, V>(multiplication: (a: U, b: Double), T, result: inout V)](vdsp/subtract(multiplication:_:result:)-9p12h.md)
  Calculates the double-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<T, U, V>(multiplication: (a: U, b: Float), T, result: inout V)](vdsp/subtract(multiplication:_:result:)-86gx3.md)
  Calculates the single-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U, V>(multiplication: (a: T, b: U), S, result: inout V)](vdsp/subtract(multiplication:_:result:)-3f2bw.md)
  Calculates the double-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<S, T, U, V>(multiplication: (a: T, b: U), S, result: inout V)](vdsp/subtract(multiplication:_:result:)-6b91s.md)
  Calculates the single-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<R, S, T, U>(multiplication: (a: T, b: U), multiplication: (c: R, d: S)) -> [Float]](vdsp/subtract(multiplication:multiplication:)-1ghyu.md)
  Returns the single-precision element-wise difference of the products of two pairs of vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/subtract(multiplication:multiplication:)-22a4b)*