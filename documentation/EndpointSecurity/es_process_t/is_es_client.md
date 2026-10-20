# is_es_client

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the process connects to the Endpoint Security subsystem.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var is_es_client: Bool
```

```c
bool is_es_client;
```

## See Also

### Inspecting the Source Process
- [var audit_token: audit_token_t](./audit_token.md)
  A token for use with Basic Security Module auditing functions.
- [var executable: UnsafeMutablePointer<es_file_t>](./executable.md)
  The file containing the executed process.
- [var is_platform_binary: Bool](./is_platform_binary.md)
  A Boolean value that indicates whether the process is a platform binary.
- [var start_time: timeval](./start_time.md)
  The time the process started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t/is_es_client)*