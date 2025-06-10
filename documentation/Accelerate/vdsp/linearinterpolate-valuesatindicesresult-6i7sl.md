# linearInterpolate(values:atIndices:result:)

**Framework**: Accelerate  
**Kind**: method

Computes the single-precision linearly interpolated values of a vector at the specified indices.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
static func linearInterpolate<T, U, V>(values: T, atIndices indices: U, result: inout V) where T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, T.Element == Float, U.Element == Float, V.Element == Float
```

#### Discussion

The following code creates a five-element vector from two values using linear interpolation. The last index in `indices` determines the length of the operation result.

```swift
let values: [Float] = [0, 100]
let indices: [Float] = [0, 4]

let count = Int(indices.last!) + 1

let result = [Float](unsafeUninitializedCapacity: count) {
    buffer, initializedCount in
    
    vDSP.linearInterpolate(values: values,
                           atIndices: indices,
                           result: &buffer)
    
    initializedCount = count
}

// Prints "[0.0, 25.0, 50.0, 75.0, 100.0]".
print(result)
```

## Parameters

- `values`: The values to interpolate.
- `indices`: The indices to the output vector.
- `result`: The destination vector that receives the result.

## See Also

- [static func absolute<U>(U) -> [Double]](vdsp/absolute(_:)-9c3ge.md)
  Returns the absolute value of each element in the supplied double-precision vector.
- [static func absolute<U>(U) -> [Float]](vdsp/absolute(_:)-5ehc1.md)
  Returns the absolute value of each element in the supplied single-precision vector.
- [static func absolute<V>(DSPSplitComplex, result: inout V)](vdsp/absolute(_:result:)-9x5jn.md)
  Calculates the absolute value of each element in the supplied single-precision complex vector.
- [static func absolute<V>(DSPDoubleSplitComplex, result: inout V)](vdsp/absolute(_:result:)-1wu9x.md)
  Calculates the absolute value of each element in the supplied double-precision complex vector.
- [static func absolute<U, V>(U, result: inout V)](vdsp/absolute(_:result:)-657bd.md)
  Calculates the absolute value of each element in the supplied double-precision vector.
- [static func absolute<U, V>(U, result: inout V)](vdsp/absolute(_:result:)-4pigo.md)
  Calculates the absolute value of each element in the supplied single-precision vector.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/linearinterpolate(values:atindices:result:)-6i7sl)*