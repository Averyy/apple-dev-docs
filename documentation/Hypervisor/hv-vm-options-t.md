# hv_vm_options_t

**Framework**: Hypervisor  
**Kind**: typealias

Options you use when creating a virtual machine.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_vm_options_t = UInt64
```

## Topics

### Options
- [var HV_VM_DEFAULT: Int](hv_vm_default.md)
  The default VM creation behavior.

## See Also

- [func hv_vm_create(hv_vm_config_t?) -> hv_return_t](hv_vm_create(_:).md)
  Creates a VM instance for the current process.
- [func hv_vm_destroy() -> hv_return_t](hv_vm_destroy().md)
  Destroys the VM instance associated with the current process.
- [func hv_capability(hv_capability_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_capability(_:_:).md)
  Gets the value of capabilities of the system.
- [typealias hv_capability_t](hv_capability_t.md)
  The type of system capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_options_t)*