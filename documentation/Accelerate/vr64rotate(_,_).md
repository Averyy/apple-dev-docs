# vR64Rotate(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

64-bit right rotate.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vR64Rotate(_ vA: vUInt32, _ vRotateFactor: vUInt8) -> vUInt32
```

```c
extern vUInt32 vR64Rotate(vUInt32 vA, vUInt8 vRotateFactor);
```

#### Return Value

Returns the shifted vector.

#### Discussion

This function treats the vector as a pair of 64-bit values to rotate.

## Parameters

- `vA`: The vector to shift.
- `vRotateFactor`: The number of bits to shift the vector.

## See Also

### Shift and Rotate Functions (from vBasicOps.h)
- [func vLL128Shift(vUInt32, vUInt8) -> vUInt32](./vll128shift%28_,_%29.md)
  128-bit logical left shift.
- [func vLR128Shift(vUInt32, vUInt8) -> vUInt32](./vlr128shift%28_,_%29.md)
  128-bit logical right shift.
- [func vLL64Shift(vUInt32, vUInt8) -> vUInt32](./vll64shift%28_,_%29.md)
  64-bit logical left shift.
- [func vLL64Shift2(vUInt32, vUInt8) -> vUInt32](./vll64shift2%28_,_%29.md)
  64-bit logical left shift with two shift factors.
- [func vLR64Shift(vUInt32, vUInt8) -> vUInt32](./vlr64shift%28_,_%29.md)
  64-bit logical right shift.
- [func vLR64Shift2(vUInt32, vUInt8) -> vUInt32](./vlr64shift2%28_,_%29.md)
  64-bit logical right shift with two shift factors.
- [func vA64Shift(vUInt32, vUInt8) -> vUInt32](./va64shift%28_,_%29.md)
  64-bit arithmetic (signed) shift.
- [func vA64Shift2(vUInt32, vUInt8) -> vUInt32](./va64shift2%28_,_%29.md)
  64-bit arithmetic (signed) shift with two shift factors.
- [func vA128Shift(vUInt32, vUInt8) -> vUInt32](./va128shift%28_,_%29.md)
  128-bit arithmetic (signed) shift.
- [func vL64Rotate(vUInt32, vUInt8) -> vUInt32](./vl64rotate%28_,_%29.md)
  64-bit left rotate.
- [func vL64Rotate2(vUInt32, vUInt8) -> vUInt32](./vl64rotate2%28_,_%29.md)
  64-bit left rotate with two rotation factors.
- [func vR64Rotate2(vUInt32, vUInt8) -> vUInt32](./vr64rotate2%28_,_%29.md)
  64-bit right rotate with two rotation factors.
- [func vL128Rotate(vUInt32, vUInt8) -> vUInt32](./vl128rotate%28_,_%29.md)
  128-bit left rotate.
- [func vR128Rotate(vUInt32, vUInt8) -> vUInt32](./vr128rotate%28_,_%29.md)
  128-bit right rotate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vr64rotate(_:_:))*