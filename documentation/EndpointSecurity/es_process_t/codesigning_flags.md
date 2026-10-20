# codesigning_flags

**Framework**: Endpoint Security  
**Kind**: property

The flags used to sign the process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var codesigning_flags: UInt32
```

#### Discussion

See `kern/cs_blobs.h` in the macOS SDK inside of the Xcode app bundle for definitions of these flags.

## See Also

- [var cdhash: es_cdhash_t](es_process_t/cdhash.md)
  The code directory hash value.
- [var signing_id: es_string_token_t](es_process_t/signing_id.md)
  The identifier used to sign the process.
- [var team_id: es_string_token_t](es_process_t/team_id.md)
  The team identifier used to sign the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t/codesigning_flags)*