# vU128Neg(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Unsigned 128-bit negation.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func vU128Neg(_ vA: vUInt32) -> vUInt32
```

```c
extern vUInt32 vU128Neg(vUInt32 vA);
```

## Return Value

Returns the negated value.

## Parameters

- `vA`: The value to negate.

## See Also

### Performing arithmetic operations on large integers
- [func vU256Add(UnsafePointer<vU256>, UnsafePointer<vU256>, UnsafeMutablePointer<vU256>)](./vu256add%28_,_,_%29.md)
  Unsigned 256-bit addition (modular arithmetic).
- [func vU256AddS(UnsafePointer<vU256>, UnsafePointer<vU256>, UnsafeMutablePointer<vU256>)](./vu256adds%28_,_,_%29.md)
  Unsigned 256-bit addition with saturation (clipping).
- [func vS256Add(UnsafePointer<vS256>, UnsafePointer<vS256>, UnsafeMutablePointer<vS256>)](./vs256add%28_,_,_%29.md)
  Signed 256-bit addition (modular arithmetic).
- [func vS256AddS(UnsafePointer<vS256>, UnsafePointer<vS256>, UnsafeMutablePointer<vS256>)](./vs256adds%28_,_,_%29.md)
  Signed 256-bit addition with saturation (clipping).
- [func vU512Add(UnsafePointer<vU512>, UnsafePointer<vU512>, UnsafeMutablePointer<vU512>)](./vu512add%28_,_,_%29.md)
  Unsigned 512-bit addition (modular arithmetic).
- [func vU512AddS(UnsafePointer<vU512>, UnsafePointer<vU512>, UnsafeMutablePointer<vU512>)](./vu512adds%28_,_,_%29.md)
  Unsigned 512-bit addition with saturation (clipping).
- [func vS512Add(UnsafePointer<vS512>, UnsafePointer<vS512>, UnsafeMutablePointer<vS512>)](./vs512add%28_,_,_%29.md)
  Signed 512-bit addition (modular arithmetic).
- [func vS512AddS(UnsafePointer<vS512>, UnsafePointer<vS512>, UnsafeMutablePointer<vS512>)](./vs512adds%28_,_,_%29.md)
  Signed 512-bit addition with saturation (clipping).
- [func vU1024Add(UnsafePointer<vU1024>, UnsafePointer<vU1024>, UnsafeMutablePointer<vU1024>)](./vu1024add%28_,_,_%29.md)
  Unsigned 1024-bit addition (modular arithmetic).
- [func vU1024AddS(UnsafePointer<vU1024>, UnsafePointer<vU1024>, UnsafeMutablePointer<vU1024>)](./vu1024adds%28_,_,_%29.md)
  Unsigned 1024-bit addition with saturation (clipping).
- [func vS1024Add(UnsafePointer<vS1024>, UnsafePointer<vS1024>, UnsafeMutablePointer<vS1024>)](./vs1024add%28_,_,_%29.md)
  Signed 1024-bit addition (modular arithmetic).
- [func vS1024AddS(UnsafePointer<vS1024>, UnsafePointer<vS1024>, UnsafeMutablePointer<vS1024>)](./vs1024adds%28_,_,_%29.md)
  Signed 1024-bit addition with saturation (clipping).
- [func vU256Sub(UnsafePointer<vU256>, UnsafePointer<vU256>, UnsafeMutablePointer<vU256>)](./vu256sub%28_,_,_%29.md)
  Unsigned 256-bit subtraction (modular arithmetic).
- [func vU256SubS(UnsafePointer<vU256>, UnsafePointer<vU256>, UnsafeMutablePointer<vU256>)](./vu256subs%28_,_,_%29.md)
  Unsigned 256-bit subtraction with saturation (clipping).
- [func vS256Sub(UnsafePointer<vS256>, UnsafePointer<vS256>, UnsafeMutablePointer<vS256>)](./vs256sub%28_,_,_%29.md)
  Signed 256-bit subtraction (modular arithmetic).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vu128neg(_:))*