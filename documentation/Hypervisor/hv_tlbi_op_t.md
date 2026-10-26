# hv_tlbi_op_t

**Framework**: Hypervisor  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 27.0+

## Declaration

```swift
struct hv_tlbi_op_t
```

```c
typedef enum { ... } hv_tlbi_op_t;
```

#### Overview

TLB invalidation operations for hv_vcpu_invalidate_tlb().

## Topics

### Initializers
- [init(UInt16)](./hv_tlbi_op_t/init%28_%29.md)
- [init(rawValue: UInt16)](./hv_tlbi_op_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt16](./hv_tlbi_op_t/rawvalue.md)
### Enumeration Cases
- [HV_TLBI_OP_ASIDE1IS](./hv_tlbi_op_aside1is.md)
- [HV_TLBI_OP_RVAAE1IS](./hv_tlbi_op_rvaae1is.md)
- [HV_TLBI_OP_RVAALE1IS](./hv_tlbi_op_rvaale1is.md)
- [HV_TLBI_OP_RVAE1IS](./hv_tlbi_op_rvae1is.md)
- [HV_TLBI_OP_RVALE1IS](./hv_tlbi_op_rvale1is.md)
- [HV_TLBI_OP_VAAE1IS](./hv_tlbi_op_vaae1is.md)
- [HV_TLBI_OP_VAALE1IS](./hv_tlbi_op_vaale1is.md)
- [HV_TLBI_OP_VAE1IS](./hv_tlbi_op_vae1is.md)
- [HV_TLBI_OP_VALE1IS](./hv_tlbi_op_vale1is.md)
- [HV_TLBI_OP_VMALLE1IS](./hv_tlbi_op_vmalle1is.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_tlbi_op_t)*