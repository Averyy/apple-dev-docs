# hv_vm_config_create()

**Framework**: Hypervisor  
**Kind**: func

Creates a virtual machine configuration object.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func hv_vm_config_create() -> hv_vm_config_t
```

#### Return Value

A new virtual-machine configuration object. Release this object with `os_release` when no longer used.

## See Also

- [func hv_vm_create(hv_vm_options_t) -> hv_return_t](hv_vm_create(_:).md)
  Creates a VM instance for the current process.
- [func hv_vm_destroy() -> hv_return_t](hv_vm_destroy().md)
  Destroys the VM instance associated with the current process.
- [protocol OS_hv_vm_config](os_hv_vm_config.md)
  Creates a virtual machine configuration object.
- [typealias hv_vm_config_t](hv_vm_config_t.md)
  The type that defines a virtual-machine configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_config_create())*