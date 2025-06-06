# hv_vmx_vcpu_set_apic_address(_:_:)

**Framework**: Hypervisor  
**Kind**: func

Sets the address of the guest Advanced Programmable Interrupt Controller (APIC) for a vCPU in the guest physical address space of the VM.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func hv_vmx_vcpu_set_apic_address(_ vcpu: hv_vcpuid_t, _ gpa: hv_gpaddr_t) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

> ❗ **Important**:  This function must be called by the owning thread.

 This function must be called by the owning thread.

## Parameters

- `vcpu`: The ID of the vCPU.
- `gpa`: The address in the guest physical address space. It must be page-aligned.

## See Also

- [Virtual Machine Control Structure (VMCS) Field IDs](virtual-machine-control-structure-vmcs-field-ids.md)
  Fields you can read or change using the Hypervisor framework’s read and write functions.
- [func hv_vmx_vcpu_read_vmcs(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_vcpu_read_vmcs(_:_:_:).md)
  Returns, by reference, the current value of a virtual machine control structure (VMCS) field of a vCPU.
- [func hv_vmx_vcpu_write_vmcs(hv_vcpuid_t, UInt32, UInt64) -> hv_return_t](hv_vmx_vcpu_write_vmcs(_:_:_:).md)
  Sets the value of a virtual machine control structure (VMCS) field of a vCPU.
- [func hv_vmx_vcpu_get_cap_write_vmcs(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt64>, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_vcpu_get_cap_write_vmcs(_:_:_:_:).md)
  Returns the allowed_0 and allowed_1 masks for a VMCS field of a vCPU.
- [Virtual Machine control structure (VMCS) Field IDs](1469436-virtual_machine_control_structur-enum.md)
  Identify the fields of the virtual machine control structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vmx_vcpu_set_apic_address(_:_:))*