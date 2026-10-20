# divide(_:by:count:result:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Calculates the single-precision element-wise division of a complex vector by a complex vector.

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
static func divide(_ splitComplexA: DSPSplitComplex, by splitComplexB: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)
```

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
- [static func divide<U, V>(Double, U, result: inout V)](./divide%28_,_,result%29-18qa3.md)
  Calculates the double-precision element-wise division of a scalar value and a vector.
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
- [static func divide(DSPDoubleSplitComplex, by: DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](./divide%28_,by,count,result%29-57jlj.md)
  Calculates the double-precision element-wise division of a complex vector by a complex vector.
- [static func divide<U>(DSPSplitComplex, by: U, result: inout DSPSplitComplex)](./divide%28_,by,result%29-66qch.md)
  Calculates the single-precision element-wise division of a complex vector by a real vector.
- [static func divide<U>(DSPDoubleSplitComplex, by: U, result: inout DSPDoubleSplitComplex)](./divide%28_,by,result%29-402v9.md)
  Calculates the double-precision element-wise division of a complex vector by a complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/divide(_:by:count:result:)-9chz5)*