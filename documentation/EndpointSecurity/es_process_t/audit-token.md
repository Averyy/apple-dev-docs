# audit_token

**Framework**: Endpoint Security  
**Kind**: property

A token for use with Basic Security Module auditing functions.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var audit_token: audit_token_t
```

#### Discussion

Use this token with the functions defined in `libbsm.h` to extract values such as the process identifier (`PID`), user identifier (`UID`), and group identifier (`GID`).

## See Also

- [var executable: UnsafeMutablePointer<es_file_t>](es_process_t/executable.md)
  The file containing the executed process.
- [var is_es_client: Bool](es_process_t/is_es_client.md)
  A Boolean value that indicates whether the process connects to the Endpoint Security subsystem.
- [var is_platform_binary: Bool](es_process_t/is_platform_binary.md)
  A Boolean value that indicates whether the process is a platform binary.
- [var start_time: timeval](es_process_t/start_time.md)
  The time the process started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t/audit_token)*