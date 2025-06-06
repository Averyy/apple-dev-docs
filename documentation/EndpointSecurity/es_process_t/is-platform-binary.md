# is_platform_binary

**Framework**: Endpoint Security  
**Kind**: property

A Boolean value that indicates whether the process is a platform binary.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var is_platform_binary: Bool
```

#### Discussion

For the purposes of this value, a “platform binary” is one signed with Apple certificates.

## See Also

- [var audit_token: audit_token_t](es_process_t/audit_token.md)
  A token for use with Basic Security Module auditing functions.
- [var executable: UnsafeMutablePointer<es_file_t>](es_process_t/executable.md)
  The file containing the executed process.
- [var is_es_client: Bool](es_process_t/is_es_client.md)
  A Boolean value that indicates whether the process connects to the Endpoint Security subsystem.
- [var start_time: timeval](es_process_t/start_time.md)
  The time the process started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t/is_platform_binary)*