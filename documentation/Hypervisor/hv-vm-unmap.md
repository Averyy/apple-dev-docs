# hv_vm_unmap(_:_:)

**Framework**: Hypervisor  
**Kind**: func

Unmaps a region in the guest physical address space of the VM.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func hv_vm_unmap(_ gpa: hv_gpaddr_t, _ size: Int) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

Intel-based Mac computers have different parameters:

## Parameters

- `size`: The size of the region to unmap, in bytes. It must be a multiple of the page size.

## See Also

- [func hv_vm_map(hv_uvaddr_t, hv_gpaddr_t, Int, hv_memory_flags_t) -> hv_return_t](hv_vm_map(_:_:_:_:).md)
  Maps a region in the virtual address space of the current process into the guest physical address space of the VM.
- [func hv_vm_protect(hv_gpaddr_t, Int, hv_memory_flags_t) -> hv_return_t](hv_vm_protect(_:_:_:).md)
  Modifies the permissions of a region in the guest physical address space of the VM.
- [typealias hv_ipa_t](hv_ipa_t.md)
  The type of an intermediate physical address, which is a guest physical address space of the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_unmap(_:_:))*