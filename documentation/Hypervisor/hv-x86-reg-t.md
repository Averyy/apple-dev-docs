# hv_x86_reg_t

**Framework**: Hypervisor  
**Kind**: struct

The type that defines x86 architectural registers.

**Availability**:
- macOS ?+

## Declaration

```swift
struct hv_x86_reg_t
```

## Topics

### Registers
- [var HV_X86_RIP: hv_x86_reg_t](hv_x86_rip.md)
  The value that identifies the x86 instruction pointer register.
- [var HV_X86_RFLAGS: hv_x86_reg_t](hv_x86_rflags.md)
  The value that identifies the x86 status register.
- [var HV_X86_RAX: hv_x86_reg_t](hv_x86_rax.md)
  The value that identifies the x86 accumulator register.
- [var HV_X86_RCX: hv_x86_reg_t](hv_x86_rcx.md)
  The value that identifies the x86 counter register.
- [var HV_X86_RDX: hv_x86_reg_t](hv_x86_rdx.md)
  The value that identifies the x86 data register.
- [var HV_X86_RBX: hv_x86_reg_t](hv_x86_rbx.md)
  The value that identifies the x86 base register.
- [var HV_X86_RSI: hv_x86_reg_t](hv_x86_rsi.md)
  The value that identifies the x86 source index register.
- [var HV_X86_RDI: hv_x86_reg_t](hv_x86_rdi.md)
  The value that identifies the x86 destination index register.
- [var HV_X86_RSP: hv_x86_reg_t](hv_x86_rsp.md)
  The value that identifies the x86 stack pointer register.
- [var HV_X86_RBP: hv_x86_reg_t](hv_x86_rbp.md)
  The value that identifies the x86 base pointer register.
- [var HV_X86_R8: hv_x86_reg_t](hv_x86_r8.md)
  The value that identifies the x86 general-purpose register R8.
- [var HV_X86_R9: hv_x86_reg_t](hv_x86_r9.md)
  The value that identifies the x86 general-purpose register R9.
- [var HV_X86_R10: hv_x86_reg_t](hv_x86_r10.md)
  The value that identifies the x86 general-purpose register R10.
- [var HV_X86_R11: hv_x86_reg_t](hv_x86_r11.md)
  The value that identifies the x86 general-purpose register R11.
- [var HV_X86_R12: hv_x86_reg_t](hv_x86_r12.md)
  The value that identifies the x86 general-purpose register R12.
- [var HV_X86_R13: hv_x86_reg_t](hv_x86_r13.md)
  The value that identifies the x86 general-purpose register R13.
- [var HV_X86_R14: hv_x86_reg_t](hv_x86_r14.md)
  The value that identifies the x86 general-purpose register R14.
- [var HV_X86_R15: hv_x86_reg_t](hv_x86_r15.md)
  The value that identifies the x86 general-purpose register R15.
- [var HV_X86_CS: hv_x86_reg_t](hv_x86_cs.md)
  The value that identifies the x86 code-segment register.
- [var HV_X86_SS: hv_x86_reg_t](hv_x86_ss.md)
  The value that identifies the x86 stack-segment register.
- [var HV_X86_DS: hv_x86_reg_t](hv_x86_ds.md)
  The value that identifies the x86 data-segment register.
- [var HV_X86_ES: hv_x86_reg_t](hv_x86_es.md)
  The value that identifies the x86 segment register ES.
- [var HV_X86_FS: hv_x86_reg_t](hv_x86_fs.md)
  The value that identifies the x86 segment register FS.
- [var HV_X86_GS: hv_x86_reg_t](hv_x86_gs.md)
  The value that identifies the x86 segment register GS.
- [var HV_X86_IDT_BASE: hv_x86_reg_t](hv_x86_idt_base.md)
  The value that identifies the x86 interrupt descriptor, table-base register.
- [var HV_X86_IDT_LIMIT: hv_x86_reg_t](hv_x86_idt_limit.md)
  The value that identifies the x86 interrupt descriptor, table-base register.
- [var HV_X86_GDT_BASE: hv_x86_reg_t](hv_x86_gdt_base.md)
  The value that identifies the x86 global descriptor, table-base register.
- [var HV_X86_GDT_LIMIT: hv_x86_reg_t](hv_x86_gdt_limit.md)
  The value that identifies the x86 global descriptor, table-limit register.
