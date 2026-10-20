# divide(_:_:result:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Calculates the double-precision element-wise division of a scalar value and a vector.

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
static func divide<U, V>(_ scalar: Double, _ vector: U, result: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Double, V.Element == Double
```

#### Discussion

This function calculates the element-wise division of scalar value `A` and vector `B`, and writes the result to vector `C`, as follows:

```swift
 for (n = 0; n < N; ++n)
    C[n] = A / B[n];
```

![A diagram showing the operation of this function. There are three rows. The top row represents the scalar value A with one box, and the input vector B with three boxes. The middle row represents the operation as three boxes with division signs. The bottom row represents the output vector C as three boxes. The diagram has connecting lines from the input vectors to the operation, and from the operation to the output vector. ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4337221@2x.png)

The following code shows an example of using this function:

```swift
    let count = 5
    
    let a: Double = 100
    let b: [Double] = [1, 2, 3, 4, 5]
    
    let c = [Double](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP.divide(a, b,
                    result: &buffer)
        
        initializedCount = count
    }
    
    // Prints "[100.0, 50.0, 33.33, 25.0, 20.0]".
    print(c)
```

## Parameters

- `scalar`: The input scalar value, `A`.
- `vector`: The input vector, `B`.
- `result`: The output vector, `C`.

## See Also

### Division
- [static func divide<U>(Double, U) -> [Double]](./divide%28_,_%29-73m8v.md)
  Returns the double-precision element-wise division of a scalar value and a vector.
- [static func divide<U>(U, Double) -> [Double]](./divide%28_,_%29-9nb4j.md)
  Calculates the double-precision element-wise division of a vector and a scalar value.
- [static func divide<T, U>(T, U) -> [Double]](./divide%28_,_%29-8swnm.md)
  Returns the double-precision element-wise division of two vectors.
- [static func divide<U>(Float, U) -> [Float]](./divide%28_,_%29-70npt.md)
  Returns the single-precision element-wise division of a scalar value and a vector.
- [static func divide<U>(U, Float) -> [Float]](./divide%28_,_%29-1uqmz.md)
  Calculates the single-precision element-wise division of a vector and a scalar value.
- [static func divide<T, U>(T, U) -> [Float]](./divide%28_,_%29-6nfsi.md)
  Returns the single-precision element-wise division of two vectors.
- [static func divide<U, V>(Float, U, result: inout V)](./divide%28_,_,result%29-3emlk.md)
  Calculates the single-precision element-wise division of a scalar value and a vector.
- [static func divide<U, V>(U, Double, result: inout V)](./divide%28_,_,result%29-44mff.md)
  Calculates the double-precision element-wise division of a vector and a scalar value.
- [static func divide<U, V>(U, Float, result: inout V)](./divide%28_,_,result%29-5hwb2.md)
  Calculates the single-precision element-wise division of a vector and a scalar value.
- [static func divide<T, U, V>(T, U, result: inout V)](./divide%28_,_,result%29-6gtmm.md)
  Calculates the double-precision element-wise division of two vectors.
- [static func divide<T, U, V>(T, U, result: inout V)](./divide%28_,_,result%29-7ejy9.md)
  Calculates the single-precision element-wise division of two vectors.
- [static func divide(DSPSplitComplex, by: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](./divide%28_,by,count,result%29-9chz5.md)
  Calculates the single-precision element-wise division of a complex vector by a complex vector.
- [static func divide(DSPDoubleSplitComplex, by: DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](./divide%28_,by,count,result%29-57jlj.md)
  Calculates the double-precision element-wise division of a complex vector by a complex vector.
- [static func divide<U>(DSPSplitComplex, by: U, result: inout DSPSplitComplex)](./divide%28_,by,result%29-66qch.md)
  Calculates the single-precision element-wise division of a complex vector by a real vector.
- [static func divide<U>(DSPDoubleSplitComplex, by: U, result: inout DSPDoubleSplitComplex)](./divide%28_,by,result%29-402v9.md)
  Calculates the double-precision element-wise division of a complex vector by a complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/divide(_:_:result:)-18qa3)*