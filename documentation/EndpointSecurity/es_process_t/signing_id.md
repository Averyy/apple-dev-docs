# signing_id

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The identifier used to sign the process.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var signing_id: es_string_token_t
```

```c
es_string_token_t signing_id;
```

## See Also

### Inspecting Code Signing Properties
- [var codesigning_flags: UInt32](./codesigning_flags.md)
  The flags used to sign the process.
- [var cdhash: es_cdhash_t](./cdhash.md)
  The code directory hash value.
- [var team_id: es_string_token_t](./team_id.md)
  The team identifier used to sign the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t/signing_id)*