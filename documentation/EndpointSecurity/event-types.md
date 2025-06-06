# Event Types

**Framework**: Endpoint Security

Types used by messages to deliver details specific to different kinds of Endpoint Security events.

#### Overview

The types in this section contain details of each event that an Endpoint Security message can contain. While the [`es_message_t`](es_message_t.md) type itself is generic, the members of its [`event`](es_message_t/event.md) union contain specific event types.

For example, when the message’s [`event_type`](es_message_t/event_type.md) is [`ES_EVENT_TYPE_NOTIFY_FORK`](es_event_type_notify_fork.md), you access the event’s [`fork`](es_events_t/fork.md) member, whose type is [`es_event_fork_t`](es_event_fork_t.md). This type has properties specific to process-forking events, such as the [`child`](es_event_fork_t/child.md) process that resulted from the fork operation.

## Topics

### File-System Event Types
- [struct es_file_t](es_file_t.md)
  A type that represents a file related to an Endpoint Security event.
- [struct es_event_access_t](es_event_access_t.md)
  A type for an event that indicates the checking of a file’s access permission.
- [struct es_event_clone_t](es_event_clone_t.md)
  A type for an event that indicates the cloning of a file.
- [struct es_event_copyfile_t](es_event_copyfile_t.md)
  A type for an event that indicates the copying of a file by use of a system call.
- [struct es_event_create_t](es_event_create_t.md)
  A type for an event that indicates the creation of a file.
- [struct es_event_dup_t](es_event_dup_t.md)
  A type for an event that indicates the duplication of a file descriptor.
- [struct es_event_fcntl_t](es_event_fcntl_t.md)
  A type for an event that indicates the manipulation of a file descriptor.
- [struct es_event_open_t](es_event_open_t.md)
  A type for an event that indicates the opening of a file.
- [struct es_event_close_t](es_event_close_t.md)
  A type for an event that indicates the closing of a file.
- [struct es_event_rename_t](es_event_rename_t.md)
  A type for an event that indicates the renaming of a file.
- [struct es_event_truncate_t](es_event_truncate_t.md)
  A type for an event that indicates the truncation of a file.
- [struct es_event_exchangedata_t](es_event_exchangedata_t.md)
  A type for an event that indicates the exchange of data between two files.
- [struct es_event_write_t](es_event_write_t.md)
  A type for an event that indicates the writing of data to a file.
- [struct es_event_lookup_t](es_event_lookup_t.md)
  A type for an event that indicates the lookup of a file’s path.
- [struct es_event_searchfs_t](es_event_searchfs_t.md)
  A type for an event that indicates searching a volume or mounted file system.
### File Metadata Event Types
- [struct es_event_deleteextattr_t](es_event_deleteextattr_t.md)
  A type for an event that indicates the deletion of an extended attribute from a file.
- [struct es_event_fsgetpath_t](es_event_fsgetpath_t.md)
  A type for an event that indicates the retrieval of a file-system path.
- [struct es_event_getattrlist_t](es_event_getattrlist_t.md)
  A type for an event that indicates the retrieval of attributes from a file.
- [struct es_event_getextattr_t](es_event_getextattr_t.md)
  A type for an event that indicates the retrieval of an extended attribute from a file.
- [struct es_event_listextattr_t](es_event_listextattr_t.md)
  A type for an event that indicates the retrieval of multiple extended attributes from a file.
- [struct es_event_readdir_t](es_event_readdir_t.md)
  A type for an event that indicates the reading of a file-system directory.
- [struct es_event_setacl_t](es_event_setacl_t.md)
  A type for an event that indicates the setting of a file’s access control list.
- [struct es_event_setattrlist_t](es_event_setattrlist_t.md)
  A type for an event that indicates the setting of a file attribute.
- [struct es_event_setextattr_t](es_event_setextattr_t.md)
  A type for an event that indicates the setting of a file’s extended attribute.
- [struct es_event_setflags_t](es_event_setflags_t.md)
  A type for an event that indicates the setting of a file’s flags.
- [struct es_event_setmode_t](es_event_setmode_t.md)
  A type for an event that indicates the setting of a file’s mode.
- [struct es_event_setowner_t](es_event_setowner_t.md)
  A type for an event that indicates the setting of a file’s owner.
- [struct es_event_stat_t](es_event_stat_t.md)
  A type for an event that indicates the retrieval of a file’s status.
- [struct es_event_utimes_t](es_event_utimes_t.md)
  A type for an event that indicates a change to a file’s access time or modification time.
### File Provider Event Types
- [struct es_event_file_provider_materialize_t](es_event_file_provider_materialize_t.md)
  A type for an event that indicates the materialization of a file provider.
- [struct es_event_file_provider_update_t](es_event_file_provider_update_t.md)
  A type for an event that indicates an update to a file provider.
### Link Event Types
- [struct es_event_link_t](es_event_link_t.md)
  A type for an event that indicates the creation of a hard link.
- [struct es_event_readlink_t](es_event_readlink_t.md)
  A type for an event that indicates the reading of a symbolic link.
- [struct es_event_unlink_t](es_event_unlink_t.md)
  A type for an event that indicates the deletion of a file.
### File System Mounting Event Types
- [struct es_event_mount_t](es_event_mount_t.md)
  A type for an event that indicates the mounting of a file system.
- [struct es_event_unmount_t](es_event_unmount_t.md)
  A type for an event that indicates the unmounting of a file system.
