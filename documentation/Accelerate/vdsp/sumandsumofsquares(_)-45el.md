# sumAndSumOfSquares(_:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Returns the single-precision vector sum and sum of squares.

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
static func sumAndSumOfSquares<U>(_ vector: U) -> (elementsSum: Float, squaresSum: Float) where U : AccelerateBuffer, U.Element == Float
```

## Discussion

This function calculates and returns the sum and the sum of the squares of the elements of a supplied vector.

The following is an example of using [`sumAndSumOfSquares(_:)`](./sumandsumofsquares%28_%29-9uec5.md):

```swift
let a: [Float] = [-1.5, 2.25, 3.6,
                  0.2, -0.1, -4.3]

let sumAndSumOfSquares = vDSP.sumAndSumOfSquares(a)

// Prints "sum 0.1500 sum of squares 38.8125".
print(String(format: "sum %.4f", sumAndSumOfSquares.elementsSum),
      String(format: "sum of squares %.4f", sumAndSumOfSquares.squaresSum))
```

## Parameters

- `vector`: The vector to sum.

## See Also

### Type Methods
- [static func absolute<U>(U) -> [Double]](./absolute%28_%29-9c3ge.md)
  Returns the absolute value of each element in the supplied double-precision vector.
- [static func absolute<U>(U) -> [Float]](./absolute%28_%29-5ehc1.md)
  Returns the absolute value of each element in the supplied single-precision vector.
- [static func absolute<V>(DSPSplitComplex, result: inout V)](./absolute%28_,result%29-9x5jn.md)
  Calculates the absolute value of each element in the supplied single-precision complex vector.
- [static func absolute<V>(DSPDoubleSplitComplex, result: inout V)](./absolute%28_,result%29-1wu9x.md)
  Calculates the absolute value of each element in the supplied double-precision complex vector.
- [static func absolute<U, V>(U, result: inout V)](./absolute%28_,result%29-657bd.md)
  Calculates the absolute value of each element in the supplied double-precision vector.
- [static func absolute<U, V>(U, result: inout V)](./absolute%28_,result%29-4pigo.md)
  Calculates the absolute value of each element in the supplied single-precision vector.
- [static func add<U>(Double, U) -> [Double]](./add%28_,_%29-9mv1a.md)
  Returns the double-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U>(T, U) -> [Double]](./add%28_,_%29-2ftxc.md)
  Returns the double-precision element-wise sum of two vectors.
- [static func add<U>(Float, U) -> [Float]](./add%28_,_%29-53nh9.md)
  Returns the single-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U>(T, U) -> [Float]](./add%28_,_%29-7swvf.md)
  Returns the single-precision element-wise sum of two vectors.
- [static func add<U, V>(Double, U, result: inout V)](./add%28_,_,result%29-2531u.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value.
- [static func add<U, V>(Float, U, result: inout V)](./add%28_,_,result%29-2w0o9.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U, V>(T, U, result: inout V)](./add%28_,_,result%29-338hl.md)
  Calculates the double-precision element-wise sum of two vectors.
- [static func add<T, U, V>(T, U, result: inout V)](./add%28_,_,result%29-3vzwi.md)
  Calculates the single-precision element-wise sum of two vectors.
- [static func add(DSPSplitComplex, to: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](./add%28_,to,count,result%29-g1dk.md)
  Calculates the single-precision element-wise sum of the supplied complex vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/sumandsumofsquares(_:)-45el)*