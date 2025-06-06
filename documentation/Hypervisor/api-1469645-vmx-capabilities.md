# VMX Capabilities

**Framework**: Hypervisor

An enumeration that represents the available VMX capabilities.

#### Overview

The capabilites available to the hypervisor can vary depending on the specific hardware platform or OS release. Use the [`hv_vmx_read_capability(_:_:)`](hv_vmx_read_capability(_:_:).md) API at run time to determine the capabilities that can you can select.

The example below demonstrates the process for checking for the availability a specific capability, here checking for the avaiability of timestamp-counter scaling (TSC scaling):

```objc
static uint64_t canonicalize(uint64_t ctrl, uint64_t mask) {
    return (ctrl | (mask & 0xffffffff)) & (mask >> 32);
}

main() {
    
    // Fetch the supported capabilities for the PROCBASED2 field
    if (hv_vmx_read_capability(HV_VMX_CAP_PROCBASED2, &proc2_cap) != 0)
        errx(1, "vcpu_read_capability(%u, CAP_VMX_PROCBASED2) failed", vcpu);
    
    // Apply the constraints to our request to use TSC scaling
    const uint64_t newcap = canonicalize(CPU_BASED2_TSC_SCALING, proc2_cap);
    
    // Test to see if that bit is supported on this platform
    if ((newcap & CPU_BASED2_TSC_SCALING) == 0) {
        warnx(“TSC scaling not supported on this platform”);
    }
    
    // Continue, but without TSC scaling ...
    write_vmcs(vcpu, VMCS_CTRL_CPU_BASED2, newcap);

    // ...
}

```

## Topics

### Capabilities
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
- [var CPU_BASED_CR8_STORE: UInt32](cpu_based_cr8_store.md)
  The value that controls whether executions of MOV from Control Register 8 (CR8) cause VM exits.
- [var CPU_BASED_TPR_SHADOW: UInt32](cpu_based_tpr_shadow.md)
  The value that controls enabling Task Priority Register (TPR) virtualization and other APIC-virtualization features.
- [var CPU_BASED_VIRTUAL_NMI_WND: UInt32](cpu_based_virtual_nmi_wnd.md)
  The value that controls if a VM exit occurs at the beginning of any instruction if there’s no virtual-NMI blocking.
- [var CPU_BASED_MOV_DR: UInt32](cpu_based_mov_dr.md)
  The value that controls whether executions of MOV to or from Debug Registers (DR) cause VM exits.
- [var CPU_BASED_UNCOND_IO: UInt32](cpu_based_uncond_io.md)
  The value that controls whether executions of various I/O instructions cause VM exits.
- [var CPU_BASED_IO_BITMAPS: UInt32](cpu_based_io_bitmaps.md)
  The value that controls whether to use I/O bitmaps to restrict executions of I/O instructions.
- [var CPU_BASED_MTF: UInt32](cpu_based_mtf.md)
  The value that controls enabling the monitor trap flag debugging feature.
- [var CPU_BASED_MSR_BITMAPS: UInt32](cpu_based_msr_bitmaps.md)
  The value that controls use of whether Model Specific Register (MSR) bitmaps to control execution of the read-from and write-to MSR instructions.
- [var CPU_BASED_MONITOR: UInt32](cpu_based_monitor.md)
  The value that controls whether executions of the Set Up Monitor Address instruction (MONITOR) cause VM exits.
- [var CPU_BASED_PAUSE: UInt32](cpu_based_pause.md)
  The value that controls whether executions of spin-wait loop (PAUSE) instruction causes VM exits.
- [var CPU_BASED_SECONDARY_CTLS: UInt32](cpu_based_secondary_ctls.md)
  The value that conntrols use of the secondary processor-based VM-execution controls.
- [var CPU_BASED2_VIRTUAL_APIC: UInt32](cpu_based2_virtual_apic.md)
  The value that controls whether the logical processor provides special treatment for access to the Advanced Programmable Interrupt Controller (APIC).
