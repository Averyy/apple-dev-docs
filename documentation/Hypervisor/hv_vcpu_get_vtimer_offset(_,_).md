# hv_vcpu_get_vtimer_offset(_:_:)

**Framework**: Hypervisor  
**Kind**: func

Returns the vTimer offset for the vCPU ID you specify.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vcpu_get_vtimer_offset(_ vcpu: hv_vcpu_t, _ vtimer_offset: UnsafeMutablePointer<UInt64>) -> hv_return_t
```

#### Return Value

`0` on success, or an error code of the type [`hv_return_t`](hv_return_t.md).

#### Discussion

This corresponds to the value of the `CNTVOFF_EL2` register.

## Parameters

- `vcpu`: The ID of the vCPU instance.
- `vtimer_offset`: A pointer to vTimer offset; the Hypervisor writes to this value on success.

## See Also

- [func hv_vcpu_get_vtimer_mask(hv_vcpu_t, UnsafeMutablePointer<Bool>) -> hv_return_t](hv_vcpu_get_vtimer_mask(_:_:).md)
  Gets the virtual timer mask.
- [func hv_vcpu_set_vtimer_mask(hv_vcpu_t, Bool) -> hv_return_t](hv_vcpu_set_vtimer_mask(_:_:).md)
  Sets or clears the virtual timer mask.
- [func hv_vcpu_set_vtimer_offset(hv_vcpu_t, UInt64) -> hv_return_t](hv_vcpu_set_vtimer_offset(_:_:).md)
  Sets the vTimer offset to a value that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_get_vtimer_offset(_:_:))*