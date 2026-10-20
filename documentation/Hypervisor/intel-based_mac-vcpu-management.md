# vCPU Management

**Framework**: Hypervisor  
**Role**: API Collection

Create and run virtual CPUs, and manage CPU-specific registers and features.

## Topics

### Creation and destruction
- [func hv_vcpu_create(UnsafeMutablePointer<hv_vcpu_t>, UnsafeMutablePointer<UnsafeMutablePointer<hv_vcpu_exit_t>?>, hv_vcpu_config_t?) -> hv_return_t](./hv_vcpu_create%28_,_,_%29.md)
  Creates a vCPU instance for the current thread.
- [func hv_vcpu_destroy(hv_vcpu_t) -> hv_return_t](./hv_vcpu_destroy%28_%29.md)
  Destroys the vCPU instance associated with the current thread.
- [typealias hv_vcpu_options_t](./hv_vcpu_options_t.md)
  Options for creating a new vCPU instance.
- [vCPU Creation Behavior](./api-1447317-vcpu-creation-behavior.md)
  An enumeration representing the default creation options for virtual CPUs.
- [typealias hv_vcpuid_t](./hv_vcpuid_t.md)
  The type that describes a vCPU ID.
### Runtime
- [func hv_vcpu_run_until(hv_vcpuid_t, UInt64) -> hv_return_t](./hv_vcpu_run_until%28_,_%29.md)
  Executes a vCPU until it reaches the deadline defined in absolute time units you provide.
- [func hv_vcpu_interrupt(UnsafeMutablePointer<hv_vcpuid_t>, UInt32) -> hv_return_t](./hv_vcpu_interrupt%28_,_%29.md)
  Forces the vCPU instances you provide to immediately exit the VM.
- [func hv_vcpu_flush(hv_vcpuid_t) -> hv_return_t](./hv_vcpu_flush%28_%29.md)
  Flushes the cached state of a vCPU.
- [func hv_vcpu_get_exec_time(hv_vcpu_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](./hv_vcpu_get_exec_time%28_,_%29.md)
  Returns, by reference, the cumulative execution time of a vCPU, in nanoseconds.
- [func hv_vcpu_run(hv_vcpu_t) -> hv_return_t](./hv_vcpu_run%28_%29.md)
  Starts the execution of a vCPU.
- [Execution Deadlines](./api-3553338-execution-deadlines.md)
  An enumeration that describes available execution deadlines available to vCPUs.
### Synchronization
- [func hv_vm_sync_tsc(UInt64) -> hv_return_t](./hv_vm_sync_tsc%28_%29.md)
  Synchronizes guest timestamp counters (TSC) across all vCPUs.
### Model-Specific Registers
- [Extending vCPU Capabilities Using Model-Specific Registers](./extending-vcpu-capabilities-using-model-specific-registers.md)
  Configure specific client performance monitoring and enable other vCPU capabilities using Model-Specific Registers.
- [func hv_vcpu_read_msr(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt64>) -> hv_return_t](./hv_vcpu_read_msr%28_,_,_%29.md)
  Returns, by reference, the current value of a Model-Specific Register (MSR) of a vCPU.
- [func hv_vcpu_write_msr(hv_vcpuid_t, UInt32, UInt64) -> hv_return_t](./hv_vcpu_write_msr%28_,_,_%29.md)
  Sets the value of a Model-Specific Register (MSR) of a vCPU.
- [func hv_vcpu_enable_native_msr(hv_vcpuid_t, UInt32, Bool) -> hv_return_t](./hv_vcpu_enable_native_msr%28_,_,_%29.md)
  Enables or disables a Model-Specific Register (MSR) that the VM uses natively.
- [func hv_vcpu_set_msr_access(hv_vcpuid_t, UInt32, hv_msr_flags_t) -> hv_return_t](./hv_vcpu_set_msr_access%28_,_,_%29.md)
  Controls the guest access of a managed Model-Specific Register (MSR).
- [func hv_vcpu_enable_managed_msr(hv_vcpuid_t, UInt32, Bool) -> hv_return_t](./hv_vcpu_enable_managed_msr%28_,_,_%29.md)
  Enables the guest access of a managed Model-Specific Register (MSR).
- [typealias hv_msr_flags_t](./hv_msr_flags_t.md)
  The type representing the native Model-Specific Register (MSR) permissions.
- [Model-Specific Registers](./api-3727856-model-specific-registers.md)
- [MSR Permissions](./api-3567078-msr_permissions-enum.md)
  An enumeration that describes possible Model-Specific Register (MSR) permisssions.
### CPU Registers
- [func hv_vcpu_read_register(hv_vcpuid_t, hv_x86_reg_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](./hv_vcpu_read_register%28_,_,_%29.md)
  Returns, by reference, the current value of an architectural x86 register of a vCPU.
- [func hv_vcpu_write_register(hv_vcpuid_t, hv_x86_reg_t, UInt64) -> hv_return_t](./hv_vcpu_write_register%28_,_,_%29.md)
  Sets the value of an architectural x86 register of a vCPU.
- [struct hv_x86_reg_t](./hv_x86_reg_t.md)
  The type that defines x86 architectural registers.
### Floating Point (FP) State
- [func hv_vcpu_read_fpstate(hv_vcpuid_t, UnsafeMutableRawPointer, Int) -> hv_return_t](./hv_vcpu_read_fpstate%28_,_,_%29.md)
  Returns, by reference, the current architectural x86 floating point and SIMD state of a vCPU.
- [func hv_vcpu_write_fpstate(hv_vcpuid_t, UnsafeMutableRawPointer, Int) -> hv_return_t](./hv_vcpu_write_fpstate%28_,_,_%29.md)
  Sets the architectural x86 floating point and SIMD state of a vCPU.
### Memory Affinity
- [func hv_vcpu_set_space(hv_vcpuid_t, hv_vm_space_t) -> hv_return_t](./hv_vcpu_set_space%28_,_%29.md)
  Associates the vCPU instance with an allocated address space.

## See Also

### Resource management
- [Memory Management](./intel-based_mac-memory-management.md)
  Map memory into the physical address space of the virtual machine, and allocate additional memory for the current task.
- [Virtual Machine Control Structure (VMCS)](./virtual-machine-control-structure-vmcs.md)
  Read and write to fields of the virtual machine control structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/intel-based_mac-vcpu-management)*