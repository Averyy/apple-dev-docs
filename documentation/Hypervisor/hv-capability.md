# hv_capability(_:_:)

**Framework**: Hypervisor  
**Kind**: func

Gets the value of capabilities of the system.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func hv_capability(_ capability: hv_capability_t, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

Intel-based Mac only.

## Parameters

- `capability`: The capability to request.
- `value`: The value for  , on output.

## See Also

- [func hv_vm_create(hv_vm_config_t?) -> hv_return_t](hv_vm_create(_:).md)
  Creates a VM instance for the current process.
- [func hv_vm_destroy() -> hv_return_t](hv_vm_destroy().md)
  Destroys the VM instance associated with the current process.
- [typealias hv_vm_options_t](hv_vm_options_t.md)
  Options you use when creating a virtual machine.
- [typealias hv_capability_t](hv_capability_t.md)
  The type of system capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_capability(_:_:))*