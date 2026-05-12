# hv_ipa_t

**Framework**: Hypervisor  
**Kind**: typealias

The type of an intermediate physical address, which is a guest physical address space of the VM.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_ipa_t = UInt64
```

## See Also

- [func hv_vm_map(hv_uvaddr_t, hv_gpaddr_t, Int, hv_memory_flags_t) -> hv_return_t](hv_vm_map(_:_:_:_:).md)
  Maps a region in the virtual address space of the current process into the guest physical address space of the VM.
- [func hv_vm_unmap(hv_gpaddr_t, Int) -> hv_return_t](hv_vm_unmap(_:_:).md)
  Unmaps a region in the guest physical address space of the VM.
- [func hv_vm_protect(hv_gpaddr_t, Int, hv_memory_flags_t) -> hv_return_t](hv_vm_protect(_:_:_:).md)
  Modifies the permissions of a region in the guest physical address space of the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_ipa_t)*