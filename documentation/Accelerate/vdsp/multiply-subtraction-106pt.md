# multiply(subtraction:_:)

**Framework**: Accelerate  
**Kind**: method

Returns the single-precision element-wise product of the difference of two vectors and a scalar value.

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
static func multiply<T, U>(subtraction: (a: T, b: U), _ scalar: Float) -> [Float] where T : AccelerateBuffer, U : AccelerateBuffer, T.Element == Float, U.Element == Float
```

## Mentions

- [Using vDSP for vector-based arithmetic](using-vdsp-for-vector-based-arithmetic.md)

#### Return Value

The output vector `D` in `D = (A - B) * C`.

#### Discussion

This function calculates the element-wise difference of vectors `A` and `B`, multiplies the difference by scalar value `C`, and writes the result to vector `D`.

```swift
 for (n = 0; n < N; ++n)
    D[n] = (A[n] - B[n]) * C;
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A and B, with three boxes of each. The second row frepresents the operation that subtracts B from A, with three boxes, as well as the input scalar C with one box. The third row represents the multiplication operation as three boxes. The bottom row represents the output vector D as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vector. ](https://docs-assets.developer.apple.com/published/fc305c66e64754bd03a5d1cf24d30eda/media-4387356%402x.png)

The following code shows an example of using this function:

```swift
    let a: [Float] = [ 1,  2,  3,  4,  5]
    let b: [Float] = [10, 20, 30, 40, 50]
    let c: Float = 5
    
    let d = vDSP.multiply(subtraction: (a, b),
                          c)
    
    // Prints "[-45.0, -90.0, -135.0, -180.0, -225.0]".
    print(d)
```

## Parameters

- `subtraction`: A tuple that contains the vectors   and   in  .
- `scalar`: The input scalar value   in  .

## See Also

- [static func multiply<U>(Double, U) -> [Double]](vdsp/multiply(_:_:)-9dxnc.md)
  Returns the double-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U>(T, U) -> [Double]](vdsp/multiply(_:_:)-1ckqt.md)
  Returns the double-precision element-wise product of two vectors.
- [static func multiply<U>(Float, U) -> [Float]](vdsp/multiply(_:_:)-993yp.md)
  Returns the single-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U>(T, U) -> [Float]](vdsp/multiply(_:_:)-9zgw.md)
  Returns the single-precision element-wise product of two vectors.
- [static func multiply<U, V>(Double, U, result: inout V)](vdsp/multiply(_:_:result:)-4xorc.md)
  Calculates the double-precision element-wise product of a vector and a scalar value.
- [static func multiply<U, V>(Float, U, result: inout V)](vdsp/multiply(_:_:result:)-358cn.md)
  Calculates the single-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U, V>(T, U, result: inout V)](vdsp/multiply(_:_:result:)-3ptjl.md)
  Calculates the double-precision element-wise product of two vectors.
- [static func multiply<T, U, V>(T, U, result: inout V)](vdsp/multiply(_:_:result:)-155f3.md)
  Calculates the single-precision element-wise product of two vectors.
- [static func multiply(DSPSplitComplex, by: DSPSplitComplex, count: Int, useConjugate: Bool, result: inout DSPSplitComplex)](vdsp/multiply(_:by:count:useconjugate:result:)-4idx8.md)
  Calculates the product of two complex single-precision vectors, optionally conjugating one of them.
- [static func multiply(DSPDoubleSplitComplex, by: DSPDoubleSplitComplex, count: Int, useConjugate: Bool, result: inout DSPDoubleSplitComplex)](vdsp/multiply(_:by:count:useconjugate:result:)-79r8u.md)
  Calculates the elementwise product of two complex double-precision vectors, optionally conjugating one of them.
- [static func multiply<U>(DSPSplitComplex, by: U, result: inout DSPSplitComplex)](vdsp/multiply(_:by:result:)-8b9eq.md)
  Calculates the double-precision elementwise product of a complex vector and a real vector.
- [static func multiply<U>(DSPDoubleSplitComplex, by: U, result: inout DSPDoubleSplitComplex)](vdsp/multiply(_:by:result:)-8jyhd.md)
  Calculates the single-precision elementwise product of a complex vector and a real vector.
- [static func multiply<T, U>(addition: (a: T, b: U), Double) -> [Double]](vdsp/multiply(addition:_:)-4c9in.md)
  Returns the double-precision element-wise product of the sum of two vectors and a scalar value.
- [static func multiply<S, T, U>(addition: (a: S, b: T), U) -> [Double]](vdsp/multiply(addition:_:)-1wt61.md)
  Returns the double-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<T, U>(addition: (a: T, b: U), Float) -> [Float]](vdsp/multiply(addition:_:)-4fnbx.md)
  Returns the single-precision element-wise product of the sum of two vectors and a scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/multiply(subtraction:_:)-106pt)*