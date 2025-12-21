# hv_vm_create(_:)

**Framework**: Hypervisor  
**Kind**: func

Creates a VM instance for the current process.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func hv_vm_create(_ flags: hv_vm_options_t) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

Intel-based Mac computers have different parameters:

## See Also

- [func hv_vm_config_create() -> hv_vm_config_t](hv_vm_config_create().md)
  Creates a virtual machine configuration object.
- [func hv_vm_destroy() -> hv_return_t](hv_vm_destroy().md)
  Destroys the VM instance associated with the current process.
- [protocol OS_hv_vm_config](os_hv_vm_config.md)
  Creates a virtual machine configuration object.
- [typealias hv_vm_config_t](hv_vm_config_t.md)
  The type that defines a virtual-machine configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_create(_:))*