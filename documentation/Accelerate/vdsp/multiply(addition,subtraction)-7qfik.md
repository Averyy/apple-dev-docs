# multiply(addition:subtraction:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Returns the double-precision element-wise product of the sum of two vectors and the difference of two vectors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
static func multiply<R, S, T, U>(addition: (a: R, b: S), subtraction: (c: T, d: U)) -> [Double] where R : AccelerateBuffer, S : AccelerateBuffer, T : AccelerateBuffer, U : AccelerateBuffer, R.Element == Double, S.Element == Double, T.Element == Double, U.Element == Double
```

#### Return Value

The output vector `E` in `E = (A + B) * (C - D)`.

#### Discussion

This function calculates the products of the first `N` elements of the addition of vectors `A` and `B` and the subtraction of vectors `C` and `D`, as follows:

```swift
 for (n = 0; n < N; ++n)
    E[n] = (B[n]+A[n]) * (C[n]-D[n]); 
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A, B, C, and D, with three boxes of each. The second row represents the operations that add vectors A and B, and subtract vectors C and D, with three boxes of each. The third row represents the multiplication operation as three boxes.  The bottom row represents the output vector E as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vectors.  ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4337123@2x.png)

The following code shows an example of using this function:

```swift
    let a: [Double] = [ 1,  2,  3,  4,  5]
    let b: [Double] = [10, 20, 30, 40, 50]
    let c: [Double] = [ 5,  4,  3,  2,  1]
    let d: [Double] = [50, 40, 30, 20, 10]
    
    
    let e = vDSP.multiply(addition: (a, b),
                          subtraction: (c, d))
    
    // Prints "[-495.0, -792.0, -891.0, -792.0, -495.0]".
    print(e)

```

## Parameters

- `addition`: A tuple that contains the vectors `A` and `B` in `E = (A + B) * (C - D)`.
- `subtraction`: A tuple that contains the vectors `C` and `D` in `E = (A + B) * (C - D)`.

## See Also

### Multiplication
- [static func multiply<U>(Double, U) -> [Double]](./multiply%28_,_%29-9dxnc.md)
  Returns the double-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U>(T, U) -> [Double]](./multiply%28_,_%29-1ckqt.md)
  Returns the double-precision element-wise product of two vectors.
- [static func multiply<U>(Float, U) -> [Float]](./multiply%28_,_%29-993yp.md)
  Returns the single-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U>(T, U) -> [Float]](./multiply%28_,_%29-9zgw.md)
  Returns the single-precision element-wise product of two vectors.
- [static func multiply<U, V>(Double, U, result: inout V)](./multiply%28_,_,result%29-4xorc.md)
  Calculates the double-precision element-wise product of a vector and a scalar value.
- [static func multiply<U, V>(Float, U, result: inout V)](./multiply%28_,_,result%29-358cn.md)
  Calculates the single-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U, V>(T, U, result: inout V)](./multiply%28_,_,result%29-3ptjl.md)
  Calculates the double-precision element-wise product of two vectors.
- [static func multiply<T, U, V>(T, U, result: inout V)](./multiply%28_,_,result%29-155f3.md)
  Calculates the single-precision element-wise product of two vectors.
- [static func multiply(DSPSplitComplex, by: DSPSplitComplex, count: Int, useConjugate: Bool, result: inout DSPSplitComplex)](./multiply%28_,by,count,useconjugate,result%29-4idx8.md)
  Calculates the product of two complex single-precision vectors, optionally conjugating one of them.
- [static func multiply(DSPDoubleSplitComplex, by: DSPDoubleSplitComplex, count: Int, useConjugate: Bool, result: inout DSPDoubleSplitComplex)](./multiply%28_,by,count,useconjugate,result%29-79r8u.md)
  Calculates the element-wise product of two complex double-precision vectors, optionally conjugating one of them.
- [static func multiply<U>(DSPSplitComplex, by: U, result: inout DSPSplitComplex)](./multiply%28_,by,result%29-8b9eq.md)
  Calculates the double-precision element-wise product of a complex vector and a real vector.
- [static func multiply<U>(DSPDoubleSplitComplex, by: U, result: inout DSPDoubleSplitComplex)](./multiply%28_,by,result%29-8jyhd.md)
  Calculates the single-precision element-wise product of a complex vector and a real vector.
- [static func multiply<T, U>(addition: (a: T, b: U), Double) -> [Double]](./multiply%28addition,_%29-4c9in.md)
  Returns the double-precision element-wise product of the sum of two vectors and a scalar value.
- [static func multiply<S, T, U>(addition: (a: S, b: T), U) -> [Double]](./multiply%28addition,_%29-1wt61.md)
  Returns the double-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<T, U>(addition: (a: T, b: U), Float) -> [Float]](./multiply%28addition,_%29-4fnbx.md)
  Returns the single-precision element-wise product of the sum of two vectors and a scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/multiply(addition:subtraction:)-7qfik)*