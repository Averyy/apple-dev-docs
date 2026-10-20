# linearInterpolate(lookupTable:withOffsets:scale:baseOffset:result:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Computes the single-precision linearly interpolated values of a lookup table from the specified offsets.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
static func linearInterpolate<T, U, V>(lookupTable: T, withOffsets offsets: U, scale: Float = 1, baseOffset: Float = 0, result: inout V) where T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, T.Element == Float, U.Element == Float, V.Element == Float
```

#### Discussion

The following code shows the result of linearly interpolating a lookup table that contains the values `[-10, 0, 100]` using the offsets `[0, 0.5, 1, 1.5, 2]`.  The integer offsets, `0`, `1`, and `2`, return the corresponding values in the lookup table, `-10`, `0`, and `2`. The noninteger offsets, `0.5` and `1.5`, return the linearly interpolated values between the lookup table values, `-5` and `50`:

```swift
let lookupTable: [Float] = [-10, 0, 100]
let offsets: [Float] = [0, 0.5, 1, 1.5, 2]

let count = offsets.count

let result = [Float](unsafeUninitializedCapacity: count) {
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/linearinterpolate(lookuptable:withoffsets:scale:baseoffset:result:)-4ownc)*