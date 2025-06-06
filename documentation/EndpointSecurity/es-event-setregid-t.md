# es_event_setregid_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the setting of a process’s real and effective group IDs.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_setregid_t
```

## Topics

### Inspecting Event Properties
- [var rgid: uid_t](es_event_setregid_t/rgid.md)
  The real group ID.
- [var egid: uid_t](es_event_setregid_t/egid.md)
  The effective group ID.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_setregid_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init()](es_event_setregid_t/init.md)
- [init(rgid: uid_t, egid: uid_t, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_setregid_t/init(rgid:egid:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct es_event_setuid_t](es_event_setuid_t.md)
  A type for an event that indicates the setting of a process’s user ID.
- [struct es_event_setgid_t](es_event_setgid_t.md)
  A type for an event that indicates the setting of a process’s group ID.
- [struct es_event_seteuid_t](es_event_seteuid_t.md)
  A type for an event that indicates the setting of a process’s effective user ID.
- [struct es_event_setegid_t](es_event_setegid_t.md)
  A type for an event that indicates the setting of a process’s effective group ID.
- [struct es_event_setreuid_t](es_event_setreuid_t.md)
  A type for an event that indicates the setting of a process’s real and effective user IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_setregid_t)*