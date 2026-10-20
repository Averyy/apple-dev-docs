# es_event_unmount_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

A type for an event that indicates the unmounting of a file system.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_event_unmount_t
```

```c
typedef struct { ... } es_event_unmount_t;
```

## Topics

### Inspecting Event Properties
- [var statfs: UnsafeMutablePointer<statfs>](./es_event_unmount_t/statfs.md)
  The statistics of the unmounted file system.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./es_event_unmount_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(statfs: UnsafeMutablePointer<statfs>, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](./es_event_unmount_t/init%28statfs,reserved%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### File System Mounting Event Types
- [struct es_event_mount_t](./es_event_mount_t.md)
  A type for an event that indicates the mounting of a file system.
- [struct es_event_remount_t](./es_event_remount_t.md)
  A type for an event that indicates the unmounting of a file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_unmount_t)*