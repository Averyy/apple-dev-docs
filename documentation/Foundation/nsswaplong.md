# NSSwapLong(_:)

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
func NSSwapLong(_ inv: UInt) -> UInt
```

#### Discussion

Swaps the bytes of `inv` and returns the resulting value. Bytes are swapped from each low-order position to the corresponding high-order position and vice versa. For example, if the bytes of `inv` are numbered from 1 to 4, this function swaps bytes 1 and 4, and bytes 2 and 3.

## See Also

- [func NSSwapInt(UInt32) -> UInt32](nsswapint(_:).md)
  Swaps the bytes of a number.
- [func NSSwapLongLong(UInt64) -> UInt64](nsswaplonglong(_:).md)
  Swaps the bytes of a number.
- [func NSSwapFloat(NSSwappedFloat) -> NSSwappedFloat](nsswapfloat(_:).md)
  Swaps the bytes of a number.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsswaplong(_:))*