- [var CPU_BASED2_EPT: UInt32](cpu_based2_ept.md)
  The value that controls enabling extended page tables (EPT).
- [var CPU_BASED2_DESC_TABLE: UInt32](cpu_based2_desc_table.md)
  The value that controls whether executions of descriptor table instructions cause VM exits.
- [var CPU_BASED2_RDTSCP: UInt32](cpu_based2_rdtscp.md)
  The value that controls whether any execution of read timestamp-counter and processor ID instruction (RDTSCP) causes an invalid-opcode exception.
- [var CPU_BASED2_X2APIC: UInt32](cpu_based2_x2apic.md)
  The value that controls the logical processor’s treatment of reading/writing of Model Specific Registers to APIC MSRs.
- [var CPU_BASED2_VPID: UInt32](cpu_based2_vpid.md)
  The value that controls the association of cached translations of linear addresses with a virtual processor identifier (VPID).
- [var CPU_BASED2_WBINVD: UInt32](cpu_based2_wbinvd.md)
  The value that controls whether executions of the Invalidate Cache with Writeback instruction (WBINVD) cause VM exits.
- [var CPU_BASED2_UNRESTRICTED: UInt32](cpu_based2_unrestricted.md)
  The value that controls whether guest software may run in unpaged protected mode or in real address mode.
- [var CPU_BASED2_APIC_REG_VIRT: UInt32](cpu_based2_apic_reg_virt.md)
  This value controls whether the logical processor virtualizes certain advanced programmable interrupt controller (APIC) accesses.
- [var CPU_BASED2_VIRT_INTR_DELIVERY: UInt32](cpu_based2_virt_intr_delivery.md)
  The value that enables evaluation and delivery of pending virtual interrupts and emulation of writes to the APIC registers that control interrupt prioritization.
- [var CPU_BASED2_PAUSE_LOOP: UInt32](cpu_based2_pause_loop.md)
  The value that controls whether a series of executions of the PAUSE instruction can cause a VM exit.
- [var CPU_BASED2_RDRAND: UInt32](cpu_based2_rdrand.md)
  The value that controls whether executions of the hardware random number generator instruction (RDRAND) cause VM exits.
- [var CPU_BASED2_INVPCID: UInt32](cpu_based2_invpcid.md)
  The value that controls whether any execution of the Invalidate Process-Context Identifier instruction (INVPCID) causes an invalid opcode exception.
- [var CPU_BASED2_VMFUNC: UInt32](cpu_based2_vmfunc.md)
  The value that enables use of the “Invoke VM function” (VMFUNC) instruction in VMX non-root operation.
- [var CPU_BASED2_VMCS_SHADOW: UInt32](cpu_based2_vmcs_shadow.md)
  The value that controls whether execution of VMREAD and VMWRITE in VMX non-root operation may access a shadow VMCS instead of causing a VM exit.
- [var CPU_BASED2_ENCLS_EXIT_MAP: UInt32](cpu_based2_encls_exit_map.md)
  The value that controls whether executions of Enclave Instruction Leaf Functions (ENCLS) cause examination of the ENCLS-exiting bitmap to determine whether the instruction causes a VM exit.
- [var CPU_BASED2_RDSEED: UInt32](cpu_based2_rdseed.md)
  The value that controls whether executions of random number generator instructions (RDSEED) cause VM exits.
- [var CPU_BASED2_PML: UInt32](cpu_based2_pml.md)
  The value that controls whether an access to a guest-physical address that sets an extended page table (EPT) dirty bit also adds an entry to the page-modification log.
- [var CPU_BASED2_EPT_VE: UInt32](cpu_based2_ept_ve.md)
  The value that controls whether extended page table (EPT) violations cause virtualization exceptions instead of VM exits.
- [var CPU_BASED2_PT_CONCEAL_VMX: UInt32](cpu_based2_pt_conceal_vmx.md)
  The value that controls whether the processor trace facility suppresses information that the processor was in VMX non-root operation.
