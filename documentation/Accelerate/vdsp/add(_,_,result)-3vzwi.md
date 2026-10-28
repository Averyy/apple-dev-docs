# add(_:_:result:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Calculates the single-precision element-wise sum of two vectors.

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
static func add<T, U, V>(_ vectorA: T, _ vectorB: U, result: inout V) where T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, T.Element == Float, U.Element == Float, V.Element == Float
```

## Discussion

This function calculates the sums of the first `N` elements of input vectors `A` and `B`, and writes the result to output vector `C`, as follows:

```swift
 for (n = 0; n < N; ++n)
    C[n] = A[n] + B[n];
```

![A diagram showing the operation of this function. There are three rows. The top row represents the input vectors, A and B, with three boxes of each. The middle row represents the operation as three boxes with plus signs. The bottom row represents the output vector C as three boxes. The diagram has connecting lines from the input vectors to the operation, and from the operation to the output vectors.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4389090@2x.png)

The following code shows an example of using this function:

```swift
    let count = 5

    let a: [Float] = [ 1,  2,  3,  4,  5]
    let b: [Float] = [10, 20, 30, 40, 50]

    let c = [Float](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP.add(a, b,
                 result: &buffer)
        
        initializedCount = count
    }
   
    // Prints "[11.0, 22.0, 33.0, 44.0, 55.0]".
    print(c)
```

## Parameters

- `vectorA`: The first input vector, `A`.
- `vectorB`: The second input vector, `B`.
- `result`: The output vector, `C`.

## See Also

### Addition
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
- [static func add(DSPSplitComplex, to: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](./add%28_,to,count,result%29-g1dk.md)
  Calculates the single-precision element-wise sum of the supplied complex vectors.
- [static func add(DSPDoubleSplitComplex, to: DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](./add%28_,to,count,result%29-75np9.md)
  Calculates the double-precision element-wise sum of the supplied complex vectors.
- [static func add<U>(multiplication: (a: U, b: Double), Double) -> [Double]](./add%28multiplication,_%29-4e3tj.md)
  Returns the double-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U>(multiplication: (a: T, b: Double), U) -> [Double]](./add%28multiplication,_%29-1bsuq.md)
  Returns the double-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U>(multiplication: (a: T, b: U), Double) -> [Double]](./add%28multiplication,_%29-9dxlr.md)
  Returns the double-precision element-wise sum of the product of two vectors, and a scalar value.
- [static func add<S, T, U>(multiplication: (a: S, b: T), U) -> [Double]](./add%28multiplication,_%29-4667v.md)
  Returns the double-precision element-wise sum of a vector and the product of two vectors.
- [static func add<U>(multiplication: (a: U, b: Float), Float) -> [Float]](./add%28multiplication,_%29-3tw93.md)
  Returns the single-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U>(multiplication: (a: T, b: Float), U) -> [Float]](./add%28multiplication,_%29-7aut1.md)
  Returns the single-precision element-wise addition of the product of a vector and a scalar value, and a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/add(_:_:result:)-3vzwi)*