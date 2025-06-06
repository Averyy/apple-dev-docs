# start_time

**Framework**: Endpoint Security  
**Kind**: property

The time the process started.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var start_time: timeval
```

#### Discussion

This value represents the time that a fork call created the process.

This field is only available if the message [`version`](es_message_t/version.md) is `3` or greater.

## See Also

- [var audit_token: audit_token_t](es_process_t/audit_token.md)
  A token for use with Basic Security Module auditing functions.
- [var executable: UnsafeMutablePointer<es_file_t>](es_process_t/executable.md)
  The file containing the executed process.
- [var is_es_client: Bool](es_process_t/is_es_client.md)
  A Boolean value that indicates whether the process connects to the Endpoint Security subsystem.
- [var is_platform_binary: Bool](es_process_t/is_platform_binary.md)
  A Boolean value that indicates whether the process is a platform binary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t/start_time)*