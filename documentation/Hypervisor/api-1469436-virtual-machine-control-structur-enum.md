# Virtual Machine control structure (VMCS) Field IDs

**Framework**: Hypervisor

Identify the fields of the virtual machine control structure.

#### Overview

Used by the functions [`hv_vmx_vcpu_read_vmcs(_:_:_:)`](hv_vmx_vcpu_read_vmcs(_:_:_:).md) and [`hv_vmx_vcpu_write_vmcs(_:_:_:)`](hv_vmx_vcpu_write_vmcs(_:_:_:).md). The VMCS fields are read-only or read-write by the Hypervisor framework, according to the following table:

Readable and Writable VMCS Fields - Guest Fields

| Guest | Field |
| --- | --- |
| RIP, RSP, RFLAGS |  |
| CR3, CR4, DR7 |  |
| Selector | {ES, CS, SS, DS, FS, GS, LDTR, TR} |
| Base | {ES, CS, SS, DS, FS, GS, LDTR, TR, GDTR, IDTR} |
| Limit | {ES, CS, SS, DS, FS, GS, LDTR, TR, GDTR, IDTR} |
| Access Rights | {ES, CS, SS, DS, FS, GS, LDTR, TR} |
| PDPTE | {0, 1, 2, 3} |
| CR3-Target | {0, 1, 2, 3} |
| IA32_SYSENTER_CS |  |
| IA32_SYSENTER_ESP |  |
| IA32_SYSENTER_EIP |  |
| IA32_EFER |  |
| Interruptibility State |  |
| Pending Debug Exceptions |  |

Readable and Writable VMCS Fields - Control Fields

| Control Field |
| --- |
| Exception Bitmap |
| Page-Fault Error-Code Mask |
| VM-Entry Interruption-Information Field |
| VM-Entry Exception Error Code |
| VM-Entry Instruction Length |
| TPR Threshold |
| PLE Gap |
| PLE Window |
| CR0 Guest/Host Mask |
| CR4 Guest/Host Mask |
| CR0 Read Shadow |
| CR4 Read Shadow |

Readable and Conditionally Writable VMCS Fields - Guest Fields

| Guest Field | Condition |
| --- | --- |
| CR0 | CR0.CD and CR0.NW are unset |
| Activity State | ACTIVE or HLT |

Readable and Conditionally Writable VMCS Fields - Control Fields

| Control Field | Condition |
| --- | --- |
| CR0 Guest/Host Mask | CR0.CD and CR0.NW are set |
| Pin-Based VM-Execution Controls | [`hv_vmx_read_capability(_:_:)`](hv_vmx_read_capability(_:_:).md) returns true |
| Primary Processor-Based VM-ExecutionControls | [`hv_vmx_read_capability(_:_:)`](hv_vmx_read_capability(_:_:).md) returns true |
| Secondary Processor-Based VM-ExecutionControls | [`hv_vmx_read_capability(_:_:)`](hv_vmx_read_capability(_:_:).md) returns true |
| VM-Entry Controls | [`hv_vmx_read_capability(_:_:)`](hv_vmx_read_capability(_:_:).md) returns true |

Read-Only VMCS Fields - Control Fields

| Control Field |
| --- |
| TSC Offset |
| APIC-Access Address |

Read-Only VMCS Fields - Data Fields

| Data Fields |
| --- |
| VM-Instruction Error |
| Exit Reason |
| VM-Exit Interruption Information |
| VM-Exit Interruption Error Code |
| IDT-Vectoring Information Field |
| IDT-Vectoring Error Code |
| VM-Exit Instruction Length |
| VM-Exit Instruction Information |
| Guest-Physical Address |
| Exit Qualification |
| Guest-Linear Address |

## Topics

