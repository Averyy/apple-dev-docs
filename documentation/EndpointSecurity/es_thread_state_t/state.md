# state

**Framework**: Endpointsecurity  
**Kind**: property

The machine-specific thread state.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var state: es_token_t
```

#### Discussion

This equivalent to [`thread_state_t`](https://developer.apple.com/documentation/kernel/thread_state_t) in Mach APIs.

> **Note**:  The [`size`](es_token_t/size.md) subfield of the [`state`](es_thread_state_t/state.md) field is in bytes, not [`natural_t`](https://developer.apple.com/documentation/kernel/natural_t) units.

## See Also

- [var flavor: Int32](es_thread_state_t/flavor.md)
  An indication of the representation of the machine-specific thread state.
- [struct es_token_t](es_token_t.md)
  An arbitrary buffer of data with its size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_thread_state_t/state)*