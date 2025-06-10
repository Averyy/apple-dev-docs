# divide(_:_:result:)

**Framework**: Accelerate  
**Kind**: method

Calculates the double-precision element-wise division of two vectors.

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
static func divide<T, U, V>(_ vectorA: T, _ vectorB: U, result: inout V) where T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, T.Element == Double, U.Element == Double, V.Element == Double
```

#### Discussion

This function calculates the division of the first `N` elements of input vectors `A` and `B`, and writes the result to output vector `C`.

```swift
 for (n = 0; n < N; ++n)
    C[n] = A[n] / B[n];
```

![A diagram showing the operation of this function. There are three rows. The top row represents the input vectors, A and B, with three boxes of each. The middle row represents the operation as three boxes with division signs. The bottom row represents the output vector C as three boxes. The diagram has connecting lines from the input vectors to the operation, and from the operation to the output vectors.](https://docs-assets.developer.apple.com/published/d1e83c4f0c951b49402b99e2581eb228/media-4336921%402x.png)

The following code shows an example of using this function:

```swift
    let count = 5
    
    let a: [Double] = [10, 20, 30, 40, 50]
    let b: [Double] = [ 1,  2,  3,  4,  5]
    
    let c = [Double](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP.divide(a, b,
                    result: &buffer)
        
        initializedCount = count
    }
    
    // Prints "[10.0, 10.0, 10.0, 10.0, 10.0]".
    print(c)
```

## Parameters

- `vectorA`: The first input vector,  .
- `vectorB`: The second input vector,  .
- `result`: The output vector,  .

## See Also

- [static func divide<U>(Double, U) -> [Double]](vdsp/divide(_:_:)-73m8v.md)
  Returns the double-precision element-wise division of a scalar value and a vector.
- [static func divide<U>(U, Double) -> [Double]](vdsp/divide(_:_:)-9nb4j.md)
  Calculates the double-precision element-wise division of a vector and a scalar value.
- [static func divide<T, U>(T, U) -> [Double]](vdsp/divide(_:_:)-8swnm.md)
  Returns the double-precision element-wise division of two vectors.
- [static func divide<U>(Float, U) -> [Float]](vdsp/divide(_:_:)-70npt.md)
  Returns the single-precision element-wise division of a scalar value and a vector.
- [static func divide<U>(U, Float) -> [Float]](vdsp/divide(_:_:)-1uqmz.md)
  Calculates the single-precision element-wise division of a vector and a scalar value.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/divide(_:_:result:)-6gtmm)*