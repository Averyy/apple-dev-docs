# vR128Rotate(_:_:)

**Framework**: Accelerate  
**Kind**: func

128-bit right rotate.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vR128Rotate(_ vA: vUInt32, _ vRotateFactor: vUInt8) -> vUInt32
```

#### Return Value

Returns the shifted vector.

#### Discussion

This function treats the entire 128-bit vector as a single value to rotate.

## Parameters

- `vA`: The vector to shift.
- `vRotateFactor`: The number of bits to shift the vector.

## See Also

- [func vLL128Shift(vUInt32, vUInt8) -> vUInt32](vll128shift(_:_:).md)
  128-bit logical left shift.
- [func vLR128Shift(vUInt32, vUInt8) -> vUInt32](vlr128shift(_:_:).md)
  128-bit logical right shift.
- [func vLL64Shift(vUInt32, vUInt8) -> vUInt32](vll64shift(_:_:).md)
  64-bit logical left shift.
- [func vLL64Shift2(vUInt32, vUInt8) -> vUInt32](vll64shift2(_:_:).md)
  64-bit logical left shift with two shift factors.
- [func vLR64Shift(vUInt32, vUInt8) -> vUInt32](vlr64shift(_:_:).md)
  64-bit logical right shift.
- [func vLR64Shift2(vUInt32, vUInt8) -> vUInt32](vlr64shift2(_:_:).md)
  64-bit logical right shift with two shift factors.
- [func vA64Shift(vUInt32, vUInt8) -> vUInt32](va64shift(_:_:).md)
  64-bit arithmetic (signed) shift.
- [func vA64Shift2(vUInt32, vUInt8) -> vUInt32](va64shift2(_:_:).md)
  64-bit arithmetic (signed) shift with two shift factors.
- [func vA128Shift(vUInt32, vUInt8) -> vUInt32](va128shift(_:_:).md)
  128-bit arithmetic (signed) shift.
- [func vL64Rotate(vUInt32, vUInt8) -> vUInt32](vl64rotate(_:_:).md)
  64-bit left rotate.
- [func vR64Rotate(vUInt32, vUInt8) -> vUInt32](vr64rotate(_:_:).md)
  64-bit right rotate.
- [func vL64Rotate2(vUInt32, vUInt8) -> vUInt32](vl64rotate2(_:_:).md)
  64-bit left rotate with two rotation factors.
- [func vR64Rotate2(vUInt32, vUInt8) -> vUInt32](vr64rotate2(_:_:).md)
  64-bit right rotate with two rotation factors.
- [func vL128Rotate(vUInt32, vUInt8) -> vUInt32](vl128rotate(_:_:).md)
  128-bit left rotate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vr128rotate(_:_:))*