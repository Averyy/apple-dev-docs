# hv_gic_state_get_data(_:_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Gets the state data for generic interrupt controller (GIC).

**Availability**:
- macOS 15.0+

## Declaration

```swift
func hv_gic_state_get_data(_ state: hv_gic_state_t, _ gic_state_data: UnsafeMutableRawPointer) -> hv_return_t
```

```c
extern hv_return_t hv_gic_state_get_data(hv_gic_state_t state, void *gic_state_data);
```

## Return Value

[`HV_SUCCESS`](./hv_success.md) on success; otherwise, an error code.

## Discussion

The function returns an opaque data buffer that contains the complete serialized state of the device, except for the GIC CPU registers. You can write the data to a file and is stable. It’s also versioned which allows the framework to detect incompatibilities when it restores the state. The size of this GIC state buffer must be at least as large as the size returned by [`hv_gic_state_get_size(_:_:)`](./hv_gic_state_get_size%28_,_%29.md).

You can read GIC CPU system registers separately, and save them to be able to restore the CPU state for the virtual machine.

## Parameters

- `state`: The GIC state object.
- `gic_state_data`: Pointer to GIC state buffer that the framework writes to upon success.

## See Also

### Getting and setting the GIC’s state
- [func hv_gic_state_create() -> hv_gic_state_t](./hv_gic_state_create%28%29.md)
  Create a generic interrupt controller (GIC) state object.
- [func hv_gic_set_state(UnsafeRawPointer, Int) -> hv_return_t](./hv_gic_set_state%28_,_%29.md)
  Sets the state of a generic interrupt controller (GIC) device.
- [func hv_gic_state_get_size(hv_gic_state_t, UnsafeMutablePointer<Int>) -> hv_return_t](./hv_gic_state_get_size%28_,_%29.md)
  Gets the size of the buffer required for generic interrupt controller (GIC) state.
- [typealias hv_gic_state_t](./hv_gic_state_t.md)
  An alias for this value type’s equivalent Hypervisor generic interrupt controller (GIC) state’s reference type.
- [protocol OS_hv_gic_state](./os_hv_gic_state.md)
  Methods that provide information on the hypervisor state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_gic_state_get_data(_:_:))*