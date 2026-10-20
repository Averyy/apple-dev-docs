# hv_capability_t

**Framework**: Hypervisor  
**Kind**: typealias  
**Role**: Type Alias

The type of system capabilities.

**Availability**:
- macOS

## Declaration

```swift
typealias hv_capability_t = UInt64
```

```c
typedef uint64_t hv_capability_t;
```

## Topics

### Capabilities
- [var HV_CAP_VCPUMAX: Int](./hv_cap_vcpumax.md)
  A value that indicates the maximum number of available vCPUs.
- [var HV_CAP_ADDRSPACEMAX: Int](./hv_cap_addrspacemax.md)
  A value that indicates the maximum number of available address spaces.

## See Also

### Virtual machine management
- [func hv_vm_create(hv_vm_config_t?) -> hv_return_t](./hv_vm_create%28_%29.md)
  Creates a VM instance for the current process.
- [func hv_vm_destroy() -> hv_return_t](./hv_vm_destroy%28%29.md)
  Destroys the VM instance associated with the current process.
- [func hv_capability(hv_capability_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](./hv_capability%28_,_%29.md)
  Gets the value of capabilities of the system.
- [typealias hv_vm_options_t](./hv_vm_options_t.md)
  Options you use when creating a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_capability_t)*