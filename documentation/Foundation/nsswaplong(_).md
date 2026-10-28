# NSSwapLong(_:)

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
func NSSwapLong(_ inv: UInt) -> UInt
```

```c
static unsigned long NSSwapLong(unsigned long inv);
```

## Discussion

Swaps the bytes of `inv` and returns the resulting value. Bytes are swapped from each low-order position to the corresponding high-order position and vice versa. For example, if the bytes of `inv` are numbered from 1 to 4, this function swaps bytes 1 and 4, and bytes 2 and 3.

## See Also

### Related Documentation
- [func NSSwapInt(UInt32) -> UInt32](./nsswapint%28_%29.md)
  Swaps the bytes of a number.
- [func NSSwapLongLong(UInt64) -> UInt64](./nsswaplonglong%28_%29.md)
  Swaps the bytes of a number.
- [func NSSwapFloat(NSSwappedFloat) -> NSSwappedFloat](./nsswapfloat%28_%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsswaplong(_:))*