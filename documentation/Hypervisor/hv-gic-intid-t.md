# hv_gic_intid_t

**Framework**: Hypervisor  
**Kind**: struct

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct hv_gic_intid_t
```

## Topics

### Initializers
- [init(UInt16)](hv_gic_intid_t/init(_:).md)
- [init(rawValue: UInt16)](hv_gic_intid_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt16](hv_gic_intid_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct hv_cache_type_t](hv_cache_type_t.md)
  The structure that describes an instruction or data cache element.
- [struct hv_vcpu_exit_exception_t](hv_vcpu_exit_exception_t.md)
  The structure that describes information about an exit from the virtual CPU (vCPU) to the host.
- [struct hv_apic_ctrl_t](hv_apic_ctrl_t.md)
- [struct hv_apic_intr_trigger_t](hv_apic_intr_trigger_t.md)
- [struct hv_apic_lvt_flavor_t](hv_apic_lvt_flavor_t.md)
- [struct hv_apic_state](hv_apic_state.md)
- [struct hv_apic_state_ext_t](hv_apic_state_ext_t.md)
- [struct hv_atpic_state](hv_atpic_state.md)
- [struct hv_atpic_state_ext_t](hv_atpic_state_ext_t.md)
- [struct hv_gic_distributor_reg_t](hv_gic_distributor_reg_t.md)
- [struct hv_gic_icc_reg_t](hv_gic_icc_reg_t.md)
- [struct hv_gic_ich_reg_t](hv_gic_ich_reg_t.md)
- [struct hv_gic_icv_reg_t](hv_gic_icv_reg_t.md)
- [struct hv_gic_msi_reg_t](hv_gic_msi_reg_t.md)
- [struct hv_gic_redistributor_reg_t](hv_gic_redistributor_reg_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_gic_intid_t)*