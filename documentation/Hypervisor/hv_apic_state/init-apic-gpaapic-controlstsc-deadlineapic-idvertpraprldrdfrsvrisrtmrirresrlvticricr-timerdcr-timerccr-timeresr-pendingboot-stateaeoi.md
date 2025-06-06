# init(apic_gpa:apic_controls:tsc_deadline:apic_id:ver:tpr:apr:ldr:dfr:svr:isr:tmr:irr:esr:lvt:icr:icr_timer:dcr_timer:ccr_timer:esr_pending:boot_state:aeoi:)

**Framework**: Hypervisor  
**Kind**: init

**Availability**:
- macOS ?+

## Declaration

```swift
init(apic_gpa: UInt64, apic_controls: UInt64, tsc_deadline: UInt64, apic_id: UInt32, ver: UInt32, tpr: UInt32, apr: UInt32, ldr: UInt32, dfr: UInt32, svr: UInt32, isr: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32), tmr: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32), irr: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32), esr: UInt32, lvt: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32), icr: (UInt32, UInt32), icr_timer: UInt32, dcr_timer: UInt32, ccr_timer: UInt32, esr_pending: UInt32, boot_state: hv_boot_state, aeoi: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32))
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_apic_state/init(apic_gpa:apic_controls:tsc_deadline:apic_id:ver:tpr:apr:ldr:dfr:svr:isr:tmr:irr:esr:lvt:icr:icr_timer:dcr_timer:ccr_timer:esr_pending:boot_state:aeoi:))*