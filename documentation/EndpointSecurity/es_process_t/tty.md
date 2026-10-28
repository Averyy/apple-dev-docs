# tty

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The TTY associated with the process sending the message.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var tty: UnsafeMutablePointer<es_file_t>?
```

```c
es_file_t * tty;
```

## Discussion

This field is available if the message version is greater than `2`.

## See Also

### Inspecting Process IDs
- [var ppid: pid_t](./ppid.md)
  The parent process identifier.
- [var original_ppid: pid_t](./original_ppid.md)
  The original parent process ID.
- [var group_id: pid_t](./group_id.md)
  The process group identifier.
- [var session_id: pid_t](./session_id.md)
  The identifier of the session that contains the process group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t/tty)*