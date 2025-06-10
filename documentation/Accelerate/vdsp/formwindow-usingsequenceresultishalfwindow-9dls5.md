# formWindow(usingSequence:result:isHalfWindow:)

**Framework**: Accelerate  
**Kind**: method

Populates a single-precision vector with a specified window.

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
static func formWindow<V>(usingSequence sequence: vDSP.WindowSequence, result: inout V, isHalfWindow: Bool) where V : AccelerateMutableBuffer, V.Element == Float
```

#### Discussion

Use this function to populate a vector with values of a specified window sequence.

The following code shows how to generate a single-precision Blackman window:

```swift
var c = [Float](repeating: 0,
                count: 1024)

vDSP.formWindow(usingSequence: .blackman,
                result: &c,
                isHalfWindow: false)
```

The following figure illustrates the values of the output vector, `c`:

![Visualization of a Blackman window.](https://docs-assets.developer.apple.com/published/60bd6fe48f68c85247dc2dc8de350818/media-3362250%402x.png)

## Parameters

- `sequence`: The window sequence to use for generation.
- `result`: The destination vector that receives the result.
- `isHalfWindow`: A Boolean value that specifies whether the function generates half of the number of elements.

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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/formwindow(usingsequence:result:ishalfwindow:)-9dls5)*