- [var CPU_BASED2_XSAVES_XRSTORS: UInt32](cpu_based2_xsaves_xrstors.md)
  The value that controls whether any execution of save or restore state instructions (XSAVES or XRSTORS) causes an invalid opcode exception.
- [var CPU_BASED2_EPT_MODE_BASED_EXEC: UInt32](cpu_based2_ept_mode_based_exec.md)
  The value that controls whether to base extended page table (EPT) execute permissions on whether access to a linear address is supervisor or user mode.
- [var CPU_BASED2_EPT_SUBPAGE_WRITE: UInt32](cpu_based2_ept_subpage_write.md)
  The value that controls whether extended page table (EPT) write permissions specify granularity of 128 bytes.
- [var CPU_BASED2_PT_GUEST_PHYSICAL: UInt32](cpu_based2_pt_guest_physical.md)
  The value that controls whether to treat all output addresses used by Intel Processor Trace as guest-physical addresses and translated using the extended page table.
- [var CPU_BASED2_TSC_SCALING: UInt32](cpu_based2_tsc_scaling.md)
  The value that controls whether the execution of various read time stamp counters and read model-specific registers that read from the IA32 timestamp counter model specific register return a value modified by the TSC multiplier field.
- [var CPU_BASED2_USER_WAIT_PAUSE: UInt32](cpu_based2_user_wait_pause.md)
  The value that controls whether any execution of TPAUSE, UMONITOR, or UMWAIT instrucitons generate an illegal opcode exception.
- [var CPU_BASED2_ENCLV_EXIT_MAP: UInt32](cpu_based2_enclv_exit_map.md)
  The value that controls whether executions of an enclave VMM function instruction (ENCLV) checks the ENCLV-exiting bitmap to determine whether the instruction causes a VM exit.
- [var VMX_EPT_VPID_SUPPORT_AD: UInt32](vmx_ept_vpid_support_ad.md)
  The value that controls if extended page tables (EPT) support accessed and dirty flags.
- [var VMX_EPT_VPID_SUPPORT_EXONLY: UInt32](vmx_ept_vpid_support_exonly.md)
  The value that controls whether extended page tables (EPT) support execute-only translations.
- [var VMEXIT_SAVE_DBG_CONTROLS: UInt32](vmexit_save_dbg_controls.md)
  Thievalue that controls whether to save debug register 7 DR7 and the IA32 debug control DEBUGCTL MSR on VM exit.
- [var VMEXIT_HOST_IA32E: UInt32](vmexit_host_ia32e.md)
  This value controls, on processors that support Intel 64 architecture, whether a logical processor is in 64-bit mode after the next VM exit.
- [var VMEXIT_LOAD_IA32_PERF_GLOBAL_CTRL: UInt32](vmexit_load_ia32_perf_global_ctrl.md)
  The value that controls whether to load the IA32_PERF_GLOBAL_CTRL model specific register on VM exit.
- [var VMEXIT_ACK_INTR: UInt32](vmexit_ack_intr.md)
  The value that controls whether the logical processor sends an acknowledgement to the interrupt controller when the VM exits.
- [var VMEXIT_SAVE_IA32_PAT: UInt32](vmexit_save_ia32_pat.md)
  The value that controls whether to save the IA32_EFER model specific register on VM exit.
- [var VMEXIT_LOAD_IA32_PAT: UInt32](vmexit_load_ia32_pat.md)
  The value that controls whether to load the IA32_EFER mode specific register on VM exit.
- [var VMEXIT_SAVE_EFER: UInt32](vmexit_save_efer.md)
  The value that controls whether to save the IA32_EFER MSR on VM exit.
- [var VMEXIT_LOAD_EFER: UInt32](vmexit_load_efer.md)
  The value that controls whether to load the IA32_EFER MSR on VM exit.
- [var VMEXIT_SAVE_VMX_TIMER: UInt32](vmexit_save_vmx_timer.md)
  The value that controls whether to save the value of the VMX-preemption timer on VM exit.