- [var HV_X86_LDTR: hv_x86_reg_t](hv_x86_ldtr.md)
  The value that identifies the x86 local descriptor, table register.
- [var HV_X86_LDT_BASE: hv_x86_reg_t](hv_x86_ldt_base.md)
  The value that identifies the x86 local descriptor, table-base register.
- [var HV_X86_LDT_LIMIT: hv_x86_reg_t](hv_x86_ldt_limit.md)
  The value that identifies the x86 local descriptor, table-limit register.
- [var HV_X86_LDT_AR: hv_x86_reg_t](hv_x86_ldt_ar.md)
  The value that identifies the x86 local descriptor table, access-rights register.
- [var HV_X86_TR: hv_x86_reg_t](hv_x86_tr.md)
  The value that identifies the x86 task register.
- [var HV_X86_TSS_BASE: hv_x86_reg_t](hv_x86_tss_base.md)
  The value that identifies the x86 task-state, segment-base register.
- [var HV_X86_TSS_LIMIT: hv_x86_reg_t](hv_x86_tss_limit.md)
  The value that identifies the x86 task state segment limit register.
- [var HV_X86_TSS_AR: hv_x86_reg_t](hv_x86_tss_ar.md)
  The value that identifies the x86 task-state, segment-access, rights register.
- [var HV_X86_CR0: hv_x86_reg_t](hv_x86_cr0.md)
  The value that identifies the x86 control-register CR0.
- [var HV_X86_CR1: hv_x86_reg_t](hv_x86_cr1.md)
  The value that identifies the x86 control-register CR1.
- [var HV_X86_CR2: hv_x86_reg_t](hv_x86_cr2.md)
  The value that identifies the x86 control-register CR2.
- [var HV_X86_CR3: hv_x86_reg_t](hv_x86_cr3.md)
  The value that identifies the x86 control-register CR3.
- [var HV_X86_CR4: hv_x86_reg_t](hv_x86_cr4.md)
  The value that identifies the x86 control-register CR4.
- [var HV_X86_DR0: hv_x86_reg_t](hv_x86_dr0.md)
  The value that identifies the x86 debug-register DR0.
- [var HV_X86_DR1: hv_x86_reg_t](hv_x86_dr1.md)
  The value that identifies the x86 debug-register DR1.
- [var HV_X86_DR2: hv_x86_reg_t](hv_x86_dr2.md)
  The value that identifies the x86 debug-register DR2.
- [var HV_X86_DR3: hv_x86_reg_t](hv_x86_dr3.md)
  The value that identifies the x86 debug-register DR3.
- [var HV_X86_DR4: hv_x86_reg_t](hv_x86_dr4.md)
  The value that identifies the x86 debug-register DR4.
- [var HV_X86_DR5: hv_x86_reg_t](hv_x86_dr5.md)
  The value that identifies the x86 debug-register DR5.
- [var HV_X86_DR6: hv_x86_reg_t](hv_x86_dr6.md)
  The value that identifies the x86 debug-register DR6.
- [var HV_X86_DR7: hv_x86_reg_t](hv_x86_dr7.md)
  The value that identifies the x86 debug-register DR7.
- [var HV_X86_TPR: hv_x86_reg_t](hv_x86_tpr.md)
  The value that identifies the x86 task-priority register.
- [var HV_X86_XCR0: hv_x86_reg_t](hv_x86_xcr0.md)
  The value that identifies the x86 extended-control register.
- [var HV_X86_REGISTERS_MAX: hv_x86_reg_t](hv_x86_registers_max.md)
  The value that identifies the maximum value of x86 register constants.
### Initializers
- [init(UInt32)](hv_x86_reg_t/init(_:).md)
  Creates a new x86 architectural register instance.
- [init(rawValue: UInt32)](hv_x86_reg_t/init(rawvalue:).md)
  Creates a new x86 architectural register instance.
### Raw Value
- [var rawValue: UInt32](hv_x86_reg_t/rawvalue.md)
  An unsigned 32-bit integer representing the x86 architectural registers.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func hv_vcpu_read_register(hv_vcpuid_t, hv_x86_reg_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_read_register(_:_:_:).md)
  Returns, by reference, the current value of an architectural x86 register of a vCPU.
- [func hv_vcpu_write_register(hv_vcpuid_t, hv_x86_reg_t, UInt64) -> hv_return_t](hv_vcpu_write_register(_:_:_:).md)
  Sets the value of an architectural x86 register of a vCPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_x86_reg_t)*