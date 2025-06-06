# hv_exit_reason_t

**Framework**: Hypervisor  
**Kind**: struct

The type that describes the event that triggered a guest exit to the host.

**Availability**:
- macOS ?+

## Declaration

```swift
struct hv_exit_reason_t
```

## Topics

### Instance Properties
- [var rawValue: UInt32](hv_exit_reason_t/rawvalue.md)
  The unsigned 32-bit integer that represents virual macine exit reasons.
### Initializers
- [init(UInt32)](hv_exit_reason_t/init(_:).md)
  Creates a new exit reason instance with the value you provide.
- [init(rawValue: UInt32)](hv_exit_reason_t/init(rawvalue:).md)
  Creates a new exit reason instance with the value you provide.
### Exit Reasons
- [var HV_EXIT_REASON_CANCELED: hv_exit_reason_t](hv_exit_reason_canceled.md)
  The value that identifies exits requested by exit handler on the host.
- [var HV_EXIT_REASON_EXCEPTION: hv_exit_reason_t](hv_exit_reason_exception.md)
  The value that identifies traps caused by the guest operations.
- [var HV_EXIT_REASON_VTIMER_ACTIVATED: hv_exit_reason_t](hv_exit_reason_vtimer_activated.md)
  The value that identifies when the virtual timer enters the pending state.
- [var HV_EXIT_REASON_UNKNOWN: hv_exit_reason_t](hv_exit_reason_unknown.md)
  The value that identifies unexpected exits.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias hv_exception_syndrome_t](hv_exception_syndrome_t.md)
  Type of a vCPU exception syndrome.
- [typealias hv_exception_address_t](hv_exception_address_t.md)
  Type of a vCPU exception virtual address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_exit_reason_t)*