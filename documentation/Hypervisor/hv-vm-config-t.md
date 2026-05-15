# hv_vm_config_t

**Framework**: Hypervisor  
**Kind**: typealias

The type that defines a virtual-machine configuration.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_vm_config_t = any OS_hv_vm_config
```

## See Also

- [func hv_vm_config_create() -> hv_vm_config_t](hv_vm_config_create().md)
  Creates a virtual machine configuration object.
- [func hv_vm_create(hv_vm_config_t?) -> hv_return_t](hv_vm_create(_:).md)
  Creates a VM instance for the current process.
- [func hv_vm_destroy() -> hv_return_t](hv_vm_destroy().md)
  Destroys the VM instance associated with the current process.
- [protocol OS_hv_vm_config](os_hv_vm_config.md)
  Creates a virtual machine configuration object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_config_t)*