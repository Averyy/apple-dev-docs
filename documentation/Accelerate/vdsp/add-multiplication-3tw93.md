# add(multiplication:_:)

**Framework**: Accelerate  
**Kind**: method

Returns the single-precision element-wise addition of the product of a vector and a scalar value, and a vector.

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
static func add<U>(multiplication: (a: U, b: Float), _ scalar: Float) -> [Float] where U : AccelerateBuffer, U.Element == Float
```

#### Return Value

The output vector `D` in `D = (A * B) + C`.

#### Discussion

This function calculates the element-wise product of vector `A` and scalar value `B`, adds scalar value `C` to the product, and writes the result to vector `D`.

```swift
 for (n = 0; n < N; ++n)
    D[n] = A[n] * B + C[n];
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vector A with three boxes, and the scalar value B with one box. The second row represents the operation that multiplies A and B, with three boxes, as well as the input vector C with three boxes. The third row represents the addition operation as three boxes. The bottom row represents the output vector D as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vector. ](https://docs-assets.developer.apple.com/published/8acd6489f7a40f9981697d673e124e2d/media-4387655%402x.png)

The following code shows an example of using this function:

```swift
    let a: [Float] = [ 1,  2,  3,  4,  5]
    let b: Float = 10
    let c: Float = 5
    
    let d = vDSP.add(multiplication: (a, b),
                     c)
    
    // Prints "[15.0, 25.0, 35.0, 45.0, 55.0]".
    print(d)
```

## Parameters

- `multiplication`: A tuple that contains the vector   and the scalar value   in  .
- `scalar`: The input scalar value   in  .

## See Also

- [static func add<U>(Double, U) -> [Double]](vdsp/add(_:_:)-9mv1a.md)
  Returns the double-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U>(T, U) -> [Double]](vdsp/add(_:_:)-2ftxc.md)
  Returns the double-precision element-wise sum of two vectors.
- [static func add<U>(Float, U) -> [Float]](vdsp/add(_:_:)-53nh9.md)
  Returns the single-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U>(T, U) -> [Float]](vdsp/add(_:_:)-7swvf.md)
  Returns the single-precision element-wise sum of two vectors.
- [static func add<U, V>(Double, U, result: inout V)](vdsp/add(_:_:result:)-2531u.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value.
- [static func add<U, V>(Float, U, result: inout V)](vdsp/add(_:_:result:)-2w0o9.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U, V>(T, U, result: inout V)](vdsp/add(_:_:result:)-338hl.md)
  Calculates the double-precision element-wise sum of two vectors.
- [static func add<T, U, V>(T, U, result: inout V)](vdsp/add(_:_:result:)-3vzwi.md)
  Calculates the single-precision element-wise sum of two vectors.
- [static func add(DSPSplitComplex, to: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](vdsp/add(_:to:count:result:)-g1dk.md)
  Calculates the single-precision elementwise sum of the supplied complex vectors.
- [static func add(DSPDoubleSplitComplex, to: DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](vdsp/add(_:to:count:result:)-75np9.md)
  Calculates the double-precision elementwise sum of the supplied complex vectors.
- [static func add<U>(multiplication: (a: U, b: Double), Double) -> [Double]](vdsp/add(multiplication:_:)-4e3tj.md)
  Returns the double-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U>(multiplication: (a: T, b: Double), U) -> [Double]](vdsp/add(multiplication:_:)-1bsuq.md)
  Returns the double-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U>(multiplication: (a: T, b: U), Double) -> [Double]](vdsp/add(multiplication:_:)-9dxlr.md)
  Returns the double-precision element-wise sum of the product of two vectors, and a scalar value.
- [static func add<S, T, U>(multiplication: (a: S, b: T), U) -> [Double]](vdsp/add(multiplication:_:)-4667v.md)
  Returns the double-precision element-wise sum of a vector and the product of two vectors.
- [static func add<T, U>(multiplication: (a: T, b: Float), U) -> [Float]](vdsp/add(multiplication:_:)-7aut1.md)
  Returns the single-precision element-wise addition of the product of a vector and a scalar value, and a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/add(multiplication:_:)-3tw93)*