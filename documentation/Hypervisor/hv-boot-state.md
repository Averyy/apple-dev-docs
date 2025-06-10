# hv_boot_state

**Framework**: Hypervisor  
**Kind**: enum

**Availability**:
- macOS ?+

## Declaration

```swift
@frozen
enum hv_boot_state
```

## Topics

### Enumeration Cases
- [hv_boot_state.HV_BS_INIT](hv_boot_state/hv_bs_init.md)
- [hv_boot_state.HV_BS_RUNNING](hv_boot_state/hv_bs_running.md)
- [hv_boot_state.HV_BS_SIPI](hv_boot_state/hv_bs_sipi.md)
### Initializers
- [init?(rawValue: UInt32)](hv_boot_state/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [VM Creation Options](1447306-vm-creation-options.md)
  Constants that describe the creation options for a virtual machine.
- [VM Capabilities](3181560-vm-capabilities.md)
  An enumeration that describes the capabilities of the system.
- [struct hv_cache_type_t](hv_cache_type_t.md)
  The structure that describes an instruction or data cache element.
- [struct hv_apic_ctrl_t](hv_apic_ctrl_t.md)
- [struct hv_apic_intr_trigger_t](hv_apic_intr_trigger_t.md)
- [struct hv_apic_lvt_flavor_t](hv_apic_lvt_flavor_t.md)
- [struct hv_gic_distributor_reg_t](hv_gic_distributor_reg_t.md)
- [struct hv_gic_icc_reg_t](hv_gic_icc_reg_t.md)
- [struct hv_gic_ich_reg_t](hv_gic_ich_reg_t.md)
- [struct hv_gic_icv_reg_t](hv_gic_icv_reg_t.md)
- [struct hv_gic_intid_t](hv_gic_intid_t.md)
- [struct hv_gic_msi_reg_t](hv_gic_msi_reg_t.md)
- [struct hv_gic_redistributor_reg_t](hv_gic_redistributor_reg_t.md)
- [struct hv_sme_p_reg_t](hv_sme_p_reg_t.md)
- [struct hv_sme_z_reg_t](hv_sme_z_reg_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_boot_state)*