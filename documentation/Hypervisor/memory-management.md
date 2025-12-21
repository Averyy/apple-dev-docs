# Memory management

**Framework**: Hypervisor

Map memory into the physical address space of the virtual machine.

#### Overview

Hypervisor virtualizes the memory seen by the guest as physical address space on top of the host’s address space.

The name for a physical address in the guest address space is an intermediate physical address or IPA in the host.

It’s possible to map memory regions in the host process into the intermediate physical address (IPA) with [`hv_vm_map(_:_:_:_:)`](hv_vm_map(_:_:_:_:).md).

Modify the guest’s access permissions over the entire region or subregions with [`hv_vm_protect(_:_:_:)`](hv_vm_protect(_:_:_:).md).

## Topics

### Intermediate physical memory
- [func hv_vm_map(hv_uvaddr_t, hv_gpaddr_t, Int, hv_memory_flags_t) -> hv_return_t](hv_vm_map(_:_:_:_:).md)
  Maps a region in the virtual address space of the current process into the guest physical address space of the VM.
- [func hv_vm_unmap(hv_gpaddr_t, Int) -> hv_return_t](hv_vm_unmap(_:_:).md)
  Unmaps a region in the guest physical address space of the VM.
- [func hv_vm_protect(hv_gpaddr_t, Int, hv_memory_flags_t) -> hv_return_t](hv_vm_protect(_:_:_:).md)
  Modifies the permissions of a region in the guest physical address space of the VM.
- [typealias hv_ipa_t](hv_ipa_t.md)
  The type of an intermediate physical address, which is a guest physical address space of the VM.

## See Also

- [vCPU Management](vcpu-management.md)
  Create and run virtual CPUs, and manage CPU-specific registers and features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/memory-management)*