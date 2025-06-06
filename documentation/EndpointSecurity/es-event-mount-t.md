# es_event_mount_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the mounting of a file system.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_mount_t
```

## Topics

### Inspecting Event Properties
- [var statfs: UnsafeMutablePointer<statfs>](es_event_mount_t/statfs.md)
  The statistics of the mounted file system.
- [typealias es_statfs_t](es_statfs_t.md)
  A type that represents statistics about a file system.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_mount_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(statfs: UnsafeMutablePointer<statfs>, disposition: es_mount_disposition_t, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_mount_t/init(statfs:disposition:reserved:).md)
### Instance Properties
- [var disposition: es_mount_disposition_t](es_event_mount_t/disposition.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_unmount_t](es_event_unmount_t.md)
  A type for an event that indicates the unmounting of a file system.
- [struct es_event_remount_t](es_event_remount_t.md)
  A type for an event that indicates the unmounting of a file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_mount_t)*