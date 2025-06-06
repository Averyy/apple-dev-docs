# es_event_seteuid_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the setting of a process’s effective user ID.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_seteuid_t
```

## Topics

### Inspecting Event Properties
- [var euid: uid_t](es_event_seteuid_t/euid.md)
  The effective user ID.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_seteuid_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init()](es_event_seteuid_t/init.md)
- [init(euid: uid_t, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_seteuid_t/init(euid:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct es_event_setuid_t](es_event_setuid_t.md)
  A type for an event that indicates the setting of a process’s user ID.
- [struct es_event_setgid_t](es_event_setgid_t.md)
  A type for an event that indicates the setting of a process’s group ID.
- [struct es_event_setegid_t](es_event_setegid_t.md)
  A type for an event that indicates the setting of a process’s effective group ID.
- [struct es_event_setreuid_t](es_event_setreuid_t.md)
  A type for an event that indicates the setting of a process’s real and effective user IDs.
- [struct es_event_setregid_t](es_event_setregid_t.md)
  A type for an event that indicates the setting of a process’s real and effective group IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_seteuid_t)*