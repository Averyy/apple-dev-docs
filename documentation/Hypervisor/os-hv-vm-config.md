# OS_hv_vm_config

**Framework**: Hypervisor  
**Kind**: protocol

Creates a virtual machine configuration object.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol OS_hv_vm_config : NSObjectProtocol
```

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func hv_vm_config_create() -> hv_vm_config_t](hv_vm_config_create().md)
  Creates a virtual machine configuration object.
- [func hv_vm_create(hv_vm_options_t) -> hv_return_t](hv_vm_create(_:).md)
  Creates a VM instance for the current process.
- [func hv_vm_destroy() -> hv_return_t](hv_vm_destroy().md)
  Destroys the VM instance associated with the current process.
- [typealias hv_vm_config_t](hv_vm_config_t.md)
  The type that defines a virtual-machine configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/os_hv_vm_config)*