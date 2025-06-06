# hv_sme_z_reg_t

**Framework**: Hypervisor  
**Kind**: struct

**Availability**:
- macOS 15.2+

## Declaration

```swift
struct hv_sme_z_reg_t
```

## Topics

### Constants
- [init(UInt32)](hv_sme_z_reg_t/init(_:).md)
- [init(rawValue: UInt32)](hv_sme_z_reg_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](hv_sme_z_reg_t/rawvalue.md)
- [var HV_SME_Z_REG_0: hv_sme_z_reg_t](hv_sme_z_reg_0.md)
- [var HV_SME_Z_REG_1: hv_sme_z_reg_t](hv_sme_z_reg_1.md)
- [var HV_SME_Z_REG_10: hv_sme_z_reg_t](hv_sme_z_reg_10.md)
- [var HV_SME_Z_REG_11: hv_sme_z_reg_t](hv_sme_z_reg_11.md)
- [var HV_SME_Z_REG_12: hv_sme_z_reg_t](hv_sme_z_reg_12.md)
- [var HV_SME_Z_REG_13: hv_sme_z_reg_t](hv_sme_z_reg_13.md)
- [var HV_SME_Z_REG_14: hv_sme_z_reg_t](hv_sme_z_reg_14.md)
- [var HV_SME_Z_REG_15: hv_sme_z_reg_t](hv_sme_z_reg_15.md)
- [var HV_SME_Z_REG_16: hv_sme_z_reg_t](hv_sme_z_reg_16.md)
- [var HV_SME_Z_REG_17: hv_sme_z_reg_t](hv_sme_z_reg_17.md)
- [var HV_SME_Z_REG_18: hv_sme_z_reg_t](hv_sme_z_reg_18.md)
- [var HV_SME_Z_REG_19: hv_sme_z_reg_t](hv_sme_z_reg_19.md)
- [var HV_SME_Z_REG_2: hv_sme_z_reg_t](hv_sme_z_reg_2.md)
- [var HV_SME_Z_REG_20: hv_sme_z_reg_t](hv_sme_z_reg_20.md)
- [var HV_SME_Z_REG_21: hv_sme_z_reg_t](hv_sme_z_reg_21.md)
- [var HV_SME_Z_REG_22: hv_sme_z_reg_t](hv_sme_z_reg_22.md)
- [var HV_SME_Z_REG_23: hv_sme_z_reg_t](hv_sme_z_reg_23.md)
- [var HV_SME_Z_REG_24: hv_sme_z_reg_t](hv_sme_z_reg_24.md)
- [var HV_SME_Z_REG_25: hv_sme_z_reg_t](hv_sme_z_reg_25.md)
- [var HV_SME_Z_REG_26: hv_sme_z_reg_t](hv_sme_z_reg_26.md)
- [var HV_SME_Z_REG_27: hv_sme_z_reg_t](hv_sme_z_reg_27.md)
- [var HV_SME_Z_REG_28: hv_sme_z_reg_t](hv_sme_z_reg_28.md)
- [var HV_SME_Z_REG_29: hv_sme_z_reg_t](hv_sme_z_reg_29.md)
- [var HV_SME_Z_REG_3: hv_sme_z_reg_t](hv_sme_z_reg_3.md)
- [var HV_SME_Z_REG_30: hv_sme_z_reg_t](hv_sme_z_reg_30.md)
- [var HV_SME_Z_REG_31: hv_sme_z_reg_t](hv_sme_z_reg_31.md)
- [var HV_SME_Z_REG_4: hv_sme_z_reg_t](hv_sme_z_reg_4.md)
- [var HV_SME_Z_REG_5: hv_sme_z_reg_t](hv_sme_z_reg_5.md)
- [var HV_SME_Z_REG_6: hv_sme_z_reg_t](hv_sme_z_reg_6.md)
- [var HV_SME_Z_REG_7: hv_sme_z_reg_t](hv_sme_z_reg_7.md)
- [var HV_SME_Z_REG_8: hv_sme_z_reg_t](hv_sme_z_reg_8.md)
- [var HV_SME_Z_REG_9: hv_sme_z_reg_t](hv_sme_z_reg_9.md)

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
- [struct hv_gic_intid_t](hv_gic_intid_t.md)
- [struct hv_gic_msi_reg_t](hv_gic_msi_reg_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_sme_z_reg_t)*