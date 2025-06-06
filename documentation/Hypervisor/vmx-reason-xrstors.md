# VMX_REASON_XRSTORS

**Framework**: Hypervisor  
**Kind**: var

The guest attempted to execute XRSTORS which wasn’t allowed in the current configuration.

**Availability**:
- macOS ?+

## Declaration

```swift
var VMX_REASON_XRSTORS: Int { get }
```

## See Also

- [var VMX_REASON_EXC_NMI: Int](vmx_reason_exc_nmi.md)
  VMX exit due to an exception or non-maskable interrupt (NMI).
- [var VMX_REASON_IRQ: Int](vmx_reason_irq.md)
  An external interrupt arrived and the “external-interrupt exiting” VM-execution control was 1.
- [var VMX_REASON_TRIPLE_FAULT: Int](vmx_reason_triple_fault.md)
  VMX exit due to a triple fault.
- [var VMX_REASON_INIT: Int](vmx_reason_init.md)
  VMX exit due to an INIT signal.
- [var VMX_REASON_SIPI: Int](vmx_reason_sipi.md)
  VMS exit due to startup (IPI).
- [var VMX_REASON_IO_SMI: Int](vmx_reason_io_smi.md)
  VMX exited due to an I/O SMM Interrupt.
- [var VMX_REASON_OTHER_SMI: Int](vmx_reason_other_smi.md)
  An SMI arrived and caused an SMM VM exit.
- [var VMX_REASON_IRQ_WND: Int](vmx_reason_irq_wnd.md)
  VMX exited due to an Interrupt Window.
- [var VMX_REASON_VIRTUAL_NMI_WND: Int](vmx_reason_virtual_nmi_wnd.md)
  At the beginning of an instruction, there was no virtual-NMI blocking.
- [var VMX_REASON_TASK: Int](vmx_reason_task.md)
  The guest attempted a task switch.
- [var VMX_REASON_CPUID: Int](vmx_reason_cpuid.md)
  The guest software attempted to execute the CPUID instruction.
- [var VMX_REASON_GETSEC: Int](vmx_reason_getsec.md)
  The guest attempted to execute GETSEC instruction.
- [var VMX_REASON_HLT: Int](vmx_reason_hlt.md)
  The guest attempted to execute HLT and the “HLT exiting” VM-execution control was 1.
- [var VMX_REASON_INVD: Int](vmx_reason_invd.md)
  The guest attempted to execute Invalidate Caches (INVD) instruction.
- [var VMX_REASON_INVLPG: Int](vmx_reason_invlpg.md)
  The guest attempted to execute the Invalidate TLB Entry (INVLPG) instruction and the “INVLPG exiting” VM-execution control was 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/vmx_reason_xrstors)*