# remount

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

Properties of an event that indicates the remounting of a file system.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var remount: es_event_remount_t { get set }
```

```c
es_event_remount_t remount;
```

## See Also

### File System Mounting Events
- [var mount: es_event_mount_t](./mount.md)
  Properties of an event that indicates the mounting of a file system.
- [var unmount: es_event_unmount_t](./unmount.md)
  Properties of an event that indicates the unmounting of a file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_events_t/remount)*