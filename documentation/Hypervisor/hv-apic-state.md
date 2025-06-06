# hv_apic_state

**Framework**: Hypervisor  
**Kind**: struct

**Availability**:
- macOS ?+

## Declaration

```swift
struct hv_apic_state
```

## Topics

### Initializers
- [init()](hv_apic_state/init.md)
- [init(apic_gpa: UInt64, apic_controls: UInt64, tsc_deadline: UInt64, apic_id: UInt32, ver: UInt32, tpr: UInt32, apr: UInt32, ldr: UInt32, dfr: UInt32, svr: UInt32, isr: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32), tmr: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32), irr: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32), esr: UInt32, lvt: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32), icr: (UInt32, UInt32), icr_timer: UInt32, dcr_timer: UInt32, ccr_timer: UInt32, esr_pending: UInt32, boot_state: hv_boot_state, aeoi: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32))](hv_apic_state/init(apic_gpa:apic_controls:tsc_deadline:apic_id:ver:tpr:apr:ldr:dfr:svr:isr:tmr:irr:esr:lvt:icr:icr_timer:dcr_timer:ccr_timer:esr_pending:boot_state:aeoi:).md)
### Instance Properties
- [var aeoi: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)](hv_apic_state/aeoi.md)
- [var apic_controls: UInt64](hv_apic_state/apic_controls.md)
- [var apic_gpa: UInt64](hv_apic_state/apic_gpa.md)
- [var apic_id: UInt32](hv_apic_state/apic_id.md)
- [var apr: UInt32](hv_apic_state/apr.md)
- [var boot_state: hv_boot_state](hv_apic_state/boot_state.md)
- [var ccr_timer: UInt32](hv_apic_state/ccr_timer.md)
- [var dcr_timer: UInt32](hv_apic_state/dcr_timer.md)
- [var dfr: UInt32](hv_apic_state/dfr.md)
- [var esr: UInt32](hv_apic_state/esr.md)
- [var esr_pending: UInt32](hv_apic_state/esr_pending.md)
- [var icr: (UInt32, UInt32)](hv_apic_state/icr.md)
- [var icr_timer: UInt32](hv_apic_state/icr_timer.md)
- [var irr: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)](hv_apic_state/irr.md)
- [var isr: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)](hv_apic_state/isr.md)
- [var ldr: UInt32](hv_apic_state/ldr.md)
- [var lvt: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)](hv_apic_state/lvt.md)
- [var svr: UInt32](hv_apic_state/svr.md)
- [var tmr: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)](hv_apic_state/tmr.md)
- [var tpr: UInt32](hv_apic_state/tpr.md)
- [var tsc_deadline: UInt64](hv_apic_state/tsc_deadline.md)
- [var ver: UInt32](hv_apic_state/ver.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_apic_state)*