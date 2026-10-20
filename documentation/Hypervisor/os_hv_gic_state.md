# OS_hv_gic_state

**Framework**: Hypervisor  
**Kind**: protocol  
**Role**: Protocol

Methods that provide information on the hypervisor state.

**Availability**:
- macOS

## Declaration

```swift
protocol OS_hv_gic_state : NSObjectProtocol
```

```objc
@protocol OS_hv_gic_state <NSObject>
```

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Getting and setting the GIC’s state
- [func hv_gic_state_create() -> hv_gic_state_t](./hv_gic_state_create%28%29.md)
  Create a generic interrupt controller (GIC) state object.
- [func hv_gic_set_state(UnsafeRawPointer, Int) -> hv_return_t](./hv_gic_set_state%28_,_%29.md)
  Sets the state of a generic interrupt controller (GIC) device.
- [func hv_gic_state_get_size(hv_gic_state_t, UnsafeMutablePointer<Int>) -> hv_return_t](./hv_gic_state_get_size%28_,_%29.md)
  Gets the size of the buffer required for generic interrupt controller (GIC) state.
- [func hv_gic_state_get_data(hv_gic_state_t, UnsafeMutableRawPointer) -> hv_return_t](./hv_gic_state_get_data%28_,_%29.md)
  Gets the state data for generic interrupt controller (GIC).
- [typealias hv_gic_state_t](./hv_gic_state_t.md)
  An alias for this value type’s equivalent Hypervisor generic interrupt controller (GIC) state’s reference type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/os_hv_gic_state)*