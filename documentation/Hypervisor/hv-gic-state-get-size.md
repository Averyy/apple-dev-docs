# hv_gic_state_get_size(_:_:)

**Framework**: Hypervisor  
**Kind**: func

Gets the size of the buffer required for generic interrupt controller (GIC) state.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func hv_gic_state_get_size(_ state: hv_gic_state_t, _ gic_state_size: UnsafeMutablePointer<Int>) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) on success; otherwise, an error code.

## Parameters

- `state`: The GIC state object.
- `gic_state_size`: The pointer to GIC data size, that the framework writes to upon success.

## See Also

- [func hv_gic_state_create() -> hv_gic_state_t](hv_gic_state_create().md)
  Create a generic interrupt controller (GIC) state object.
- [func hv_gic_set_state(UnsafeRawPointer, Int) -> hv_return_t](hv_gic_set_state(_:_:).md)
  Sets the state of a generic interrupt controller (GIC) device.
- [func hv_gic_state_get_data(hv_gic_state_t, UnsafeMutableRawPointer) -> hv_return_t](hv_gic_state_get_data(_:_:).md)
  Gets the state data for generic interrupt controller (GIC).
- [typealias hv_gic_state_t](hv_gic_state_t.md)
  An alias for this value type’s equivalent Hypervisor generic interrupt controller (GIC) state’s reference type.
- [protocol OS_hv_gic_state](os_hv_gic_state.md)
  Methods that provide information on the hypervisor state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_gic_state_get_size(_:_:))*