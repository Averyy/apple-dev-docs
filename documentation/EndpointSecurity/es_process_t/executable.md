# executable

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The file containing the executed process.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var executable: UnsafeMutablePointer<es_file_t>
```

```c
es_file_t * executable;
```

## See Also

### Inspecting the Source Process
- [var audit_token: audit_token_t](./audit_token.md)
  A token for use with Basic Security Module auditing functions.
- [var is_es_client: Bool](./is_es_client.md)
  A Boolean value that indicates whether the process connects to the Endpoint Security subsystem.
- [var is_platform_binary: Bool](./is_platform_binary.md)
  A Boolean value that indicates whether the process is a platform binary.
- [var start_time: timeval](./start_time.md)
  The time the process started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t/executable)*