### IDs
- [var VMCS_VPID: Int](vmcs_vpid.md)
- [var VMCS_CTRL_POSTED_INT_N_VECTOR: Int](vmcs_ctrl_posted_int_n_vector.md)
- [var VMCS_CTRL_EPTP_INDEX: Int](vmcs_ctrl_eptp_index.md)
- [var VMCS_GUEST_ES: Int](vmcs_guest_es.md)
- [var VMCS_GUEST_CS: Int](vmcs_guest_cs.md)
- [var VMCS_GUEST_SS: Int](vmcs_guest_ss.md)
- [var VMCS_GUEST_DS: Int](vmcs_guest_ds.md)
- [var VMCS_GUEST_FS: Int](vmcs_guest_fs.md)
- [var VMCS_GUEST_GS: Int](vmcs_guest_gs.md)
- [var VMCS_GUEST_LDTR: Int](vmcs_guest_ldtr.md)
- [var VMCS_GUEST_TR: Int](vmcs_guest_tr.md)
- [var VMCS_GUEST_INT_STATUS: Int](vmcs_guest_int_status.md)
- [var VMCS_GUESTPML_INDEX: Int](vmcs_guestpml_index.md)
- [var VMCS_HOST_ES: Int](vmcs_host_es.md)
- [var VMCS_HOST_CS: Int](vmcs_host_cs.md)
- [var VMCS_HOST_SS: Int](vmcs_host_ss.md)
- [var VMCS_HOST_DS: Int](vmcs_host_ds.md)
- [var VMCS_HOST_FS: Int](vmcs_host_fs.md)
- [var VMCS_HOST_GS: Int](vmcs_host_gs.md)
- [var VMCS_HOST_TR: Int](vmcs_host_tr.md)
- [var VMCS_CTRL_IO_BITMAP_A: Int](vmcs_ctrl_io_bitmap_a.md)
- [var VMCS_CTRL_IO_BITMAP_B: Int](vmcs_ctrl_io_bitmap_b.md)
- [var VMCS_CTRL_MSR_BITMAPS: Int](vmcs_ctrl_msr_bitmaps.md)
- [var VMCS_CTRL_VMEXIT_MSR_STORE_ADDR: Int](vmcs_ctrl_vmexit_msr_store_addr.md)
- [var VMCS_CTRL_VMEXIT_MSR_LOAD_ADDR: Int](vmcs_ctrl_vmexit_msr_load_addr.md)
- [var VMCS_CTRL_VMENTRY_MSR_LOAD_ADDR: Int](vmcs_ctrl_vmentry_msr_load_addr.md)
- [var VMCS_CTRL_EXECUTIVE_VMCS_PTR: Int](vmcs_ctrl_executive_vmcs_ptr.md)
- [var VMCS_CTRL_PML_ADDR: Int](vmcs_ctrl_pml_addr.md)
- [var VMCS_CTRL_TSC_OFFSET: Int](vmcs_ctrl_tsc_offset.md)
- [var VMCS_CTRL_VIRTUAL_APIC: Int](vmcs_ctrl_virtual_apic.md)
- [var VMCS_CTRL_APIC_ACCESS: Int](vmcs_ctrl_apic_access.md)
- [var VMCS_CTRL_POSTED_INT_DESC_ADDR: Int](vmcs_ctrl_posted_int_desc_addr.md)
- [var VMCS_CTRL_VMFUNC_CTRL: Int](vmcs_ctrl_vmfunc_ctrl.md)
- [var VMCS_CTRL_EPTP: Int](vmcs_ctrl_eptp.md)
- [var VMCS_CTRL_EOI_EXIT_BITMAP_0: Int](vmcs_ctrl_eoi_exit_bitmap_0.md)
- [var VMCS_CTRL_EOI_EXIT_BITMAP_1: Int](vmcs_ctrl_eoi_exit_bitmap_1.md)
- [var VMCS_CTRL_EOI_EXIT_BITMAP_2: Int](vmcs_ctrl_eoi_exit_bitmap_2.md)
- [var VMCS_CTRL_EOI_EXIT_BITMAP_3: Int](vmcs_ctrl_eoi_exit_bitmap_3.md)
- [var VMCS_CTRL_EPTP_LIST_ADDR: Int](vmcs_ctrl_eptp_list_addr.md)
- [var VMCS_CTRL_VMREAD_BITMAP_ADDR: Int](vmcs_ctrl_vmread_bitmap_addr.md)
- [var VMCS_CTRL_VMWRITE_BITMAP_ADDR: Int](vmcs_ctrl_vmwrite_bitmap_addr.md)
- [var VMCS_CTRL_VIRT_EXC_INFO_ADDR: Int](vmcs_ctrl_virt_exc_info_addr.md)
- [var VMCS_CTRL_XSS_EXITING_BITMAP: Int](vmcs_ctrl_xss_exiting_bitmap.md)
- [var VMCS_CTRL_ENCLS_EXITING_BITMAP: Int](vmcs_ctrl_encls_exiting_bitmap.md)
- [var VMCS_CTRL_SPP_TABLE: Int](vmcs_ctrl_spp_table.md)
- [var VMCS_CTRL_TSC_MULTIPLIER: Int](vmcs_ctrl_tsc_multiplier.md)
- [var VMCS_GUEST_PHYSICAL_ADDRESS: Int](vmcs_guest_physical_address.md)
- [var VMCS_GUEST_LINK_POINTER: Int](vmcs_guest_link_pointer.md)
- [var VMCS_GUEST_IA32_DEBUGCTL: Int](vmcs_guest_ia32_debugctl.md)
- [var VMCS_GUEST_IA32_PAT: Int](vmcs_guest_ia32_pat.md)
- [var VMCS_GUEST_IA32_EFER: Int](vmcs_guest_ia32_efer.md)
- [var VMCS_GUEST_IA32_PERF_GLOBAL_CTRL: Int](vmcs_guest_ia32_perf_global_ctrl.md)
- [var VMCS_GUEST_PDPTE0: Int](vmcs_guest_pdpte0.md)
- [var VMCS_GUEST_PDPTE1: Int](vmcs_guest_pdpte1.md)
- [var VMCS_GUEST_PDPTE2: Int](vmcs_guest_pdpte2.md)
- [var VMCS_GUEST_PDPTE3: Int](vmcs_guest_pdpte3.md)
- [var VMCS_GUEST_IA32_BNDCFGS: Int](vmcs_guest_ia32_bndcfgs.md)
- [var VMCS_GUEST_IA32_RTIT_CTL: Int](vmcs_guest_ia32_rtit_ctl.md)
- [var VMCS_HOST_IA32_PAT: Int](vmcs_host_ia32_pat.md)
- [var VMCS_HOST_IA32_EFER: Int](vmcs_host_ia32_efer.md)
- [var VMCS_HOST_IA32_PERF_GLOBAL_CTRL: Int](vmcs_host_ia32_perf_global_ctrl.md)
- [var VMCS_CTRL_PIN_BASED: Int](vmcs_ctrl_pin_based.md)
- [var VMCS_CTRL_CPU_BASED: Int](vmcs_ctrl_cpu_based.md)
- [var VMCS_CTRL_EXC_BITMAP: Int](vmcs_ctrl_exc_bitmap.md)
- [var VMCS_CTRL_PF_ERROR_MASK: Int](vmcs_ctrl_pf_error_mask.md)
- [var VMCS_CTRL_PF_ERROR_MATCH: Int](vmcs_ctrl_pf_error_match.md)
- [var VMCS_CTRL_CR3_COUNT: Int](vmcs_ctrl_cr3_count.md)
- [var VMCS_CTRL_VMEXIT_CONTROLS: Int](vmcs_ctrl_vmexit_controls.md)
- [var VMCS_CTRL_VMEXIT_MSR_STORE_COUNT: Int](vmcs_ctrl_vmexit_msr_store_count.md)
- [var VMCS_CTRL_VMEXIT_MSR_LOAD_COUNT: Int](vmcs_ctrl_vmexit_msr_load_count.md)
- [var VMCS_CTRL_VMENTRY_CONTROLS: Int](vmcs_ctrl_vmentry_controls.md)
- [var VMCS_CTRL_VMENTRY_MSR_LOAD_COUNT: Int](vmcs_ctrl_vmentry_msr_load_count.md)
- [var VMCS_CTRL_VMENTRY_IRQ_INFO: Int](vmcs_ctrl_vmentry_irq_info.md)
- [var VMCS_CTRL_VMENTRY_EXC_ERROR: Int](vmcs_ctrl_vmentry_exc_error.md)
- [var VMCS_CTRL_VMENTRY_INSTR_LEN: Int](vmcs_ctrl_vmentry_instr_len.md)
- [var VMCS_CTRL_TPR_THRESHOLD: Int](vmcs_ctrl_tpr_threshold.md)
- [var VMCS_CTRL_CPU_BASED2: Int](vmcs_ctrl_cpu_based2.md)
- [var VMCS_CTRL_PLE_GAP: Int](vmcs_ctrl_ple_gap.md)
- [var VMCS_CTRL_PLE_WINDOW: Int](vmcs_ctrl_ple_window.md)
- [var VMCS_RO_INSTR_ERROR: Int](vmcs_ro_instr_error.md)
- [var VMCS_RO_EXIT_REASON: Int](vmcs_ro_exit_reason.md)
- [var VMCS_RO_VMEXIT_IRQ_INFO: Int](vmcs_ro_vmexit_irq_info.md)
- [var VMCS_RO_VMEXIT_IRQ_ERROR: Int](vmcs_ro_vmexit_irq_error.md)
- [var VMCS_RO_IDT_VECTOR_INFO: Int](vmcs_ro_idt_vector_info.md)
- [var VMCS_RO_IDT_VECTOR_ERROR: Int](vmcs_ro_idt_vector_error.md)
- [var VMCS_RO_VMEXIT_INSTR_LEN: Int](vmcs_ro_vmexit_instr_len.md)
- [var VMCS_RO_VMX_INSTR_INFO: Int](vmcs_ro_vmx_instr_info.md)
- [var VMCS_GUEST_ES_LIMIT: Int](vmcs_guest_es_limit.md)
- [var VMCS_GUEST_CS_LIMIT: Int](vmcs_guest_cs_limit.md)
- [var VMCS_GUEST_SS_LIMIT: Int](vmcs_guest_ss_limit.md)
- [var VMCS_GUEST_DS_LIMIT: Int](vmcs_guest_ds_limit.md)
- [var VMCS_GUEST_FS_LIMIT: Int](vmcs_guest_fs_limit.md)
- [var VMCS_GUEST_GS_LIMIT: Int](vmcs_guest_gs_limit.md)
- [var VMCS_GUEST_LDTR_LIMIT: Int](vmcs_guest_ldtr_limit.md)
- [var VMCS_GUEST_TR_LIMIT: Int](vmcs_guest_tr_limit.md)
- [var VMCS_GUEST_GDTR_LIMIT: Int](vmcs_guest_gdtr_limit.md)
- [var VMCS_GUEST_IDTR_LIMIT: Int](vmcs_guest_idtr_limit.md)
- [var VMCS_GUEST_ES_AR: Int](vmcs_guest_es_ar.md)
- [var VMCS_GUEST_CS_AR: Int](vmcs_guest_cs_ar.md)
- [var VMCS_GUEST_SS_AR: Int](vmcs_guest_ss_ar.md)
- [var VMCS_GUEST_DS_AR: Int](vmcs_guest_ds_ar.md)
- [var VMCS_GUEST_FS_AR: Int](vmcs_guest_fs_ar.md)
- [var VMCS_GUEST_GS_AR: Int](vmcs_guest_gs_ar.md)
- [var VMCS_GUEST_LDTR_AR: Int](vmcs_guest_ldtr_ar.md)
- [var VMCS_GUEST_TR_AR: Int](vmcs_guest_tr_ar.md)
- [var VMCS_GUEST_INTERRUPTIBILITY: Int](vmcs_guest_interruptibility.md)
- [var VMCS_GUEST_IGNORE_IRQ: Int](vmcs_guest_ignore_irq.md)
- [var VMCS_GUEST_ACTIVITY_STATE: Int](vmcs_guest_activity_state.md)
- [var VMCS_GUEST_SMBASE: Int](vmcs_guest_smbase.md)
- [var VMCS_GUEST_IA32_SYSENTER_CS: Int](vmcs_guest_ia32_sysenter_cs.md)
- [var VMCS_GUEST_VMX_TIMER_VALUE: Int](vmcs_guest_vmx_timer_value.md)
- [var VMCS_HOST_IA32_SYSENTER_CS: Int](vmcs_host_ia32_sysenter_cs.md)
- [var VMCS_CTRL_CR0_MASK: Int](vmcs_ctrl_cr0_mask.md)
- [var VMCS_CTRL_CR4_MASK: Int](vmcs_ctrl_cr4_mask.md)
- [var VMCS_CTRL_CR0_SHADOW: Int](vmcs_ctrl_cr0_shadow.md)
- [var VMCS_CTRL_CR4_SHADOW: Int](vmcs_ctrl_cr4_shadow.md)
- [var VMCS_CTRL_CR3_VALUE0: Int](vmcs_ctrl_cr3_value0.md)
- [var VMCS_CTRL_CR3_VALUE1: Int](vmcs_ctrl_cr3_value1.md)
- [var VMCS_CTRL_CR3_VALUE2: Int](vmcs_ctrl_cr3_value2.md)
- [var VMCS_CTRL_CR3_VALUE3: Int](vmcs_ctrl_cr3_value3.md)
- [var VMCS_RO_EXIT_QUALIFIC: Int](vmcs_ro_exit_qualific.md)
- [var VMCS_RO_IO_RCX: Int](vmcs_ro_io_rcx.md)
- [var VMCS_RO_IO_RSI: Int](vmcs_ro_io_rsi.md)
- [var VMCS_RO_IO_RDI: Int](vmcs_ro_io_rdi.md)
- [var VMCS_RO_IO_RIP: Int](vmcs_ro_io_rip.md)
- [var VMCS_RO_GUEST_LIN_ADDR: Int](vmcs_ro_guest_lin_addr.md)
- [var VMCS_GUEST_CR0: Int](vmcs_guest_cr0.md)
- [var VMCS_GUEST_CR3: Int](vmcs_guest_cr3.md)
- [var VMCS_GUEST_CR4: Int](vmcs_guest_cr4.md)
- [var VMCS_GUEST_ES_BASE: Int](vmcs_guest_es_base.md)
- [var VMCS_GUEST_CS_BASE: Int](vmcs_guest_cs_base.md)
- [var VMCS_GUEST_SS_BASE: Int](vmcs_guest_ss_base.md)
- [var VMCS_GUEST_DS_BASE: Int](vmcs_guest_ds_base.md)
- [var VMCS_GUEST_FS_BASE: Int](vmcs_guest_fs_base.md)
- [var VMCS_GUEST_GS_BASE: Int](vmcs_guest_gs_base.md)
- [var VMCS_GUEST_IDTR_BASE: Int](vmcs_guest_idtr_base.md)
- [var VMCS_GUEST_TR_BASE: Int](vmcs_guest_tr_base.md)
- [var VMCS_GUEST_GDTR_BASE: Int](vmcs_guest_gdtr_base.md)
- [var VMCS_GUEST_LDTR_BASE: Int](vmcs_guest_ldtr_base.md)
- [var VMCS_GUEST_DR7: Int](vmcs_guest_dr7.md)
- [var VMCS_GUEST_RSP: Int](vmcs_guest_rsp.md)
- [var VMCS_GUEST_RIP: Int](vmcs_guest_rip.md)
- [var VMCS_GUEST_RFLAGS: Int](vmcs_guest_rflags.md)
- [var VMCS_GUEST_DEBUG_EXC: Int](vmcs_guest_debug_exc.md)
- [var VMCS_GUEST_SYSENTER_ESP: Int](vmcs_guest_sysenter_esp.md)
- [var VMCS_GUEST_SYSENTER_EIP: Int](vmcs_guest_sysenter_eip.md)
- [var VMCS_HOST_CR0: Int](vmcs_host_cr0.md)
- [var VMCS_HOST_CR3: Int](vmcs_host_cr3.md)
- [var VMCS_HOST_CR4: Int](vmcs_host_cr4.md)
- [var VMCS_HOST_FS_BASE: Int](vmcs_host_fs_base.md)
- [var VMCS_HOST_GS_BASE: Int](vmcs_host_gs_base.md)
- [var VMCS_HOST_TR_BASE: Int](vmcs_host_tr_base.md)
- [var VMCS_HOST_GDTR_BASE: Int](vmcs_host_gdtr_base.md)
- [var VMCS_HOST_IDTR_BASE: Int](vmcs_host_idtr_base.md)
- [var VMCS_HOST_IA32_SYSENTER_ESP: Int](vmcs_host_ia32_sysenter_esp.md)
- [var VMCS_HOST_IA32_SYSENTER_EIP: Int](vmcs_host_ia32_sysenter_eip.md)
- [var VMCS_HOST_RSP: Int](vmcs_host_rsp.md)
- [var VMCS_HOST_RIP: Int](vmcs_host_rip.md)
- [var VMCS_MAX: Int](vmcs_max.md)
### Interruptibility options
- [var GUEST_INTRBILITY_MOVSS_BLOCKING: UInt64](guest_intrbility_movss_blocking.md)
- [var GUEST_INTRBILITY_NMI_BLOCKING: UInt64](guest_intrbility_nmi_blocking.md)
- [var GUEST_INTRBILITY_SMI_BLOCKING: UInt64](guest_intrbility_smi_blocking.md)
- [var GUEST_INTRBILITY_STI_BLOCKING: UInt64](guest_intrbility_sti_blocking.md)
### Constants
- [var VMCS_INVALID: Int](vmcs_invalid.md)
- [var VMCS_CTRL_ENCLV_EXITING_BITMAP: Int](vmcs_ctrl_enclv_exiting_bitmap.md)
- [var VMCS_GUEST_IA32_INTR_SSP_TABLE_ADDR: Int](vmcs_guest_ia32_intr_ssp_table_addr.md)
- [var VMCS_GUEST_IA32_PKRS: Int](vmcs_guest_ia32_pkrs.md)
- [var VMCS_GUEST_IA32_S_CET: Int](vmcs_guest_ia32_s_cet.md)
- [var VMCS_GUEST_SSP: Int](vmcs_guest_ssp.md)
- [var VMCS_HOST_IA32_INTR_SSP_TABLE_ADDR: Int](vmcs_host_ia32_intr_ssp_table_addr.md)
- [var VMCS_HOST_IA32_PKRS: Int](vmcs_host_ia32_pkrs.md)
- [var VMCS_HOST_IA32_S_CET: Int](vmcs_host_ia32_s_cet.md)
- [var VMCS_HOST_SSP: Int](vmcs_host_ssp.md)