- [var VMEXIT_CLEAR_IA32_BNDCFGS: UInt32](vmexit_clear_ia32_bndcfgs.md)
  The value that controls whether to clear the IA32_BNDCFGS model specific register on VM exit.
- [var VMEXIT_PT_CONCEAL_VMX: UInt32](vmexit_pt_conceal_vmx.md)
  The value that controls whether the Intel Processor Trace produces a paging information packet on VM exit or a VMCS packet on SMM VM exit.
- [var VMEXIT_CLEAR_IA32_RTIT_CTL: UInt32](vmexit_clear_ia32_rtit_ctl.md)
  The value that controls whether to clear the IA32_RTIT_CTL model specific register (MSR) on VM exit.
- [var VMEXIT_LOAD_CET_STATE: UInt32](vmexit_load_cet_state.md)
  The value that controls whether to load CET-related MSRs and SPP on VM exit.
- [var VMENTRY_LOAD_DBG_CONTROLS: UInt32](vmentry_load_dbg_controls.md)
  The value that controls whetherto load Debug Register 7 and the IA32_DEBUGCTL model specific register (MSR) on VM entry.
- [var VMENTRY_GUEST_IA32E: UInt32](vmentry_guest_ia32e.md)
  The value that controls whether the logical processor is in IA-32e mode after VM entry.
- [var VMENTRY_SMM: UInt32](vmentry_smm.md)
  The value that controls whether the logical processor is in system-management mode (SMM) after VM entry.
- [var VMENTRY_DEACTIVATE_DUAL_MONITOR: UInt32](vmentry_deactivate_dual_monitor.md)
  The value that controls whether the treatment of SMIs and system-management mode (SMM) is in effect after the VM entry.
- [var VMENTRY_LOAD_IA32_PERF_GLOBAL_CTRL: UInt32](vmentry_load_ia32_perf_global_ctrl.md)
  The value that controls whether to load the IA32_PERF_GLOBAL_CTRL model specific register on VM entry.
- [var VMENTRY_LOAD_IA32_PAT: UInt32](vmentry_load_ia32_pat.md)
  The value that controls whether to load the IA32_PAT model specific register on VM entry.
- [var VMENTRY_LOAD_EFER: UInt32](vmentry_load_efer.md)
  The value that determines whether to load the IA32_EFER model specific register on VM entry.
- [var VMENTRY_LOAD_IA32_BNDCFGS: UInt32](vmentry_load_ia32_bndcfgs.md)
  The value that controls whether to load the IA32_BNDCFGS model specific register on VM entry.
- [var VMENTRY_PT_CONCEAL_VMX: UInt32](vmentry_pt_conceal_vmx.md)
  The value that controls whether the Intel Processor Trace produces a paging information packet (PIP) on a VM entry or a VMCS packet on a VM entry that returns from system-management mode.
- [var VMENTRY_LOAD_IA32_RTIT_CTL: UInt32](vmentry_load_ia32_rtit_ctl.md)
  The value that controls whether to clear the IA32_RTIT_CTL model specific register (MSR) on VM exit.
- [var VMENTRY_LOAD_CET_STATE: UInt32](vmentry_load_cet_state.md)
  The value that controls whether to load CET-related model specific registers and SPP on VM exit.

## See Also

- [func hv_vmx_read_capability(hv_vmx_capability_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_read_capability(_:_:).md)
  Returns, by reference, the VMX virtualization capabilities of the host processor.
- [func hv_vmx_get_msr_info(hv_vmx_msr_info_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_get_msr_info(_:_:).md)
  Returns information about guest MSR configuration.
- [struct hv_vmx_capability_t](hv_vmx_capability_t.md)
  The type that describes Virtual Machine Extensions (VMX) capability fields.
- [typealias hv_vmx_msr_info_t](hv_vmx_msr_info_t.md)
  The type that describes Move to Status Register (MSR) information fields.
- [MSR Information Fields](3567084-msr-information-fields.md)
  The type that describes Machine Specific Register (MSR) fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/1469645-vmx-capabilities)*