# Virtual Machine Control Structure (VMCS)

**Framework**: Hypervisor

Read and write to fields of the virtual machine control structure.

## Topics

### Capabilities
- [func hv_vmx_read_capability(hv_vmx_capability_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_read_capability(_:_:).md)
  Returns, by reference, the VMX virtualization capabilities of the host processor.
- [func hv_vmx_get_msr_info(hv_vmx_msr_info_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_get_msr_info(_:_:).md)
  Returns information about guest MSR configuration.
- [struct hv_vmx_capability_t](hv_vmx_capability_t.md)
  The type that describes Virtual Machine Extensions (VMX) capability fields.
- [VMX Capabilities](1469645-vmx-capabilities.md)
  An enumeration that represents the available VMX capabilities.
- [typealias hv_vmx_msr_info_t](hv_vmx_msr_info_t.md)
  The type that describes Move to Status Register (MSR) information fields.
- [MSR Information Fields](3567084-msr-information-fields.md)
  The type that describes Machine Specific Register (MSR) fields.
### Field management
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
- [Virtual Machine control structure (VMCS) Field IDs](1469436-virtual_machine_control_structur-enum.md)
  Identify the fields of the virtual machine control structure.
### Shadow fields
- [func hv_vmx_vcpu_read_shadow_vmcs(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_vcpu_read_shadow_vmcs(_:_:_:).md)
  Returns the current value of a shadow VMCS field of a vCPU.
- [func hv_vmx_vcpu_set_shadow_access(hv_vcpuid_t, UInt32, hv_shadow_flags_t) -> hv_return_t](hv_vmx_vcpu_set_shadow_access(_:_:_:).md)
  Set the access permissions of a shadow VMCS field of a vCPU.
- [func hv_vmx_vcpu_write_shadow_vmcs(hv_vcpuid_t, UInt32, UInt64) -> hv_return_t](hv_vmx_vcpu_write_shadow_vmcs(_:_:_:).md)
  Set the value of a shadow VMCS field of a vCPU.
- [typealias hv_shadow_flags_t](hv_shadow_flags_t.md)
  Shadow VMCS permissions for the set shadow access function.
- [Shadow Permissions](3567083-shadow_permissions-enum.md)
  Permissions that define access to the shadow VMCS fields.
### Shared types
- [VMX Creation Behavior](1469509-vmx_creation_behavior-enum.md)
  An enumeration that describes VMX creation behavior options.
- [VMX Exit Reasons](1469470-vmx-exit-reasons.md)
  An enumertion that describes the VMX exit reasons.
- [Interrupt request (IRQ) codes](1469442-interrupt_request_irq_codes-enum.md)
  An enumeration that describes available interrupt codes.

## See Also

- [vCPU Management](intel-based_mac-vcpu-management.md)
  Create and run virtual CPUs, and manage CPU-specific registers and features.
- [Memory Management](intel-based_mac-memory-management.md)
  Map memory into the physical address space of the virtual machine, and allocate additional memory for the current task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/virtual-machine-control-structure-vmcs)*