- [struct es_event_remount_t](es_event_remount_t.md)
  A type for an event that indicates the unmounting of a file system.
### Memory Mapping Event Types
- [struct es_event_mmap_t](es_event_mmap_t.md)
  A type for an event that indicates the mapping of memory to a file.
- [struct es_event_mprotect_t](es_event_mprotect_t.md)
  A type for an event that indicates a change to protection of memory-mapped pages.
### Process Event Types
- [struct es_event_chdir_t](es_event_chdir_t.md)
  A type for an event that indicates a change to a process’s working directory.
- [struct es_event_chroot_t](es_event_chroot_t.md)
  A type for an event that indicates a change to a process’s root directory.
- [struct es_event_exec_t](es_event_exec_t.md)
  A type for an event that indicates the execution of a process.
- [struct es_event_fork_t](es_event_fork_t.md)
  A type for an event that indicates the forking of a process.
- [struct es_event_proc_check_t](es_event_proc_check_t.md)
  A type that indicates the call used and the data returned when a process checks on the access of the target process.
- [struct es_event_signal_t](es_event_signal_t.md)
  A type for an event that indicates the sending of a signal to a process.
- [struct es_event_exit_t](es_event_exit_t.md)
  A type for an event that indicates a process exiting.
### Process Event Helper Functions
- [func es_exec_arg(UnsafePointer<es_event_exec_t>, UInt32) -> es_string_token_t](es_exec_arg(_:_:).md)
  Gets the argument at the specified position from a process execution event.
- [func es_exec_arg_count(UnsafePointer<es_event_exec_t>) -> UInt32](es_exec_arg_count(_:).md)
  Gets the number of arguments from a process execution event.
- [func es_exec_env(UnsafePointer<es_event_exec_t>, UInt32) -> es_string_token_t](es_exec_env(_:_:).md)
  Gets the environment variable at the specified position from a process execution event.
- [func es_exec_env_count(UnsafePointer<es_event_exec_t>) -> UInt32](es_exec_env_count(_:).md)
  Gets the number of environment variables from a process execution event.
- [func es_exec_fd(UnsafePointer<es_event_exec_t>, UInt32) -> UnsafePointer<es_fd_t>](es_exec_fd(_:_:).md)
  Gets the file descriptor at the specified position from a process execution event.
- [func es_exec_fd_count(UnsafePointer<es_event_exec_t>) -> UInt32](es_exec_fd_count(_:).md)
  Gets the number of file descriptors from a process execution event.
- [struct es_fd_t](es_fd_t.md)
  A structure that describes an open file descriptor.
### Interprocess Events
- [struct es_event_proc_suspend_resume_t](es_event_proc_suspend_resume_t.md)
  A type for an event that indicates a call to suspend, resume, or shut down sockets for a process.
- [struct es_event_trace_t](es_event_trace_t.md)
  A type for an event that indicates an attempt by one process to attach to another process.
- [struct es_event_remote_thread_create_t](es_event_remote_thread_create_t.md)
  A type for an event that indicates an attempt by one process to create a thread in another process.
### Task Port Event Types
- [struct es_event_get_task_t](es_event_get_task_t.md)
  A type for an event that indicates the retrieval of a task’s control port.
- [struct es_event_get_task_read_t](es_event_get_task_read_t.md)
  A type for an event that indicates the retrieval of a task’s read port.
- [struct es_event_get_task_inspect_t](es_event_get_task_inspect_t.md)
  A type for an event that indicates the retrieval of a task’s inspect port.
- [struct es_event_get_task_name_t](es_event_get_task_name_t.md)
  A type for an event that indicates the retrieval of a task’s name port.
### User and Group ID Types
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
- [struct es_event_setregid_t](es_event_setregid_t.md)
  A type for an event that indicates the setting of a process’s real and effective group IDs.
### Code Signing Event Types
- [struct es_event_cs_invalidated_t](es_event_cs_invalidated_t.md)
  A type for an event that indicates the invalidation of a process’ code signing status.
### Socket Event Types
- [struct es_event_uipc_bind_t](es_event_uipc_bind_t.md)
  A type for an event that indicates the binding of a socket to a path.
- [struct es_event_uipc_connect_t](es_event_uipc_connect_t.md)
  A type for an event that indicates the connection of a socket.
### Clock Event Types
- [struct es_event_settime_t](es_event_settime_t.md)
  A type for an event that indicates the modification of the system time.
### Kernel Event Types
- [struct es_event_iokit_open_t](es_event_iokit_open_t.md)
  A type for an event that indicates the opening of an IOKit device.
- [struct es_event_kextload_t](es_event_kextload_t.md)
  A type for an event that indicates the loading of a kernel extension.
- [struct es_event_kextunload_t](es_event_kextunload_t.md)
  A type for an event that indicates the unloading of a Kernel Extension (KEXT).
### Pseudoterminal Event Types
- [struct es_event_pty_close_t](es_event_pty_close_t.md)
  A type for an event that indicates the closing of a pseudoterminal device.
- [struct es_event_pty_grant_t](es_event_pty_grant_t.md)
  A type for an event that indicates the granting of a pseudoterminal device to a user.

## See Also

- [Client](client.md)
  An opaque type that maintains Endpoint Security client state, and functions related to this type.
- [Message](message.md)
  A type used by Endpoint Security to notify your client when a monitored action occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/event-types)*