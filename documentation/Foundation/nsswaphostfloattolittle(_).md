# NSSwapHostFloatToLittle(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

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
func NSSwapHostFloatToLittle(_ x: Float) -> NSSwappedFloat
```

```c
static NSSwappedFloat NSSwapHostFloatToLittle(float x);
```

## Discussion

Converts the value in `x`, specified in the current endian format, to little-endian format and returns the resulting value. If it is necessary to swap the bytes, this function calls [`NSSwapFloat(_:)`](./nsswapfloat%28_%29.md) to perform the swap.

## See Also

### Related Documentation
- [func NSSwapHostFloatToBig(Float) -> NSSwappedFloat](./nsswaphostfloattobig%28_%29.md)
  Swaps the bytes of a number.
- [func NSSwapLittleFloatToHost(NSSwappedFloat) -> Float](./nsswaplittlefloattohost%28_%29.md)
  Swaps the bytes of a number.
### Functions
- [func NSConvertHostDoubleToSwapped(Double) -> NSSwappedDouble](./nsconverthostdoubletoswapped%28_%29.md)
  Performs a type conversion.
- [func NSConvertHostFloatToSwapped(Float) -> NSSwappedFloat](./nsconverthostfloattoswapped%28_%29.md)
  Performs a type conversion.
- [func NSConvertSwappedDoubleToHost(NSSwappedDouble) -> Double](./nsconvertswappeddoubletohost%28_%29.md)
  Performs a type conversion.
- [func NSConvertSwappedFloatToHost(NSSwappedFloat) -> Float](./nsconvertswappedfloattohost%28_%29.md)
  Performs a type conversion.
- [func NSHostByteOrder() -> Int](./nshostbyteorder%28%29.md)
  Returns the endian format.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsswaphostfloattolittle(_:))*