# cdhash

**Framework**: Endpoint Security  
**Kind**: property

The code directory hash value.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var cdhash: es_cdhash_t
```

#### Discussion

The code directory hash identifies a specific version of a program. This allows the system to verify that the contents of a binary have not changed since being code-signed.

## See Also

- [var codesigning_flags: UInt32](es_process_t/codesigning_flags.md)
  The flags used to sign the process.
- [var signing_id: es_string_token_t](es_process_t/signing_id.md)
  The identifier used to sign the process.
- [var team_id: es_string_token_t](es_process_t/team_id.md)
  The team identifier used to sign the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t/cdhash)*