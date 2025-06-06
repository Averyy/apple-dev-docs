# es_event_setgid_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the setting of a process’s group ID.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_setgid_t
```

## Topics

### Inspecting Event Properties
- [var gid: uid_t](es_event_setgid_t/gid.md)
  The group ID.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_setgid_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init()](es_event_setgid_t/init.md)
- [init(gid: uid_t, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_setgid_t/init(gid:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct es_event_setuid_t](es_event_setuid_t.md)
  A type for an event that indicates the setting of a process’s user ID.
- [struct es_event_seteuid_t](es_event_seteuid_t.md)
  A type for an event that indicates the setting of a process’s effective user ID.
- [struct es_event_setegid_t](es_event_setegid_t.md)
  A type for an event that indicates the setting of a process’s effective group ID.
- [struct es_event_setreuid_t](es_event_setreuid_t.md)
  A type for an event that indicates the setting of a process’s real and effective user IDs.
- [struct es_event_setregid_t](es_event_setregid_t.md)
  A type for an event that indicates the setting of a process’s real and effective group IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_setgid_t)*