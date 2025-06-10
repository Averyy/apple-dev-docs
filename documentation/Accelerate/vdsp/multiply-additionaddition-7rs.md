# multiply(addition:addition:)

**Framework**: Accelerate  
**Kind**: method

Returns the double-precision element-wise product of the sums of two pairs of vectors.

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
static func multiply<S, T, U>(addition additionAB: (a: S, b: T), addition additionCD: (c: U, d: U)) -> [Double] where S : AccelerateBuffer, T : AccelerateBuffer, U : AccelerateBuffer, S.Element == Double, T.Element == Double, U.Element == Double
```

#### Return Value

The output vector `E` in `E = (A + B) * (C + D)`.

#### Discussion

This function calculates the products of the first `N` elements of the addition of vectors `A` and `B` and the addition of vectors `C` and `D`.

```swift
 for (n = 0; n < N; ++n)
    E[n] = (A[n]+B[n]) * (C[n]+D[n]); 
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A, B, C, and D, with three boxes of each. The second row represents the operations that sum vectors A and B, and sum vectors C and D, with three boxes of each. The third row represents the multiplication operation as three boxes.  The bottom row represents the output vector E as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vectors.](https://docs-assets.developer.apple.com/published/43f694c15ca78fe79df15fdc4c7a05f9/media-4337064%402x.png)

The following code shows an example of using this function:

```swift
    let a: [Double] = [ 1,  2,  3,  4,  5]
    let b: [Double] = [10, 20, 30, 40, 50]
    let c: [Double] = [ 5,  4,  3,  2,  1]
    let d: [Double] = [50, 40, 30, 20, 10]
    
    let e = vDSP.multiply(addition: (a, b),
                          addition: (c, d))
    
    // Prints "[605.0, 968.0, 1089.0, 968.0, 605.0]".
    print(e)

```

## Parameters

- `additionAB`: A tuple that contains the vectors   and   in  .
- `additionCD`: A tuple that contains the vectors   and   in  .

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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/multiply(addition:addition:)-7rs)*