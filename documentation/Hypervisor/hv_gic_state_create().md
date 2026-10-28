# hv_gic_state_create()

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Create a generic interrupt controller (GIC) state object.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func hv_gic_state_create() -> hv_gic_state_t
```

```c
extern hv_gic_state_thv_gic_state_create();
```

## Return Value

A new GIC state object that represents the current GIC state.

## Discussion

Release this object with [`os_release`](../os/os_release-c.func.md) when it’s no longer needed.

## See Also

### Getting and setting the GIC’s state
- [func hv_gic_set_state(UnsafeRawPointer, Int) -> hv_return_t](./hv_gic_set_state%28_,_%29.md)
  Sets the state of a generic interrupt controller (GIC) device.
- [func hv_gic_state_get_size(hv_gic_state_t, UnsafeMutablePointer<Int>) -> hv_return_t](./hv_gic_state_get_size%28_,_%29.md)
  Gets the size of the buffer required for generic interrupt controller (GIC) state.
- [func hv_gic_state_get_data(hv_gic_state_t, UnsafeMutableRawPointer) -> hv_return_t](./hv_gic_state_get_data%28_,_%29.md)
  Gets the state data for generic interrupt controller (GIC).
- [typealias hv_gic_state_t](./hv_gic_state_t.md)
  An alias for this value type’s equivalent Hypervisor generic interrupt controller (GIC) state’s reference type.
- [protocol OS_hv_gic_state](./os_hv_gic_state.md)
  Methods that provide information on the hypervisor state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_gic_state_create())*