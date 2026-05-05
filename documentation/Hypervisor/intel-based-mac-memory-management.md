# Memory Management

**Framework**: Hypervisor

Map memory into the physical address space of the virtual machine, and allocate additional memory for the current task.

## Topics

### Shared memory
- [func hv_vm_map(hv_uvaddr_t, hv_gpaddr_t, Int, hv_memory_flags_t) -> hv_return_t](hv_vm_map(_:_:_:_:).md)
  Maps a region in the virtual address space of the current process into the guest physical address space of the VM.
- [func hv_vm_unmap(hv_gpaddr_t, Int) -> hv_return_t](hv_vm_unmap(_:_:).md)
  Unmaps a region in the guest physical address space of the VM.
- [func hv_vm_protect(hv_gpaddr_t, Int, hv_memory_flags_t) -> hv_return_t](hv_vm_protect(_:_:_:).md)
  Modifies the permissions of a region in the guest physical address space of the VM.
### Process-specific memory
- [func hv_vm_space_create(UnsafeMutablePointer<hv_vm_space_t>) -> hv_return_t](hv_vm_space_create(_:).md)
  Creates an additional guest address space for the current task.
- [func hv_vm_space_destroy(hv_vm_space_t) -> hv_return_t](hv_vm_space_destroy(_:).md)
  Destroys the address space instance associated with the current task.
- [func hv_vm_map_space(hv_vm_space_t, hv_uvaddr_t, hv_gpaddr_t, Int, hv_memory_flags_t) -> hv_return_t](hv_vm_map_space(_:_:_:_:_:).md)
  Maps a region in the virtual address space of the current task into a guest physical address space of the VM.
- [func hv_vm_unmap_space(hv_vm_space_t, hv_gpaddr_t, Int) -> hv_return_t](hv_vm_unmap_space(_:_:_:).md)
  Umaps a region in a guest physical address space of the VM.
- [func hv_vm_protect_space(hv_vm_space_t, hv_gpaddr_t, Int, hv_memory_flags_t) -> hv_return_t](hv_vm_protect_space(_:_:_:_:).md)
  Modifies the permissions of a region in a guest physical address space of the VM.
### Common types
- [typealias hv_uvaddr_t](hv_uvaddr_t.md)
  The type of a user virtual address.
- [typealias hv_gpaddr_t](hv_gpaddr_t.md)
  The type of a guest physical address (GPA).
- [typealias hv_memory_flags_t](hv_memory_flags_t.md)
  The permissions for guest physical memory regions.
- [Memory Permissions](1447309-memory_permissions-enum.md)
  Enumeration values that describe memory permissions.
- [typealias hv_vm_space_t](hv_vm_space_t.md)
  The type of a guest-address space.
- [Address Space Types](3181561-address_space_type-enum.md)

## See Also

- [vCPU Management](intel-based_mac-vcpu-management.md)
  Create and run virtual CPUs, and manage CPU-specific registers and features.
- [Virtual Machine Control Structure (VMCS)](virtual-machine-control-structure-vmcs.md)
  Read and write to fields of the virtual machine control structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/intel-based_mac-memory-management)*