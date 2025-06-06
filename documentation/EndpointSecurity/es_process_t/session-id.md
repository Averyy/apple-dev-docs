# session_id

**Framework**: Endpoint Security  
**Kind**: property

The identifier of the session that contains the process group.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var session_id: pid_t
```

## See Also

- [var ppid: pid_t](es_process_t/ppid.md)
  The parent process identifier.
- [var original_ppid: pid_t](es_process_t/original_ppid.md)
  The original parent process ID.
- [var group_id: pid_t](es_process_t/group_id.md)
  The process group identifier.
- [var tty: UnsafeMutablePointer<es_file_t>?](es_process_t/tty.md)
  The TTY associated with the process sending the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t/session_id)*