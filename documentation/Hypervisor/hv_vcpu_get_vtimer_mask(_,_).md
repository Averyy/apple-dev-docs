# hv_vcpu_get_vtimer_mask(_:_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Gets the virtual timer mask.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vcpu_get_vtimer_mask(_ vcpu: hv_vcpu_t, _ vtimer_is_masked: UnsafeMutablePointer<Bool>) -> hv_return_t
```

```c
extern hv_return_t hv_vcpu_get_vtimer_mask(hv_vcpu_t vcpu, bool *vtimer_is_masked);
```

#### Return Value

[`HV_SUCCESS`](./hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](./hv_return_t.md).

## Parameters

- `vcpu`: The ID of the vCPU instance.
- `vtimer_is_masked`: The value of the mask.

## See Also

### Timer functions
- [func hv_vcpu_set_vtimer_mask(hv_vcpu_t, Bool) -> hv_return_t](./hv_vcpu_set_vtimer_mask%28_,_%29.md)
  Sets or clears the virtual timer mask.
- [func hv_vcpu_get_vtimer_offset(hv_vcpu_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](./hv_vcpu_get_vtimer_offset%28_,_%29.md)
  Returns the vTimer offset for the vCPU ID you specify.
- [func hv_vcpu_set_vtimer_offset(hv_vcpu_t, UInt64) -> hv_return_t](./hv_vcpu_set_vtimer_offset%28_,_%29.md)
  Sets the vTimer offset to a value that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_get_vtimer_mask(_:_:))*