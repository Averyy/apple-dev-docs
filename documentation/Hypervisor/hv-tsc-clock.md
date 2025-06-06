# hv_tsc_clock()

**Framework**: Hypervisor  
**Kind**: func

Returns the value of an abstract clock.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_tsc_clock() -> UInt64
```

#### Return Value

A 64-bit unsigned integer that represents the current clock value.

#### Discussion

The abstract clock ticks at the same rate as the host TSC, offset by an implementation-dependent constant. The clock value increases monotonically.

## See Also

- [func hv_vcpu_set_tsc_relative(hv_vcpuid_t, Int64) -> hv_return_t](hv_vcpu_set_tsc_relative(_:_:).md)
  Sets the offset of the guest timestamp-counter (TSC) relative to the Hypervisor’s TSC clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_tsc_clock())*