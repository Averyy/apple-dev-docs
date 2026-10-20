# hv_ipa_t

**Framework**: Hypervisor  
**Kind**: typealias  
**Role**: Type Alias

The type of an intermediate physical address, which is a guest physical address space of the VM.

**Availability**:
- macOS

## Declaration

```swift
typealias hv_ipa_t = UInt64
```

```c
typedef uint64_t hv_ipa_t;
```

## See Also

### Intermediate physical memory
- [func hv_vm_map(UnsafeMutableRawPointer, hv_ipa_t, Int, hv_memory_flags_t) -> hv_return_t](./hv_vm_map%28_,_,_,_%29.md)
  Maps a region in the virtual address space of the current process into the guest physical address space of the VM.
- [func hv_vm_unmap(hv_ipa_t, Int) -> hv_return_t](./hv_vm_unmap%28_,_%29.md)
  Unmaps a region in the guest physical address space of the VM.
- [func hv_vm_protect(hv_ipa_t, Int, hv_memory_flags_t) -> hv_return_t](./hv_vm_protect%28_,_,_%29.md)
  Modifies the permissions of a region in the guest physical address space of the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_ipa_t)*