# es_proc_check_type_t

**Framework**: Endpoint Security  
**Kind**: struct

The type of call used when a process checks on the access of the target process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_proc_check_type_t
```

#### Overview

This value provides detail, in coordination with [`flavor`](es_event_proc_check_t/flavor.md) from [`es_event_proc_check_t`](es_event_proc_check_t.md), to identify the functions and the type of data returned from checks called in `libproc.h`.

## Topics

### Process Check Result Types
- [var ES_PROC_CHECK_TYPE_DIRTYCONTROL: es_proc_check_type_t](es_proc_check_type_dirtycontrol.md)
  A type of process check that uses the process’s dirty state.
- [var ES_PROC_CHECK_TYPE_LISTPIDS: es_proc_check_type_t](es_proc_check_type_listpids.md)
  A type of process check that lists related process identifiers.
- [var ES_PROC_CHECK_TYPE_PIDFDINFO: es_proc_check_type_t](es_proc_check_type_pidfdinfo.md)
  A type of process check that gets file descriptor information.
- [var ES_PROC_CHECK_TYPE_PIDFILEPORTINFO: es_proc_check_type_t](es_proc_check_type_pidfileportinfo.md)
  A type of process check that gets port information.
- [var ES_PROC_CHECK_TYPE_PIDINFO: es_proc_check_type_t](es_proc_check_type_pidinfo.md)
  A type of process check that gets basic process information.
- [var ES_PROC_CHECK_TYPE_PIDRUSAGE: es_proc_check_type_t](es_proc_check_type_pidrusage.md)
  A type of process check that gets a process’s resource usage information.
- [var ES_PROC_CHECK_TYPE_SETCONTROL: es_proc_check_type_t](es_proc_check_type_setcontrol.md)
  A type of process check that sets the process control state.
### Deprecated Result Types
- [var ES_PROC_CHECK_TYPE_KERNMSGBUF: es_proc_check_type_t](es_proc_check_type_kernmsgbuf.md)
  A type of process check that checks the message buffer.
- [var ES_PROC_CHECK_TYPE_TERMINATE: es_proc_check_type_t](es_proc_check_type_terminate.md)
  A type of process check that terninates a process.
- [var ES_PROC_CHECK_TYPE_UDATA_INFO: es_proc_check_type_t](es_proc_check_type_udata_info.md)
  A type of process check that involves a user data token.
### Initializers
- [init(UInt32)](es_proc_check_type_t/init(_:).md)
- [init(rawValue: UInt32)](es_proc_check_type_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](es_proc_check_type_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var flavor: Int32](es_event_proc_check_t/flavor.md)
  A representation of the information sought by a process based on the type member of [`es_event_proc_check_t`](es_event_proc_check_t.md).
- [var target: UnsafeMutablePointer<es_process_t>?](es_event_proc_check_t/target.md)
  The process targeted by this event.
- [var type: es_proc_check_type_t](es_event_proc_check_t/type.md)
  The type of call number used to check the access on the target process.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_proc_check_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_proc_check_type_t)*