## See Also

- [Virtual Machine Control Structure (VMCS) Field IDs](virtual-machine-control-structure-vmcs-field-ids.md)
  Fields you can read or change using the Hypervisor framework’s read and write functions.
- [func hv_vmx_vcpu_read_vmcs(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_vcpu_read_vmcs(_:_:_:).md)
  Returns, by reference, the current value of a virtual machine control structure (VMCS) field of a vCPU.
- [func hv_vmx_vcpu_write_vmcs(hv_vcpuid_t, UInt32, UInt64) -> hv_return_t](hv_vmx_vcpu_write_vmcs(_:_:_:).md)
  Sets the value of a virtual machine control structure (VMCS) field of a vCPU.
- [func hv_vmx_vcpu_get_cap_write_vmcs(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt64>, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_vcpu_get_cap_write_vmcs(_:_:_:_:).md)
  Returns the allowed_0 and allowed_1 masks for a VMCS field of a vCPU.
- [func hv_vmx_vcpu_set_apic_address(hv_vcpuid_t, hv_gpaddr_t) -> hv_return_t](hv_vmx_vcpu_set_apic_address(_:_:).md)
  Sets the address of the guest Advanced Programmable Interrupt Controller (APIC) for a vCPU in the guest physical address space of the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/1469436-virtual_machine_control_structur-enum)*