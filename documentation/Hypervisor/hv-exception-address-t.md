# hv_exception_address_t

**Framework**: Hypervisor  
**Kind**: typealias

Type of a vCPU exception virtual address.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_exception_address_t = UInt64
```

#### Discussion

This corresponds to Fault Address Register EL2 (FAR_EL2).

## See Also

- [struct hv_exit_reason_t](hv_exit_reason_t.md)
  The type that describes the event that triggered a guest exit to the host.
- [typealias hv_exception_syndrome_t](hv_exception_syndrome_t.md)
  Type of a vCPU exception syndrome.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_exception_address_t)*