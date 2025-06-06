# VMENTRY_PT_CONCEAL_VMX

**Framework**: Hypervisor  
**Kind**: var

The value that controls whether the Intel Processor Trace produces a paging information packet (PIP) on a VM entry or a VMCS packet on a VM entry that returns from system-management mode.

**Availability**:
- macOS ?+

## Declaration

```swift
var VMENTRY_PT_CONCEAL_VMX: UInt32 { get }
```

#### Discussion

Must be `0`.

## See Also

- [var PIN_BASED_INTR: UInt32](pin_based_intr.md)
  The value that controls whether external interrupts cause VM exits.
- [var PIN_BASED_NMI: UInt32](pin_based_nmi.md)
  The value that controls whether external non-maskable interrupts cause VM exits.
- [var PIN_BASED_VIRTUAL_NMI: UInt32](pin_based_virtual_nmi.md)
  The value that controls blocking of non-maskable interrupts.
- [var PIN_BASED_PREEMPTION_TIMER: UInt32](pin_based_preemption_timer.md)
  The value that controls whether the VMX-preemption timer counts down in VMX non-root operation.
- [var PIN_BASED_POSTED_INTR: UInt32](pin_based_posted_intr.md)
  The value that controls whether the processor gives special treatment to interrupts with posted-interrupt notification vectors.
- [var CPU_BASED_IRQ_WND: UInt32](cpu_based_irq_wnd.md)
  The value that controls whether a VM exits at the beginning of any instruction where there’s no blocking of interrupts and the interrupt flag is 1.
- [var CPU_BASED_TSC_OFFSET: UInt32](cpu_based_tsc_offset.md)
  The value that controls whether reading the timestamp-counter MSRs changes depending on the value of the timestamp-counter offset field.
- [var CPU_BASED_HLT: UInt32](cpu_based_hlt.md)
  The value that controls whether the execution of HALT instructions cause VM exits.
- [var CPU_BASED_INVLPG: UInt32](cpu_based_invlpg.md)
  The value that controls whether the execution of invalid page instructions (INVLPG) cause VM exits.
- [var CPU_BASED_MWAIT: UInt32](cpu_based_mwait.md)
  The value that controls whether the execution of Monitor Wait instructions (MWAIT) cause VM exits.
- [var CPU_BASED_RDPMC: UInt32](cpu_based_rdpmc.md)
  The value that controls whether the execution of Read Performance Monitoring Counters instructions (RDPMC) cause VM exits.
- [var CPU_BASED_RDTSC: UInt32](cpu_based_rdtsc.md)
  The value that controls whether the execution of Read Timestamp-Counter instructions (RDTSC) cause VM exits.
- [var CPU_BASED_CR3_LOAD: UInt32](cpu_based_cr3_load.md)
  The value that controls whether executions of MOV to Control Register 3 (CR3) cause VM exits.
- [var CPU_BASED_CR3_STORE: UInt32](cpu_based_cr3_store.md)
  The value that controls whether executions of MOV from Control Register 3 (CR3) cause VM exits.
- [var CPU_BASED_CR8_LOAD: UInt32](cpu_based_cr8_load.md)
  The value that controls whether executions of MOV to Control Register 8 (CR8) cause VM exits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/vmentry_pt_conceal_vmx)*