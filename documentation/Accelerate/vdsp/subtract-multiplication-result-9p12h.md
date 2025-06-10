# subtract(multiplication:_:result:)

**Framework**: Accelerate  
**Kind**: method

Calculates the double-precision element-wise difference of the product of a vector and a scalar value, and a vector.

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
static func subtract<T, U, V>(multiplication: (a: U, b: Double), _ vector: T, result: inout V) where T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, T.Element == Double, U.Element == Double, V.Element == Double
```

#### Discussion

This function calculates the element-wise product of vector `A` and scalar value `B`, subtracts vector `C` from the product, and writes the result to vector `D`.

```swift
 for (n = 0; n < N; ++n)
    D[n] = A[n] * B - C[n];
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vector A with three boxes, and the scalar value B with one box. The second row represents the operation that multiplies A and B, with three boxes, as well as the input vector C with three boxes. The third row represents the subtraction operation as three boxes. The bottom row represents the output vector D as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vector.  ](https://docs-assets.developer.apple.com/published/4e34a5f56d6ecfd4fd5bb8762ac89baa/media-4387387%402x.png)

The following code shows an example of using this function:

```swift
    let count = 5
    
    let a: [Double] = [ 1,  2,  3,  4,  5]
    let b: Double = 10
    let c: [Double] = [ 5,  4,  3,  2,  1]
    
    let d = [Double](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP.subtract(multiplication: (a, b),
                      c,
                      result: &buffer)
        
        initializedCount = count
    }
    
    // Prints "[5.0, 16.0, 27.0, 38.0, 49.0]".
    print(d)
```

## Parameters

- `multiplication`: A tuple that contains the vectors   and   in  .
- `vector`: The input scalar value   in  .
- `result`: The output vector   in  .

## See Also

- [static func subtract<T, U>(U, T) -> [Double]](vdsp/subtract(_:_:)-8o5ai.md)
  Returns the double-precision element-wise subtraction of two vectors.
- [static func subtract<T, U>(U, T) -> [Float]](vdsp/subtract(_:_:)-9xmo8.md)
  Returns the single-precision element-wise subtraction of two vectors.
- [static func subtract<T, U, V>(U, T, result: inout V)](vdsp/subtract(_:_:result:)-1ianx.md)
  Calculates the double-precision element-wise subtraction of two vectors.
- [static func subtract<T, U, V>(U, T, result: inout V)](vdsp/subtract(_:_:result:)-2p3fa.md)
  Calculates the single-precision element-wise subtraction of two vectors.
- [static func subtract(DSPSplitComplex, from: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](vdsp/subtract(_:from:count:result:)-4p5xd.md)
  Calculates the single-precision elementwise subtraction of a complex vector from a complex vector.
- [static func subtract(DSPDoubleSplitComplex, from: DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](vdsp/subtract(_:from:count:result:)-80zi9.md)
  Calculates the double-precision elementwise subtraction of a complex vector from a complex vector.
- [static func subtract<T, U>(multiplication: (a: U, b: Double), T) -> [Double]](vdsp/subtract(multiplication:_:)-2hhme.md)
  Calculates the double-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U>(multiplication: (a: T, b: U), S) -> [Double]](vdsp/subtract(multiplication:_:)-9gphg.md)
  Returns the double-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<T, U>(multiplication: (a: U, b: Float), T) -> [Float]](vdsp/subtract(multiplication:_:)-3zm6l.md)
  Calculates the single-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U>(multiplication: (a: T, b: U), S) -> [Float]](vdsp/subtract(multiplication:_:)-6u3sp.md)
  Returns the single-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<T, U, V>(multiplication: (a: U, b: Float), T, result: inout V)](vdsp/subtract(multiplication:_:result:)-86gx3.md)
  Calculates the single-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U, V>(multiplication: (a: T, b: U), S, result: inout V)](vdsp/subtract(multiplication:_:result:)-3f2bw.md)
  Calculates the double-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<S, T, U, V>(multiplication: (a: T, b: U), S, result: inout V)](vdsp/subtract(multiplication:_:result:)-6b91s.md)
  Calculates the single-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<R, S, T, U>(multiplication: (a: T, b: U), multiplication: (c: R, d: S)) -> [Double]](vdsp/subtract(multiplication:multiplication:)-22a4b.md)
  Returns the double-precision element-wise difference of the products of two pairs of vectors.
- [static func subtract<R, S, T, U>(multiplication: (a: T, b: U), multiplication: (c: R, d: S)) -> [Float]](vdsp/subtract(multiplication:multiplication:)-1ghyu.md)
  Returns the single-precision element-wise difference of the products of two pairs of vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/subtract(multiplication:_:result:)-9p12h)*