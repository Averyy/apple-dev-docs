# ES_EVENT_TYPE_AUTH_UNLINK

**Framework**: Endpoint Security  
**Kind**: var

An identifier for a process that requests permission from the operating system to delete a file.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var ES_EVENT_TYPE_AUTH_UNLINK: es_event_type_t { get }
```

#### Discussion

This identifier corresponds to the [`es_events_t`](es_events_t.md) union member [`unlink`](es_events_t/unlink.md), which has the type [`es_event_unlink_t`](es_event_unlink_t.md).

## See Also

- [var ES_EVENT_TYPE_AUTH_CHDIR: es_event_type_t](es_event_type_auth_chdir.md)
  An identifier for a process that requests permission from the operating system to change the working directory for the process.
- [var ES_EVENT_TYPE_AUTH_CHROOT: es_event_type_t](es_event_type_auth_chroot.md)
  An identifier for a process that requests permission from the operating system to change the root directory for the process.
- [var ES_EVENT_TYPE_AUTH_CLONE: es_event_type_t](es_event_type_auth_clone.md)
  An identifier for a process that requests permission from the operating system to clone a file.
- [var ES_EVENT_TYPE_AUTH_COPYFILE: es_event_type_t](es_event_type_auth_copyfile.md)
  An identifier for a process that requests permission from the operating system to copy a file.
- [var ES_EVENT_TYPE_AUTH_CREATE: es_event_type_t](es_event_type_auth_create.md)
  An identifier for a process that requests permission from the operating system to create a file.
- [var ES_EVENT_TYPE_AUTH_DELETEEXTATTR: es_event_type_t](es_event_type_auth_deleteextattr.md)
  An identifier for a process that requests permission from the operating system to delete an extended attribute from a file.
- [var ES_EVENT_TYPE_AUTH_EXCHANGEDATA: es_event_type_t](es_event_type_auth_exchangedata.md)
  An identifier for a process that requests permission from the operating system to exchange data between two files.
- [var ES_EVENT_TYPE_AUTH_EXEC: es_event_type_t](es_event_type_auth_exec.md)
  An identifier for a process that requests permission from the operating system to execute another image.
- [var ES_EVENT_TYPE_AUTH_FCNTL: es_event_type_t](es_event_type_auth_fcntl.md)
  An identifier for a process that requests permission from the operating system to manipulate a file descriptor.
- [var ES_EVENT_TYPE_AUTH_FILE_PROVIDER_MATERIALIZE: es_event_type_t](es_event_type_auth_file_provider_materialize.md)
  An identifier for a process that requests permission for a file provider to return a reference to a file.
- [var ES_EVENT_TYPE_AUTH_FILE_PROVIDER_UPDATE: es_event_type_t](es_event_type_auth_file_provider_update.md)
  An identifier for a process that requests permission from the operating system to update a file.
- [var ES_EVENT_TYPE_AUTH_FSGETPATH: es_event_type_t](es_event_type_auth_fsgetpath.md)
  An identifier for a process that requests permission from the operating system to retrieve a file system path.
- [var ES_EVENT_TYPE_AUTH_GET_TASK: es_event_type_t](es_event_type_auth_get_task.md)
  An identifier for a process that requests permission from the operating system to retrieve a process’s task control port.
- [var ES_EVENT_TYPE_AUTH_GET_TASK_READ: es_event_type_t](es_event_type_auth_get_task_read.md)
  An identifier for a process that requests permission from the operating system to retrieve a process’s task read port.
- [var ES_EVENT_TYPE_AUTH_GETATTRLIST: es_event_type_t](es_event_type_auth_getattrlist.md)
  An identifier for a process that requests permission from the operating system to retrieve attributes from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_type_auth_unlink)*