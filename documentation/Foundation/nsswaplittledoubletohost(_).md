# NSSwapLittleDoubleToHost(_:)

**Framework**: Foundation  
**Kind**: func

Swaps the bytes of a number.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func NSSwapLittleDoubleToHost(_ x: NSSwappedDouble) -> Double
```

#### Discussion

Converts the little-endian formatted value in `x` to the current endian format and returns the resulting value. If it is necessary to swap the bytes of `x`, this function calls [`NSSwapDouble(_:)`](nsswapdouble(_:).md) to perform the swap.

## See Also

- [func NSSwapBigDoubleToHost(NSSwappedDouble) -> Double](nsswapbigdoubletohost(_:).md)
  Swaps the bytes of a number.
- [func NSSwapHostDoubleToLittle(Double) -> NSSwappedDouble](nsswaphostdoubletolittle(_:).md)
  Swaps the bytes of a number.
- [func NSConvertSwappedDoubleToHost(NSSwappedDouble) -> Double](nsconvertswappeddoubletohost(_:).md)
  Performs a type conversion.
- [func NSConvertHostDoubleToSwapped(Double) -> NSSwappedDouble](nsconverthostdoubletoswapped(_:).md)
  Performs a type conversion.
- [func NSConvertHostFloatToSwapped(Float) -> NSSwappedFloat](nsconverthostfloattoswapped(_:).md)
  Performs a type conversion.
- [func NSConvertSwappedDoubleToHost(NSSwappedDouble) -> Double](nsconvertswappeddoubletohost(_:).md)
  Performs a type conversion.
- [func NSConvertSwappedFloatToHost(NSSwappedFloat) -> Float](nsconvertswappedfloattohost(_:).md)
  Performs a type conversion.
- [func NSHostByteOrder() -> Int](nshostbyteorder().md)
  Returns the endian format.
- [func NSSwapBigDoubleToHost(NSSwappedDouble) -> Double](nsswapbigdoubletohost(_:).md)
  Swaps the bytes of a number.
- [func NSSwapBigFloatToHost(NSSwappedFloat) -> Float](nsswapbigfloattohost(_:).md)
  Swaps the bytes of a number.
- [func NSSwapBigIntToHost(UInt32) -> UInt32](nsswapbiginttohost(_:).md)
  Swaps the bytes of a number.
- [func NSSwapBigLongLongToHost(UInt64) -> UInt64](nsswapbiglonglongtohost(_:).md)
  Swaps the bytes of a number.
- [func NSSwapBigLongToHost(UInt) -> UInt](nsswapbiglongtohost(_:).md)
  Swaps the bytes of a number.
- [func NSSwapBigShortToHost(UInt16) -> UInt16](nsswapbigshorttohost(_:).md)
  Swaps the bytes of a number.
- [func NSSwapDouble(NSSwappedDouble) -> NSSwappedDouble](nsswapdouble(_:).md)
  Swaps the bytes of a number.
- [func NSSwapFloat(NSSwappedFloat) -> NSSwappedFloat](nsswapfloat(_:).md)
  Swaps the bytes of a number.
- [func NSSwapHostDoubleToBig(Double) -> NSSwappedDouble](nsswaphostdoubletobig(_:).md)
  Swaps the bytes of a number.
- [func NSSwapHostDoubleToLittle(Double) -> NSSwappedDouble](nsswaphostdoubletolittle(_:).md)
  Swaps the bytes of a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsswaplittledoubletohost(_:))*