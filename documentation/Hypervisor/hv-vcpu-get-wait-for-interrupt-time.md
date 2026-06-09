# hv_vcpu_get_wait_for_interrupt_time(_:_:)

**Framework**: Hypervisor  
**Kind**: func

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func hv_vcpu_get_wait_for_interrupt_time(_ vcpu: hv_vcpu_t, _ time: UnsafeMutablePointer<UInt64>) -> hv_return_t
```

#### Return Value

HV_SUCCESS on success, error code otherwise.

#### Discussion

Returns the cumulative wait time of a vCPU spent at WFI instruction while waiting for interrupts in the units of mach_absolute_time().

Must be called by the owning thread. Returns HV_UNSUPPORTED if the VM was created without a GIC device (hv_gic_create).

## Parameters

- `vcpu`: ID of the vcpu instance.
- `time`: Pointer to wait time value (written on success).


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_get_wait_for_interrupt_time(_:_:))*