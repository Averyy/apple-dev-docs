# hv_gic_set_state(_:_:)

**Framework**: Hypervisor  
**Kind**: func

Sets the state of a generic interrupt controller (GIC) device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func hv_gic_set_state(_ gic_state_data: UnsafeRawPointer, _ gic_state_size: Int) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) on success; otherwise, an error code.

#### Discussion

Use this method to restore the state of a GIC. You can only restore a GIC’s state after creating a GIC device and vCPUs and before the vCPUs are running. Restore the rest of the virtual machine including GIC CPU registers with values that are compatible with the [`hv_gic_state_t`](hv_gic_state_t.md).

In some cases this method can fail if a software update has changed the host in a way that would be incompatible with the previous format.

## Parameters

- `gic_state_data`: A pointer to the state buffer to use to set the GIC.
- `gic_state_size`: Size of GIC state buffer, in bytes.

## See Also

- [func hv_gic_state_create() -> hv_gic_state_t](hv_gic_state_create().md)
  Create a generic interrupt controller (GIC) state object.
- [func hv_gic_state_get_size(hv_gic_state_t, UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_state_get_size(_:_:).md)
  Gets the size of the buffer required for generic interrupt controller (GIC) state.
- [func hv_gic_state_get_data(hv_gic_state_t, UnsafeMutableRawPointer) -> hv_return_t](hv_gic_state_get_data(_:_:).md)
  Gets the state data for generic interrupt controller (GIC).
- [typealias hv_gic_state_t](hv_gic_state_t.md)
  An alias for this value type’s equivalent Hypervisor generic interrupt controller (GIC) state’s reference type.
- [protocol OS_hv_gic_state](os_hv_gic_state.md)
  Methods that provide information on the hypervisor state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_gic_set_state(_:_:))*