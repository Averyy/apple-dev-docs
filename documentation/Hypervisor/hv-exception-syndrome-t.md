# hv_exception_syndrome_t

**Framework**: Hypervisor  
**Kind**: typealias

Type of a vCPU exception syndrome.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_exception_syndrome_t = UInt64
```

#### Discussion

This corresponds to Exception Syndrome Register  EL2 (ESR_EL2).

## See Also

- [struct hv_exit_reason_t](hv_exit_reason_t.md)
  The type that describes the event that triggered a guest exit to the host.
- [typealias hv_exception_address_t](hv_exception_address_t.md)
  Type of a vCPU exception virtual address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_exception_syndrome_t)*