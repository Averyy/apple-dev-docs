# original_ppid

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The original parent process ID.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var original_ppid: pid_t
```

```c
pid_t original_ppid;
```

#### Discussion

This field stays constant, even if the process’ parent changes.

## See Also

### Inspecting Process IDs
- [var ppid: pid_t](./ppid.md)
  The parent process identifier.
- [var group_id: pid_t](./group_id.md)
  The process group identifier.
- [var session_id: pid_t](./session_id.md)
  The identifier of the session that contains the process group.
- [var tty: UnsafeMutablePointer<es_file_t>?](./tty.md)
  The TTY associated with the process sending the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t/original_ppid)*