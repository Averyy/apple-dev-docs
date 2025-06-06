# hv_vm_map(_:_:_:_:)

**Framework**: Hypervisor  
**Kind**: func

Maps a region in the virtual address space of the current process into the guest physical address space of the VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vm_map(_ addr: UnsafeMutableRawPointer, _ ipa: hv_ipa_t, _ size: Int, _ flags: hv_memory_flags_t) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

The host memory must encompass a single VM region, typically allocated with `mmap` or [`mach_vm_allocate`](https://developer.apple.com/documentation/kernel/1402376-mach_vm_allocate) instead of `malloc`.

Intel-based Mac computers have different parameters:

## Parameters

- `addr`: Apple silicon only.
- `ipa`: Apple silicon only.
- `size`: The size of the mapped region in bytes. It must be a multiple of the page size.
- `flags`: The permissions for the mapped region. For a list of valid options, see  .

## See Also

- [func hv_vm_unmap(hv_ipa_t, Int) -> hv_return_t](hv_vm_unmap(_:_:).md)
  Unmaps a region in the guest physical address space of the VM.
- [func hv_vm_protect(hv_ipa_t, Int, hv_memory_flags_t) -> hv_return_t](hv_vm_protect(_:_:_:).md)
  Modifies the permissions of a region in the guest physical address space of the VM.
- [typealias hv_ipa_t](hv_ipa_t.md)
  The type of an intermediate physical address, which is a guest physical address space of the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_map(_:_:_:_:))*