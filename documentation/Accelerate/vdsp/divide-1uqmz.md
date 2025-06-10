# divide(_:_:)

**Framework**: Accelerate  
**Kind**: method

Calculates the single-precision element-wise division of a vector and a scalar value.

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
static func divide<U>(_ vector: U, _ scalar: Float) -> [Float] where U : AccelerateBuffer, U.Element == Float
```

## Mentions

- [Using vDSP for vector-based arithmetic](using-vdsp-for-vector-based-arithmetic.md)

#### Return Value

The output vector, `C`.

#### Discussion

This function calculates the element-wise division of vector `A` and scalar value `B`, and writes the result to vector `C`.

```swift
 for (n = 0; n < N; ++n)
    C[n] = A[n] / B;
```

![A diagram showing the operation of this function. There are three rows. The top row represents the input vector A with three boxes, and the scalar value B with one box. The middle row represents the operation as three boxes with division signs. The bottom row represents the output vector C as three boxes. The diagram has connecting lines from the input vectors to the operation, and from the operation to the output vector.](https://docs-assets.developer.apple.com/published/8c8f0f67f125aded76822f745564ccff/media-4337210%402x.png)

The following code shows an example of using this function:

```swift
    let a: [Float] = [1, 2, 3, 4, 5]
    let b: Float = 10
    
    let c = vDSP.divide(a, b)
    
    // Prints "[0.1, 0.2, 0.3, 0.4, 0.5]".
    print(c)
```

## Parameters

- `vector`: The input vector,  .
- `scalar`: The input scalar value,  .

## See Also

- [static func divide<U>(Double, U) -> [Double]](vdsp/divide(_:_:)-73m8v.md)
  Returns the double-precision element-wise division of a scalar value and a vector.
- [static func divide<U>(U, Double) -> [Double]](vdsp/divide(_:_:)-9nb4j.md)
  Calculates the double-precision element-wise division of a vector and a scalar value.
- [static func divide<T, U>(T, U) -> [Double]](vdsp/divide(_:_:)-8swnm.md)
  Returns the double-precision element-wise division of two vectors.
- [static func divide<U>(Float, U) -> [Float]](vdsp/divide(_:_:)-70npt.md)
  Returns the single-precision element-wise division of a scalar value and a vector.
- [static func divide<T, U>(T, U) -> [Float]](vdsp/divide(_:_:)-6nfsi.md)
  Returns the single-precision element-wise division of two vectors.
- [static func divide<U, V>(Double, U, result: inout V)](vdsp/divide(_:_:result:)-18qa3.md)
  Calculates the double-precision element-wise division of a scalar value and a vector.
- [static func divide<U, V>(Float, U, result: inout V)](vdsp/divide(_:_:result:)-3emlk.md)
  Calculates the single-precision element-wise division of a scalar value and a vector.
- [static func divide<U, V>(U, Double, result: inout V)](vdsp/divide(_:_:result:)-44mff.md)
  Calculates the double-precision element-wise division of a vector and a scalar value.
- [static func divide<U, V>(U, Float, result: inout V)](vdsp/divide(_:_:result:)-5hwb2.md)
  Calculates the single-precision element-wise division of a vector and a scalar value.
- [static func divide<T, U, V>(T, U, result: inout V)](vdsp/divide(_:_:result:)-6gtmm.md)
  Calculates the double-precision element-wise division of two vectors.
- [static func divide<T, U, V>(T, U, result: inout V)](vdsp/divide(_:_:result:)-7ejy9.md)
  Calculates the single-precision element-wise division of two vectors.
- [static func divide(DSPSplitComplex, by: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](vdsp/divide(_:by:count:result:)-9chz5.md)
  Calculates the single-precision elementwise division of a complex vector by a complex vector.
- [static func divide(DSPDoubleSplitComplex, by: DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](vdsp/divide(_:by:count:result:)-57jlj.md)
  Calculates the double-precision elementwise division of a complex vector by a complex vector.
- [static func divide<U>(DSPSplitComplex, by: U, result: inout DSPSplitComplex)](vdsp/divide(_:by:result:)-66qch.md)
  Calculates the single-precision elementwise division of a complex vector by a real vector.
- [static func divide<U>(DSPDoubleSplitComplex, by: U, result: inout DSPDoubleSplitComplex)](vdsp/divide(_:by:result:)-402v9.md)
  Calculates the double-precision elementwise division of a complex vector by a complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/divide(_:_:)-1uqmz)*