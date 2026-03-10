# Apple Silicon

**Framework**: Hypervisor

Create and run virtual machines on Apple silicon.

## Topics

### Virtual machine management
- [func hv_vm_config_create() -> hv_vm_config_t](hv_vm_config_create().md)
  Creates a virtual machine configuration object.
- [func hv_vm_create(hv_vm_config_t?) -> hv_return_t](hv_vm_create(_:).md)
  Creates a VM instance for the current process.
- [func hv_vm_destroy() -> hv_return_t](hv_vm_destroy().md)
  Destroys the VM instance associated with the current process.
- [protocol OS_hv_vm_config](os_hv_vm_config.md)
  Creates a virtual machine configuration object.
- [typealias hv_vm_config_t](hv_vm_config_t.md)
  The type that defines a virtual-machine configuration.
### Resource management
- [vCPU Management](vcpu-management.md)
  Create and run virtual CPUs, and manage CPU-specific registers and features.
- [Memory management](memory-management.md)
  Map memory into the physical address space of the virtual machine.
### Timer functions
- [func hv_vcpu_get_vtimer_mask(hv_vcpu_t, UnsafeMutablePointer<Bool>) -> hv_return_t](hv_vcpu_get_vtimer_mask(_:_:).md)
  Gets the virtual timer mask.
- [func hv_vcpu_set_vtimer_mask(hv_vcpu_t, Bool) -> hv_return_t](hv_vcpu_set_vtimer_mask(_:_:).md)
  Sets or clears the virtual timer mask.
- [func hv_vcpu_get_vtimer_offset(hv_vcpu_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_get_vtimer_offset(_:_:).md)
  Returns the vTimer offset for the vCPU ID you specify.
- [func hv_vcpu_set_vtimer_offset(hv_vcpu_t, UInt64) -> hv_return_t](hv_vcpu_set_vtimer_offset(_:_:).md)
  Sets the vTimer offset to a value that you provide.
### Common data types
- [typealias hv_return_t](hv_return_t.md)
  The return type of framework functions.
- [Hypervisor Errors](hypervisor-errors.md)
  Return codes returned by framework functions.
### Nested virtualization
- [func hv_vm_config_get_el2_supported(UnsafeMutablePointer<Bool>) -> hv_return_t](hv_vm_config_get_el2_supported(_:).md)
  Returns a status value that indicates whether the current platform supports Exception Level 2 (EL2).
- [func hv_vm_config_get_el2_enabled(hv_vm_config_t, UnsafeMutablePointer<Bool>) -> hv_return_t](hv_vm_config_get_el2_enabled(_:_:).md)
  Return a status value that indicates whether the VM configuration enables support for Exception Level 2 (EL2).
- [func hv_vm_config_set_el2_enabled(hv_vm_config_t, Bool) -> hv_return_t](hv_vm_config_set_el2_enabled(_:_:).md)
  Sets whether the specified VM configuration enables support for Exception Level 2 (EL2).
### Generic interrupt controllers (GICs)
- [GIC functions](gic-functions.md)
  These functions and registers support the creation and operation of a generic interrupt controller.
- [GIC registers](gic-registers.md)
  These registers support the operation of a generic interrupt controller and its interface with the Hypervisor and virtual CPUs.

## See Also

- [Intel-based Mac](intel-based-mac.md)
  Create and run virtual machines on Intel-based Mac computers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/apple-silicon)*