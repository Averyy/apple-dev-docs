# hv_gic_reset()

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Resets the generic interrupt controller (GIC) device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func hv_gic_reset() -> hv_return_t
```

```c
extern hv_return_t hv_gic_reset();
```

#### Return Value

[`HV_SUCCESS`](./hv_success.md) on success, an error code otherwise.

#### Discussion

When you’re resetting the virtual machine, call this function to reset the GIC distributor, redistributor registers and the internal state of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_gic_reset())*