# hv_reg_t

**Framework**: Hypervisor  
**Kind**: struct

The type that defines general registers.

**Availability**:
- macOS ?+

## Declaration

```swift
struct hv_reg_t
```

## Topics

### General registers
- [var HV_REG_CPSR: hv_reg_t](hv_reg_cpsr.md)
  The value that identifies the current program status register (CPSR).
- [var HV_REG_LR: hv_reg_t](hv_reg_lr.md)
  The value that identifies the link register (LR).
- [var HV_REG_PC: hv_reg_t](hv_reg_pc.md)
  The value that identifies the program counter (PC).
- [var HV_REG_FP: hv_reg_t](hv_reg_fp.md)
  The value that identifies the frame pointer (FP).
- [var HV_REG_FPCR: hv_reg_t](hv_reg_fpcr.md)
  The value that identifies the floating-point control register (FPCR).
- [var HV_REG_FPSR: hv_reg_t](hv_reg_fpsr.md)
  The value that identifies the floating-point status register (FPSR).
- [var HV_REG_X0: hv_reg_t](hv_reg_x0.md)
  The value that identifies register X0.
- [var HV_REG_X1: hv_reg_t](hv_reg_x1.md)
  The value that identifies register X1.
- [var HV_REG_X2: hv_reg_t](hv_reg_x2.md)
  The value that identifies register X2.
- [var HV_REG_X3: hv_reg_t](hv_reg_x3.md)
  The value that identifies register X3.
- [var HV_REG_X4: hv_reg_t](hv_reg_x4.md)
  The value that identifies register X4.
- [var HV_REG_X5: hv_reg_t](hv_reg_x5.md)
  The value that identifies register X5.
- [var HV_REG_X6: hv_reg_t](hv_reg_x6.md)
  The value that identifies register X6.
- [var HV_REG_X7: hv_reg_t](hv_reg_x7.md)
  The value that identifies register X7.
- [var HV_REG_X8: hv_reg_t](hv_reg_x8.md)
  The value that identifies register X8.
- [var HV_REG_X9: hv_reg_t](hv_reg_x9.md)
  The value that identifies register X9.
- [var HV_REG_X10: hv_reg_t](hv_reg_x10.md)
  The value that identifies register X10.
- [var HV_REG_X11: hv_reg_t](hv_reg_x11.md)
  The value that identifies register X11.
- [var HV_REG_X12: hv_reg_t](hv_reg_x12.md)
  The value that identifies register X12.
- [var HV_REG_X13: hv_reg_t](hv_reg_x13.md)
  The value that identifies register X13.
- [var HV_REG_X14: hv_reg_t](hv_reg_x14.md)
  The value that identifies register X14.
- [var HV_REG_X15: hv_reg_t](hv_reg_x15.md)
  The value that identifies register X15.
- [var HV_REG_X16: hv_reg_t](hv_reg_x16.md)
  The value that identifies register X16.
- [var HV_REG_X17: hv_reg_t](hv_reg_x17.md)
  The value that identifies register X17.
- [var HV_REG_X18: hv_reg_t](hv_reg_x18.md)
  The value that identifies register X18.
- [var HV_REG_X19: hv_reg_t](hv_reg_x19.md)
  The value that identifies register X19.
- [var HV_REG_X20: hv_reg_t](hv_reg_x20.md)
  The value that identifies register X20.
- [var HV_REG_X21: hv_reg_t](hv_reg_x21.md)
  The value that identifies register X21.
- [var HV_REG_X22: hv_reg_t](hv_reg_x22.md)
  The value that identifies register X22.
- [var HV_REG_X23: hv_reg_t](hv_reg_x23.md)
  The value that identifies register X23.
- [var HV_REG_X24: hv_reg_t](hv_reg_x24.md)
  The value that identifies register X24.
- [var HV_REG_X25: hv_reg_t](hv_reg_x25.md)
  The value that identifies register X25.
- [var HV_REG_X26: hv_reg_t](hv_reg_x26.md)
  The value that identifies register X26.
- [var HV_REG_X27: hv_reg_t](hv_reg_x27.md)
  The value that identifies register X27.
- [var HV_REG_X28: hv_reg_t](hv_reg_x28.md)
  The value that identifies register X28.
- [var HV_REG_X29: hv_reg_t](hv_reg_x29.md)
  The value that identifies register X29.
- [var HV_REG_X30: hv_reg_t](hv_reg_x30.md)
  The value that identifies register X30.
### Instance properties
- [var rawValue: UInt32](hv_reg_t/rawvalue.md)
  A 32-bit unsigned integer that represents the general registers.
### Initializers
- [init(UInt32)](hv_reg_t/init(_:).md)
  Creates a new general register instance initialized with the value you provide.
- [init(rawValue: UInt32)](hv_reg_t/init(rawvalue:).md)
  Creates a new general register instance initialized with the value you provide.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func hv_vcpu_get_reg(hv_vcpu_t, hv_reg_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_get_reg(_:_:_:).md)
  Gets the current value of a vCPU register.
- [func hv_vcpu_set_reg(hv_vcpu_t, hv_reg_t, UInt64) -> hv_return_t](hv_vcpu_set_reg(_:_:_:).md)
  Sets the value of a vCPU register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_reg_t)*