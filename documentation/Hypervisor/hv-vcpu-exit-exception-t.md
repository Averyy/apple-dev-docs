# hv_vcpu_exit_exception_t

**Framework**: Hypervisor  
**Kind**: struct

The structure that describes information about an exit from the virtual CPU (vCPU) to the host.

**Availability**:
- macOS ?+

## Declaration

```swift
struct hv_vcpu_exit_exception_t
```

## Topics

### Initializers
- [init()](hv_vcpu_exit_exception_t/init.md)
  Creates a new VCPU exit exception instance.
- [init(syndrome: hv_exception_syndrome_t, virtual_address: hv_exception_address_t, physical_address: hv_ipa_t)](hv_vcpu_exit_exception_t/init(syndrome:virtual_address:physical_address:).md)
  Creates a new VCPU exit exception instance.with the parameters you provide.
### Instance Properties
- [var physical_address: hv_ipa_t](hv_vcpu_exit_exception_t/physical_address.md)
  The intermediate physical address of the exception in the client.
- [var syndrome: hv_exception_syndrome_t](hv_vcpu_exit_exception_t/syndrome.md)
  The vCPU exception syndrome causing the exception.
- [var virtual_address: hv_exception_address_t](hv_vcpu_exit_exception_t/virtual_address.md)
  The vCPU virtual address of the exception.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct hv_cache_type_t](hv_cache_type_t.md)
  The structure that describes an instruction or data cache element.
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
- [struct hv_gic_intid_t](hv_gic_intid_t.md)
- [struct hv_gic_msi_reg_t](hv_gic_msi_reg_t.md)
- [struct hv_gic_redistributor_reg_t](hv_gic_redistributor_reg_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_exit_exception_t)*