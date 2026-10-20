# state

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The machine-specific thread state.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var state: es_token_t
```

```c
es_token_t state;
```

#### Discussion

This equivalent to [`thread_state_t`](../../kernel/thread_state_t.md) in Mach APIs.

> **Note**:  The [`size`](../es_token_t/size.md) subfield of the [`state`](./state.md) field is in bytes, not [`natural_t`](../../kernel/natural_t.md) units.

## See Also

### Inspecting Thread State
- [var flavor: Int32](./flavor.md)
  An indication of the representation of the machine-specific thread state.
- [struct es_token_t](../es_token_t.md)
  An arbitrary buffer of data with its size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_thread_state_t/state)*