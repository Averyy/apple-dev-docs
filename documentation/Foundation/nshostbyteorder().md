# NSHostByteOrder()

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns the endian format.

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
func NSHostByteOrder() -> Int
```

```c
static long NSHostByteOrder();
```

## Return Value

The endian format, either [`NS_LittleEndian`](./ns_littleendian.md) or [`NS_BigEndian`](./ns_bigendian.md).

## See Also

### Functions
- [func NSConvertHostDoubleToSwapped(Double) -> NSSwappedDouble](./nsconverthostdoubletoswapped%28_%29.md)
  Performs a type conversion.
- [func NSConvertHostFloatToSwapped(Float) -> NSSwappedFloat](./nsconverthostfloattoswapped%28_%29.md)
  Performs a type conversion.
- [func NSConvertSwappedDoubleToHost(NSSwappedDouble) -> Double](./nsconvertswappeddoubletohost%28_%29.md)
  Performs a type conversion.
- [func NSConvertSwappedFloatToHost(NSSwappedFloat) -> Float](./nsconvertswappedfloattohost%28_%29.md)
  Performs a type conversion.
- [func NSSwapBigDoubleToHost(NSSwappedDouble) -> Double](./nsswapbigdoubletohost%28_%29.md)
  Swaps the bytes of a number.
- [func NSSwapBigFloatToHost(NSSwappedFloat) -> Float](./nsswapbigfloattohost%28_%29.md)
  Swaps the bytes of a number.
- [func NSSwapBigIntToHost(UInt32) -> UInt32](./nsswapbiginttohost%28_%29.md)
  Swaps the bytes of a number.
- [func NSSwapBigLongLongToHost(UInt64) -> UInt64](./nsswapbiglonglongtohost%28_%29.md)
  Swaps the bytes of a number.
- [func NSSwapBigLongToHost(UInt) -> UInt](./nsswapbiglongtohost%28_%29.md)
  Swaps the bytes of a number.
- [func NSSwapBigShortToHost(UInt16) -> UInt16](./nsswapbigshorttohost%28_%29.md)
  Swaps the bytes of a number.
- [func NSSwapDouble(NSSwappedDouble) -> NSSwappedDouble](./nsswapdouble%28_%29.md)
  Swaps the bytes of a number.
- [func NSSwapFloat(NSSwappedFloat) -> NSSwappedFloat](./nsswapfloat%28_%29.md)
  Swaps the bytes of a number.
- [func NSSwapHostDoubleToBig(Double) -> NSSwappedDouble](./nsswaphostdoubletobig%28_%29.md)
  Swaps the bytes of a number.
- [func NSSwapHostDoubleToLittle(Double) -> NSSwappedDouble](./nsswaphostdoubletolittle%28_%29.md)
  Swaps the bytes of a number.
- [func NSSwapHostFloatToBig(Float) -> NSSwappedFloat](./nsswaphostfloattobig%28_%29.md)
  Swaps the bytes of a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshostbyteorder())*