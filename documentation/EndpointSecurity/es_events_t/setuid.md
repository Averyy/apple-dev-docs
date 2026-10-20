# setuid

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

Properties of an event that indicates a change to a process’s user ID.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var setuid: es_event_setuid_t { get set }
```

```c
es_event_setuid_t setuid;
```

## See Also

### User and Group ID Events
- [var setgid: es_event_setgid_t](./setgid.md)
  Properties of an event that indicates a change to a process’s group ID.
- [var seteuid: es_event_seteuid_t](./seteuid.md)
  Properties of an event that indicates a change to a process’s effective user ID.
- [var setegid: es_event_setegid_t](./setegid.md)
  Properties of an event that indicates a change to a process’s effective group ID.
- [var setreuid: es_event_setreuid_t](./setreuid.md)
  Properties of an event that indicates a change to a process’s real and effective user IDs.
- [var setregid: es_event_setregid_t](./setregid.md)
  Properties of an event that indicates a change to a process’s real and effective group IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_events_t/setuid)*