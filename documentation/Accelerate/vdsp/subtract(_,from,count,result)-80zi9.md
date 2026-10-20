# subtract(_:from:count:result:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Calculates the double-precision element-wise subtraction of a complex vector from a complex vector.

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
static func subtract(_ splitComplexB: DSPDoubleSplitComplex, from splitComplexA: DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)
```

## See Also

### Subtraction
- [static func subtract<T, U>(U, T) -> [Double]](./subtract%28_,_%29-8o5ai.md)
  Returns the double-precision element-wise subtraction of two vectors.
- [static func subtract<T, U>(U, T) -> [Float]](./subtract%28_,_%29-9xmo8.md)
  Returns the single-precision element-wise subtraction of two vectors.
- [static func subtract<T, U, V>(U, T, result: inout V)](./subtract%28_,_,result%29-1ianx.md)
  Calculates the double-precision element-wise subtraction of two vectors.
- [static func subtract<T, U, V>(U, T, result: inout V)](./subtract%28_,_,result%29-2p3fa.md)
  Calculates the single-precision element-wise subtraction of two vectors.
- [static func subtract(DSPSplitComplex, from: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](./subtract%28_,from,count,result%29-4p5xd.md)
  Calculates the single-precision element-wise subtraction of a complex vector from a complex vector.
- [static func subtract<T, U>(multiplication: (a: U, b: Double), T) -> [Double]](./subtract%28multiplication,_%29-2hhme.md)
  Calculates the double-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U>(multiplication: (a: T, b: U), S) -> [Double]](./subtract%28multiplication,_%29-9gphg.md)
  Returns the double-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<T, U>(multiplication: (a: U, b: Float), T) -> [Float]](./subtract%28multiplication,_%29-3zm6l.md)
  Calculates the single-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U>(multiplication: (a: T, b: U), S) -> [Float]](./subtract%28multiplication,_%29-6u3sp.md)
  Returns the single-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<T, U, V>(multiplication: (a: U, b: Double), T, result: inout V)](./subtract%28multiplication,_,result%29-9p12h.md)
  Calculates the double-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<T, U, V>(multiplication: (a: U, b: Float), T, result: inout V)](./subtract%28multiplication,_,result%29-86gx3.md)
  Calculates the single-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U, V>(multiplication: (a: T, b: U), S, result: inout V)](./subtract%28multiplication,_,result%29-3f2bw.md)
  Calculates the double-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<S, T, U, V>(multiplication: (a: T, b: U), S, result: inout V)](./subtract%28multiplication,_,result%29-6b91s.md)
  Calculates the single-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<R, S, T, U>(multiplication: (a: T, b: U), multiplication: (c: R, d: S)) -> [Double]](./subtract%28multiplication,multiplication%29-22a4b.md)
  Returns the double-precision element-wise difference of the products of two pairs of vectors.
- [static func subtract<R, S, T, U>(multiplication: (a: T, b: U), multiplication: (c: R, d: S)) -> [Float]](./subtract%28multiplication,multiplication%29-1ghyu.md)
  Returns the single-precision element-wise difference of the products of two pairs of vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/subtract(_:from:count:result:)-80zi9)*