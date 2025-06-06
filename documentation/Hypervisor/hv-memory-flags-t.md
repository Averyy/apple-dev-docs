# hv_memory_flags_t

**Framework**: Hypervisor  
**Kind**: typealias

The permissions for guest physical memory regions.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_memory_flags_t = UInt64
```

#### Discussion

Set with the [`hv_vm_map(_:_:_:_:)`](hv_vm_map(_:_:_:_:).md) and [`hv_vm_protect(_:_:_:)`](hv_vm_protect(_:_:_:).md) functions.

## Topics

### Permissions
- [var HV_MEMORY_READ: Int](hv_memory_read.md)
  The value that represents the memory-read permission.
- [var HV_MEMORY_WRITE: Int](hv_memory_write.md)
  The value that represents the memory-write permission.
- [var HV_MEMORY_EXEC: Int](hv_memory_exec.md)
  The value that represents the memory-execute permission.

## See Also

- [typealias hv_allocate_flags_t](hv_allocate_flags_t.md)
- [typealias hv_gpaddr_t](hv_gpaddr_t.md)
  The type of a guest physical address (GPA).
- [typealias hv_sme_zt0_uchar64_t](hv_sme_zt0_uchar64_t.md)
- [typealias hv_uvaddr_t](hv_uvaddr_t.md)
  The type of a user virtual address.
- [typealias hv_vm_space_t](hv_vm_space_t.md)
  The type of a guest-address space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_memory_flags_t)*