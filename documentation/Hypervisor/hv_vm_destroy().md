# hv_vm_destroy()

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Destroys the VM instance associated with the current process.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vm_destroy() -> hv_return_t
```

```c
extern hv_return_t hv_vm_destroy();
```

#### Return Value

[`HV_SUCCESS`](./hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](./hv_return_t.md).

## See Also

### Virtual machine management
- [func hv_vm_config_create() -> hv_vm_config_t](./hv_vm_config_create%28%29.md)
  Creates a virtual machine configuration object.
- [func hv_vm_create(hv_vm_config_t?) -> hv_return_t](./hv_vm_create%28_%29.md)
  Creates a VM instance for the current process.
- [protocol OS_hv_vm_config](./os_hv_vm_config.md)
  Creates a virtual machine configuration object.
- [typealias hv_vm_config_t](./hv_vm_config_t.md)
  The type that defines a virtual-machine configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_destroy())*