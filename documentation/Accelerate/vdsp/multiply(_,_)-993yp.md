# multiply(_:_:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Returns the single-precision element-wise product of a vector and a scalar value.

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
static func multiply<U>(_ scalar: Float, _ vector: U) -> [Float] where U : AccelerateBuffer, U.Element == Float
```

## Mentions

- [Using vDSP for vector-based arithmetic](../using-vdsp-for-vector-based-arithmetic.md)

## Return Value

The output vector, `C`.

## Discussion

This function calculates the element-wise product of vector `A` and scalar value `B`, and writes the result to vector `C`, as follows:

```swift
 for (n = 0; n < N; ++n)
    C[n] = A[n] * B;
```

![A diagram showing the operation of this function. There are three rows. The top row represents the input vector A with three boxes, and the scalar value B with one box. The middle row represents the operation as three boxes with multiplication signs. The bottom row represents the output vector C as three boxes. The diagram has connecting lines from the input vectors to the operation, and from the operation to the output vector.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4337183@2x.png)

The following code shows an example of using this function:

```swift
    let a: [Float] = [1, 2, 3, 4, 5]
    let b: Float = 10
    
    let c = vDSP.multiply(b, a)
    
    // Prints "[10.0, 20.0, 30.0, 40.0, 50.0]".
    print(c)
```

## Parameters

- `scalar`: The input scalar value, `B`.
- `vector`: The input vector, `A`.

## See Also

### Multiplication
- [static func multiply<U>(Double, U) -> [Double]](./multiply%28_,_%29-9dxnc.md)
  Returns the double-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U>(T, U) -> [Double]](./multiply%28_,_%29-1ckqt.md)
  Returns the double-precision element-wise product of two vectors.
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
- [static func multiply<S, T, U>(addition: (a: S, b: T), U) -> [Float]](./multiply%28addition,_%29-7t59.md)
  Returns the single-precision element-wise product of a vector and the sum of two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/multiply(_:_:)-993yp)*