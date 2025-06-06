# hv_atpic_state

**Framework**: Hypervisor  
**Kind**: struct

**Availability**:
- macOS ?+

## Declaration

```swift
struct hv_atpic_state
```

## Topics

### Initializers
- [init()](hv_atpic_state/init.md)
- [init(ready: Bool, icw_num: UInt8, rd_cmd_reg: UInt8, aeoi: Bool, poll: Bool, rotate: Bool, sfn: Bool, irq_base: UInt8, request: UInt8, service: UInt8, mask: UInt8, smm: Bool, last_request: UInt8, lowprio: UInt8, intr_raised: Bool, elc: UInt8)](hv_atpic_state/init(ready:icw_num:rd_cmd_reg:aeoi:poll:rotate:sfn:irq_base:request:service:mask:smm:last_request:lowprio:intr_raised:elc:).md)
### Instance Properties
- [var aeoi: Bool](hv_atpic_state/aeoi.md)
- [var elc: UInt8](hv_atpic_state/elc.md)
- [var icw_num: UInt8](hv_atpic_state/icw_num.md)
- [var intr_raised: Bool](hv_atpic_state/intr_raised.md)
- [var irq_base: UInt8](hv_atpic_state/irq_base.md)
- [var last_request: UInt8](hv_atpic_state/last_request.md)
- [var lowprio: UInt8](hv_atpic_state/lowprio.md)
- [var mask: UInt8](hv_atpic_state/mask.md)
- [var poll: Bool](hv_atpic_state/poll.md)
- [var rd_cmd_reg: UInt8](hv_atpic_state/rd_cmd_reg.md)
- [var ready: Bool](hv_atpic_state/ready.md)
- [var request: UInt8](hv_atpic_state/request.md)
- [var rotate: Bool](hv_atpic_state/rotate.md)
- [var service: UInt8](hv_atpic_state/service.md)
- [var sfn: Bool](hv_atpic_state/sfn.md)
- [var smm: Bool](hv_atpic_state/smm.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
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
- [struct hv_atpic_state_ext_t](hv_atpic_state_ext_t.md)
- [struct hv_gic_distributor_reg_t](hv_gic_distributor_reg_t.md)
- [struct hv_gic_icc_reg_t](hv_gic_icc_reg_t.md)
- [struct hv_gic_ich_reg_t](hv_gic_ich_reg_t.md)
- [struct hv_gic_icv_reg_t](hv_gic_icv_reg_t.md)
- [struct hv_gic_intid_t](hv_gic_intid_t.md)
- [struct hv_gic_msi_reg_t](hv_gic_msi_reg_t.md)
- [struct hv_gic_redistributor_reg_t](hv_gic_redistributor_reg_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_atpic_state)*