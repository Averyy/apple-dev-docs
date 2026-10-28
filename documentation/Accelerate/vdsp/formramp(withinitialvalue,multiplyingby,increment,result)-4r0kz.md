# formRamp(withInitialValue:multiplyingBy:increment:result:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Populates a single-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.

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
static func formRamp<U, V>(withInitialValue initialValue: inout Float, multiplyingBy vector: U, increment: Float, result: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Float, V.Element == Float
```

## Discussion

Use this function to generate and return a vector populated with ramped values with each element multiplied by the corresponding element in a second vector.

The following code generates a ramped vector with values in the range `0 ... 7`. The function multiplies elements at even indices by `10` and multiplies elements at odd indices by `100`:

```swift
    let n = 8
    
    var initialValue: Float = 0
    let increment: Float = 1
    
    let ramp = [Float](unsafeUninitializedCapacity: n) {
        buffer, initializedCount in
        
        vDSP.formRamp(withInitialValue: &initialValue,
                      multiplyingBy: [10, 100, 10, 100, 10, 100, 10, 100],
                      increment: increment,
                      result: &buffer)
        
        initializedCount = n
    }
    
    // Prints "[0.0, 100.0, 20.0, 300.0, 40.0, 500.0, 60.0, 700.0]".
    print(ramp)
    
    // Prints "8".
    print(initialValue)
```

## Parameters

- `initialValue`: On input, the initial value of the ramp. On output, the next value in the ramp.
- `vector`: The input vector that the function multiplies by the ramp.
- `increment`: The increment, or decrement if negative, between each generated element.
- `result`: The result.

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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/formramp(withinitialvalue:multiplyingby:increment:result:)-4r0kz)*