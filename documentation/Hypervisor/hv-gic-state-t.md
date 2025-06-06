# hv_gic_state_t

**Framework**: Hypervisor  
**Kind**: typealias

An alias for this value type’s equivalent Hypervisor generic interrupt controller (GIC) state’s reference type.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_gic_state_t = any OS_hv_gic_state
```

## See Also

- [func hv_gic_state_create() -> hv_gic_state_t](hv_gic_state_create().md)
  Create a generic interrupt controller (GIC) state object.
- [func hv_gic_set_state(UnsafeRawPointer, Int) -> hv_return_t](hv_gic_set_state(_:_:).md)
  Sets the state of a generic interrupt controller (GIC) device.
- [func hv_gic_state_get_size(hv_gic_state_t, UnsafeMutablePointer<Int>) -> hv_return_t](hv_gic_state_get_size(_:_:).md)
  Gets the size of the buffer required for generic interrupt controller (GIC) state.
- [func hv_gic_state_get_data(hv_gic_state_t, UnsafeMutableRawPointer) -> hv_return_t](hv_gic_state_get_data(_:_:).md)
  Gets the state data for generic interrupt controller (GIC).
- [protocol OS_hv_gic_state](os_hv_gic_state.md)
  Methods that provide information on the hypervisor state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_gic_state_t)*