# Virtual Machine Control Structure (VMCS) Field IDs

**Framework**: Hypervisor

Fields you can read or change using the Hypervisor framework’s read and write functions.

#### Overview

You can examine the state of, or control the operation of the framework and indivudal guests through various fields in the Virtual Machine Control Structure. The VMCS fields listed below describe which fields are read-only or read-write using the Hypervisor framework’s read and write functions.

##### Readable and Writable Vmcs Guest Fields

These are fields, states, flags, and registers in hypervisor guests that you can read from or write to. In some instances there are limitations on what you can read or write, such as specific regsters or bit positions as indicated for each field.

- `RIP`, `RSP`, `RFLAGS`
- `CR3`, `CR4`, `DR7`
- `PDTR` — {`0`, `1`, `2`, `3`}
- `CR3`-Target — {`0`, `1`, `2`, `3`}
- `IA32_SYSENTER_CS`
- `IA32_SYSENTER_ESP`
- `IA32_SYSENTER_EIP`
- `IA32_EFER`
- Interruptibility State
- Pending Debug Exceptions
- Selector — {`ES`, `CS`, `SS`, `DS`, `FS`, `GS`, `LDTR`, `TR`}
- Base — {`ES`, `CS`, `SS`, `DS`, `FS`, `GS`, `LDTR`, `TR`, `GDTR`, `ITDR`}
- Limit — {`ES`, `CS`, `SS`, `DS`, `FS`, `GS`, `LDTR`, `TR`, `GDTR`, `ITDR`}
- Access Rights — {`ES`, `CS`, `SS`, `FS`, `GS`, `LDTR`, `TR`}.

##### Readable and Writable Vmcs Control Fields

These control fields that you can both read and write.

- Exception Bitmap
- Framework
- Hypervisor
- Page-Fault Error-Code Mask
- VM-Entry Interruption-Information Field
- VM-Entry Exception Error Code
- VM-Entry Instruction Length
- TPR Threshold
- PLE Gap
- PLE Window
- `CR0` Guest/Host Mask
- `CR4` Guest/Host Mask
- `CR0` Read Shadow
- `CR4` Read Shadow

##### Readable and Conditionally Writable Vmcs Guest Fields

These guest fields describe the guest’s control registers and activity state. Updating these field requires the conditions listed for each field:

- `CR0` — `CR0.CD` and `CR0.NW` are unset
- Activity State — The current state must be either `ACTIVE` or `HLT`

##### Readable and Conditionally Writable Vmcs Control Fields

These fields describe VM execution controls, and access to the framework’s guest/host mask. Reading or updating these field requires the conditions listed for each field:

- Pin-Based VM-Execution Controls — [`hv_vmx_read_capability(_:_:)`](hv_vmx_read_capability(_:_:).md) must be `true`
- Primary Processor-Based VM-Execution Controls — [`hv_vmx_read_capability(_:_:)`](hv_vmx_read_capability(_:_:).md) must be `true`
- Secondary Processor-Based VM-Execution Controls — [`hv_vmx_read_capability(_:_:)`](hv_vmx_read_capability(_:_:).md) must be `true`
- VM Entry Controls — [`hv_vmx_read_capability(_:_:)`](hv_vmx_read_capability(_:_:).md) must be `true`
- `CR0` Guest/Host Mask — `CR0.CD` and `CR0.NW` are set

##### Read Only Vmcs Control Fields

These read-only fields provide information about time-stamp counter offsets and programmable interrupt controllers addresses:

- TCS Offset
- APIC-Access Address

##### Read Only Vmcs Data Fields

These read-only fields describe error and exit information, interrupt descriptor tables, or guest address information:

- VM-Instruction Error
- Exit Reason
- VM-Exit Interruption Information
- VM-Exit Interruption Error Code
- IDT-Vectoring Information Field
- IDT-Vectoring Error Code
- VM-Exit Instruction Length
- VM-Exit Instruction Information
- Guest-Physical Address
- Exit Qualification
- Guest-Linear Address

## Topics

### Enumerations
- [VM Creation Options](1447306-vm-creation-options.md)
  Constants that describe the creation options for a virtual machine.
- [VM Capabilities](3181560-vm-capabilities.md)
  An enumeration that describes the capabilities of the system.
- [struct hv_cache_type_t](hv_cache_type_t.md)
  The structure that describes an instruction or data cache element.
- [enum hv_boot_state](hv_boot_state.md)
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
- [struct hv_vm_exitinfo_t](hv_vm_exitinfo_t.md)

## See Also

- [func hv_vmx_vcpu_read_vmcs(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_vcpu_read_vmcs(_:_:_:).md)
  Returns, by reference, the current value of a virtual machine control structure (VMCS) field of a vCPU.
- [func hv_vmx_vcpu_write_vmcs(hv_vcpuid_t, UInt32, UInt64) -> hv_return_t](hv_vmx_vcpu_write_vmcs(_:_:_:).md)
  Sets the value of a virtual machine control structure (VMCS) field of a vCPU.
- [func hv_vmx_vcpu_get_cap_write_vmcs(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt64>, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_vcpu_get_cap_write_vmcs(_:_:_:_:).md)
  Returns the allowed_0 and allowed_1 masks for a VMCS field of a vCPU.
- [func hv_vmx_vcpu_set_apic_address(hv_vcpuid_t, hv_gpaddr_t) -> hv_return_t](hv_vmx_vcpu_set_apic_address(_:_:).md)
  Sets the address of the guest Advanced Programmable Interrupt Controller (APIC) for a vCPU in the guest physical address space of the VM.
- [Virtual Machine control structure (VMCS) Field IDs](1469436-virtual_machine_control_structur-enum.md)
  Identify the fields of the virtual machine control structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/virtual-machine-control-structure-vmcs-field-ids)*