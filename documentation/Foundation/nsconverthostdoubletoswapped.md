# NSConvertHostDoubleToSwapped(_:)

**Framework**: Foundation  
**Kind**: func

Performs a type conversion.

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
func NSConvertHostDoubleToSwapped(_ x: Double) -> NSSwappedDouble
```

#### Discussion

Converts the double value in `x` to a value whose bytes can be swapped. This function does not actually swap the bytes of `x`. You should not need to call this function directly.

## See Also

- [func NSSwapHostDoubleToLittle(Double) -> NSSwappedDouble](nsswaphostdoubletolittle(_:).md)
  Swaps the bytes of a number.
- [func NSSwapHostDoubleToBig(Double) -> NSSwappedDouble](nsswaphostdoubletobig(_:).md)
  Swaps the bytes of a number.
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
- [func NSSwapHostFloatToBig(Float) -> NSSwappedFloat](nsswaphostfloattobig(_:).md)
  Swaps the bytes of a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconverthostdoubletoswapped(_:))*