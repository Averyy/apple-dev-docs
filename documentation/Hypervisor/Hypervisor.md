# Hypervisor

**Framework**: Hypervisor  
**Kind**: module

Build virtualization solutions on top of a lightweight hypervisor, without third-party kernel extensions.

**Availability**:
- macOS 10.10+

#### Overview

Hypervisor provides C APIs so you can interact with virtualization technologies in user space, without writing kernel extensions (KEXTs). As a result, the apps you create using this framework are suitable for distribution on the [`Mac App Store`](https://developer.apple.comhttps://www.appstore.com/).

Use this framework to create and control hardware-facilitated virtual machines and virtual processors (VMs and vCPUs) from your entitled, sandboxed, user-space process. Hypervisor abstracts virtual machines as processes, and virtual processors as threads.

##### Requirements

The Hypervisor framework has the following requirements:

- **Supported hardware**: The Hypervisor framework requires hardware support to virtualize hardware resources. On Apple silicon, that includes the Virtualization Extensions. On Intel-based Mac computers, the framework supports machines with an Intel VT-x feature set that includes Extended Page Tables (EPT) and Unrestricted Mode.

At runtime, determine whether the Hypervisor APIs are available on a particular machine with the sysctl command, passing `kern.hv_support` as an argument.

- **Entitlements**: All process must have the [`com.apple.security.hypervisor`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hypervisor) entitlement to use Hypervisor API.

##### Virtual Resource Mapping

A guest is an operating system that runs on top of the virtual hardware. The operating system and processes that run the virtualized hardware are together called the host. Virtual hardware in the guest maps to specific resources on the host.

Each virtual machine corresponds to a process on the host. There can only be one virtual machine at a time per process; the virtual machine creates it with [`hv_vm_create(_:)`](hv_vm_create(_:).md).

Virtual CPUs (vCPUs) in a virtual machine map to POSIX threads. Create a new vCPU for the current thread with [`hv_vcpu_create(_:_:_:)`](hv_vcpu_create(_:_:_:).md). The vCPU runs when the thread calls [`hv_vcpu_run(_:)`](hv_vcpu_run(_:).md).

Hypervisor maps the physical memory in the guest to virtual memory of the host process. Create a new memory mapping with [`hv_vm_map(_:_:_:_:)`](hv_vm_map(_:_:_:_:).md). Access to memory outside the mapped range causes [`hv_vcpu_run(_:)`](hv_vcpu_run(_:).md) to exit. Emulate memory-mapped hardware by emulating the memory access on exit and re-enter the guest with [`hv_vcpu_run(_:)`](hv_vcpu_run(_:).md).

##### Example Vm Life Cycle

The following figure illustrates a simplified life cycle of creating and running a virtual machine with one or more virtual CPUs using the Hypervisor API.

![A flow diagram that represents the life cycle of a virtual machine.](/images/com.apple.hypervisor/media-2916425@2x.png)

At the start of a task:

- Create a VM with [`hv_vm_create(_:)`](hv_vm_create(_:).md).
- Map a region in the virtual address space of the current task into the guest physical address space of the VM with [`hv_vm_map(_:_:_:_:)`](hv_vm_map(_:_:_:_:).md).
- Create one or more POSIX threads with `pthread_create(_:_:_:_:)`.

In each thread:

- Create a virtual CPU with [`hv_vcpu_create(_:_:_:)`](hv_vcpu_create(_:_:_:).md).
- Call [`hv_vcpu_run(_:)`](hv_vcpu_run(_:).md) to run the vCPU.

When a thread receives an exit event:

- Handle the event.
- Re-enter the guest with [`hv_vcpu_run(_:)`](hv_vcpu_run(_:).md) or destroy the vCPU with [`hv_vcpu_destroy(_:)`](hv_vcpu_destroy(_:).md).

After all threads finish:

- Unmap the memory region with [`hv_vm_unmap(_:_:)`](hv_vm_unmap(_:_:).md).
- Destroy the VM with [`hv_vm_destroy()`](hv_vm_destroy().md).

## Topics

### Platforms
- [Apple Silicon](apple-silicon.md)
  Create and run virtual machines on Apple silicon.
- [Intel-based Mac](intel-based-mac.md)
  Create and run virtual machines on Intel-based Mac computers.
### Entitlements
- [com.apple.security.hypervisor](../bundleresources/entitlements/com.apple.security.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.hypervisor](../bundleresources/entitlements/com.apple.vm.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.networking](../bundleresources/entitlements/com.apple.vm.networking.md)
  A Boolean that indicates whether the app manages virtual network interfaces without escalating privileges to the root user.
- [com.apple.vm.device-access](../bundleresources/entitlements/com.apple.vm.device-access.md)
  A Boolean value that indicates whether the app captures USB devices and uses them in the guest-operating system.
### Reference
- [Hypervisor Structures](hypervisor-structures.md)
- [Hypervisor Constants](hypervisor-constants.md)
- [Hypervisor Functions](hypervisor-functions.md)
- [Hypervisor Data Types](hypervisor-data-types.md)
### Structures
- [struct hv_ipa_granule_t](hv_ipa_granule_t.md)
- [struct hv_tlbi_op_t](hv_tlbi_op_t.md)
### Variables
- [var HV_FEATURE_REG_ID_AA64ISAR2_EL1: hv_feature_reg_t](hv_feature_reg_id_aa64isar2_el1.md)
- [var HV_FEATURE_REG_ID_AA64MMFR3_EL1: hv_feature_reg_t](hv_feature_reg_id_aa64mmfr3_el1.md)
- [var HV_FEATURE_REG_ID_AA64MMFR4_EL1: hv_feature_reg_t](hv_feature_reg_id_aa64mmfr4_el1.md)
- [var HV_FEATURE_REG_ID_AA64PFR2_EL1: hv_feature_reg_t](hv_feature_reg_id_aa64pfr2_el1.md)
- [var HV_IPA_GRANULE_16KB: hv_ipa_granule_t](hv_ipa_granule_16kb.md)
- [var HV_IPA_GRANULE_4KB: hv_ipa_granule_t](hv_ipa_granule_4kb.md)
- [var HV_SYS_REG_ID_AA64ISAR2_EL1: hv_sys_reg_t](hv_sys_reg_id_aa64isar2_el1.md)
- [var HV_SYS_REG_ID_AA64MMFR3_EL1: hv_sys_reg_t](hv_sys_reg_id_aa64mmfr3_el1.md)
- [var HV_SYS_REG_ID_AA64MMFR4_EL1: hv_sys_reg_t](hv_sys_reg_id_aa64mmfr4_el1.md)
- [var HV_SYS_REG_ID_AA64PFR2_EL1: hv_sys_reg_t](hv_sys_reg_id_aa64pfr2_el1.md)
- [var HV_TLBI_OP_ASIDE1IS: hv_tlbi_op_t](hv_tlbi_op_aside1is.md)
- [var HV_TLBI_OP_RVAAE1IS: hv_tlbi_op_t](hv_tlbi_op_rvaae1is.md)
- [var HV_TLBI_OP_RVAALE1IS: hv_tlbi_op_t](hv_tlbi_op_rvaale1is.md)
- [var HV_TLBI_OP_RVAE1IS: hv_tlbi_op_t](hv_tlbi_op_rvae1is.md)
- [var HV_TLBI_OP_RVALE1IS: hv_tlbi_op_t](hv_tlbi_op_rvale1is.md)
- [var HV_TLBI_OP_VAAE1IS: hv_tlbi_op_t](hv_tlbi_op_vaae1is.md)
- [var HV_TLBI_OP_VAALE1IS: hv_tlbi_op_t](hv_tlbi_op_vaale1is.md)
- [var HV_TLBI_OP_VAE1IS: hv_tlbi_op_t](hv_tlbi_op_vae1is.md)
- [var HV_TLBI_OP_VALE1IS: hv_tlbi_op_t](hv_tlbi_op_vale1is.md)
- [var HV_TLBI_OP_VMALLE1IS: hv_tlbi_op_t](hv_tlbi_op_vmalle1is.md)
### Functions
- [func hv_vcpu_get_serror(hv_vcpu_t, UnsafeMutablePointer<Bool>) -> hv_return_t](hv_vcpu_get_serror(_:_:).md)
- [func hv_vcpu_get_wait_for_interrupt_time(hv_vcpu_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_get_wait_for_interrupt_time(_:_:).md)
- [func hv_vcpu_invalidate_tlb(hv_vcpu_t, hv_tlbi_op_t, UInt64) -> hv_return_t](hv_vcpu_invalidate_tlb(_:_:_:).md)
- [func hv_vcpu_set_serror(hv_vcpu_t, Bool) -> hv_return_t](hv_vcpu_set_serror(_:_:).md)
- [func hv_vm_config_get_default_ipa_granule(UnsafeMutablePointer<hv_ipa_granule_t>) -> hv_return_t](hv_vm_config_get_default_ipa_granule(_:).md)
- [func hv_vm_config_get_ipa_granule(hv_vm_config_t, UnsafeMutablePointer<hv_ipa_granule_t>) -> hv_return_t](hv_vm_config_get_ipa_granule(_:_:).md)
- [func hv_vm_config_set_ipa_granule(hv_vm_config_t, hv_ipa_granule_t) -> hv_return_t](hv_vm_config_set_ipa_granule(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Hypervisor)*