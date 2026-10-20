# vR512Rotate(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

512-bit right rotate.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vR512Rotate(_ a: UnsafePointer<vU512>, _ rotateAmount: UInt32, _ result: UnsafeMutablePointer<vU512>)
```

```c
extern void vR512Rotate(const vU512 *a, uint32_t rotateAmount, vU512 *result);
```

## See Also

### Shifting and rotating large integers
- [func vLL256Shift(UnsafePointer<vU256>, UInt32, UnsafeMutablePointer<vU256>)](./vll256shift%28_,_,_%29.md)
  256-bit logical left shift.
- [func vLR256Shift(UnsafePointer<vU256>, UInt32, UnsafeMutablePointer<vU256>)](./vlr256shift%28_,_,_%29.md)
  256-bit logical right shift.
- [func vA256Shift(UnsafePointer<vS256>, UInt32, UnsafeMutablePointer<vS256>)](./va256shift%28_,_,_%29.md)
  256-bit arithmetic shift.
- [func vLL512Shift(UnsafePointer<vU512>, UInt32, UnsafeMutablePointer<vU512>)](./vll512shift%28_,_,_%29.md)
  512-bit logical left shift.
- [func vLR512Shift(UnsafePointer<vU512>, UInt32, UnsafeMutablePointer<vU512>)](./vlr512shift%28_,_,_%29.md)
  512-bit logical right shift .
- [func vA512Shift(UnsafePointer<vS512>, UInt32, UnsafeMutablePointer<vS512>)](./va512shift%28_,_,_%29.md)
  512-bit arithmetic shift.
- [func vLL1024Shift(UnsafePointer<vU1024>, UInt32, UnsafeMutablePointer<vU1024>)](./vll1024shift%28_,_,_%29.md)
  1024-bit logical left shift.
- [func vLR1024Shift(UnsafePointer<vU1024>, UInt32, UnsafeMutablePointer<vU1024>)](./vlr1024shift%28_,_,_%29.md)
  1024-bit logical right shift .
- [func vA1024Shift(UnsafePointer<vS1024>, UInt32, UnsafeMutablePointer<vS1024>)](./va1024shift%28_,_,_%29.md)
  1024-bit arithmetic shift.
- [func vL256Rotate(UnsafePointer<vU256>, UInt32, UnsafeMutablePointer<vU256>)](./vl256rotate%28_,_,_%29.md)
  256-bit left rotate.
- [func vR256Rotate(UnsafePointer<vU256>, UInt32, UnsafeMutablePointer<vU256>)](./vr256rotate%28_,_,_%29.md)
  256-bit right rotate.
- [func vL512Rotate(UnsafePointer<vU512>, UInt32, UnsafeMutablePointer<vU512>)](./vl512rotate%28_,_,_%29.md)
  512-bit left rotate.
- [func vL1024Rotate(UnsafePointer<vU1024>, UInt32, UnsafeMutablePointer<vU1024>)](./vl1024rotate%28_,_,_%29.md)
  1024-bit left rotate.
- [func vR1024Rotate(UnsafePointer<vU1024>, UInt32, UnsafeMutablePointer<vU1024>)](./vr1024rotate%28_,_,_%29.md)
  1024-bit right rotate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vr512rotate(_:_:_:))*