# HV_EXIT_REASON_EXCEPTION

**Framework**: Hypervisor  
**Kind**: var

The value that identifies traps caused by the guest operations.

**Availability**:
- macOS ?+

## Declaration

```swift
var HV_EXIT_REASON_EXCEPTION: hv_exit_reason_t { get }
```

## See Also

- [var HV_EXIT_REASON_CANCELED: hv_exit_reason_t](hv_exit_reason_canceled.md)
  The value that identifies exits requested by exit handler on the host.
- [var HV_EXIT_REASON_VTIMER_ACTIVATED: hv_exit_reason_t](hv_exit_reason_vtimer_activated.md)
  The value that identifies when the virtual timer enters the pending state.
- [var HV_EXIT_REASON_UNKNOWN: hv_exit_reason_t](hv_exit_reason_unknown.md)
  The value that identifies unexpected exits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_exit_reason_exception)*