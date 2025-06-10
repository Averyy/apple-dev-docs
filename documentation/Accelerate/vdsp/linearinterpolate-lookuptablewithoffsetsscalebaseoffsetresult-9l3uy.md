# linearInterpolate(lookupTable:withOffsets:scale:baseOffset:result:)

**Framework**: Accelerate  
**Kind**: method

Computes the double-precision linearly interpolated values of a lookup table from the specified offsets.

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
static func linearInterpolate<T, U, V>(lookupTable: T, withOffsets offsets: U, scale: Double = 1, baseOffset: Double = 0, result: inout V) where T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, T.Element == Double, U.Element == Double, V.Element == Double
```

#### Discussion

The following code shows the result of linearly interpolating a lookup table that contains the values `[-10, 0, 100]` using the offsets `[0, 0.5, 1, 1.5, 2]`.  The integer offsets, `0`, `1`, and `2`, return the corresponding values in the lookup table, `-10`, `0`, and `2`. The noninteger offsets, `0.5` and `1.5`, return the linearly interpolated values between the lookup table values, `-5` and `50`.

```swift
let lookupTable: [Double] = [-10, 0, 100]
let offsets: [Double] = [0, 0.5, 1, 1.5, 2]

let count = offsets.count

let result = [Double](unsafeUninitializedCapacity: count) {
    buffer, initializedCount in
    
    vDSP.linearInterpolate(lookupTable: lookupTable,
                                        withOffsets: offsets,
                                        result: &buffer)
    
    initializedCount = count
}

// Prints "[-10.0, -5.0, 0.0, 50.0, 100.0]".
print(result)
```

## Parameters

- `lookupTable`: The lookup table.
- `offsets`: The offsets into the lookup table.
- `scale`: The scale factor for the offsets.
- `baseOffset`: The base offset for the offsets.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/linearinterpolate(lookuptable:withoffsets:scale:baseoffset:result:)-9l3uy)*