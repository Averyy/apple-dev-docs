# hv_vm_config_set_el2_enabled(_:_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Sets whether the specified VM configuration enables support for Exception Level 2 (EL2).

**Availability**:
- macOS 15.0+

## Declaration

```swift
func hv_vm_config_set_el2_enabled(_ config: hv_vm_config_t, _ el2_enabled: Bool) -> hv_return_t
```

```c
extern hv_return_t hv_vm_config_set_el2_enabled(hv_vm_config_t config, bool el2_enabled);
```

## Return Value

[`HV_SUCCESS`](./hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](./hv_return_t.md).

## Parameters

- `config`: The VM’s configuration object
- `el2_enabled`: A Boolean value that indicates whether the specified configure enables EL2. The framework writes this value on success; otherwise `nil`.

## See Also

### Nested virtualization
- [func hv_vm_config_get_el2_supported(UnsafeMutablePointer<Bool>) -> hv_return_t](./hv_vm_config_get_el2_supported%28_%29.md)
  Returns a status value that indicates whether the current platform supports Exception Level 2 (EL2).
- [func hv_vm_config_get_el2_enabled(hv_vm_config_t, UnsafeMutablePointer<Bool>) -> hv_return_t](./hv_vm_config_get_el2_enabled%28_,_%29.md)
  Return a status value that indicates whether the VM configuration enables support for Exception Level 2 (EL2).


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_config_set_el2_enabled(_:_:))*