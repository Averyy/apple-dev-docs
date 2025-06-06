# es_events_t

**Framework**: Endpoint Security  
**Kind**: struct

A C union of event-specific types.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_events_t
```

#### Overview

Each event monitored by Endpoint Security delivers different properties to clients. For example, a file-renaming event provides source and target paths, while a process-forking event provides the process identifier of the new child process. This C `union` represents each kind of event as a unique member, each with a type specific to the kind of data it contains.

## Topics

### File-System Events
- [var access: es_event_access_t](es_events_t/access.md)
  Properties of an event that indicates the checking of a file’s access permission.
- [var clone: es_event_clone_t](es_events_t/clone.md)
  Properties of an event that indicates the cloning of a file.
- [var copyfile: es_event_copyfile_t](es_events_t/copyfile.md)
  Properties of an event that indicates the cloning of a file.
- [var close: es_event_close_t](es_events_t/close.md)
  Properties of an event that indicates the closing of a file.
- [var create: es_event_create_t](es_events_t/create.md)
  Properties of an event that indicates the creation of a file.
- [var dup: es_event_dup_t](es_events_t/dup.md)
  Properties of an event that indicates the duplication of a file descriptor.
- [var exchangedata: es_event_exchangedata_t](es_events_t/exchangedata.md)
  Properties of an event that indicates the exchange of data between two files.
- [var fcntl: es_event_fcntl_t](es_events_t/fcntl.md)
  Properties of an event that indicates the manipulation of a file descriptor.
- [var open: es_event_open_t](es_events_t/open.md)
  Properties of an event that indicates the opening of a file.
- [var rename: es_event_rename_t](es_events_t/rename.md)
  Properties of an event that indicates the renaming of a file.
- [var write: es_event_write_t](es_events_t/write.md)
  Properties of an event that indicates the writing of data to a file.
- [var truncate: es_event_truncate_t](es_events_t/truncate.md)
  Properties of an event that indicates the truncation of a file.
- [var lookup: es_event_lookup_t](es_events_t/lookup.md)
  Properties of an event that indicates the lookup of a file’s path.
- [var searchfs: es_event_searchfs_t](es_events_t/searchfs.md)
  Properties of an event that indicates a search operation on a volume or mounted file system.
### File Metadata Events
- [var deleteextattr: es_event_deleteextattr_t](es_events_t/deleteextattr.md)
  Properties of an event that indicates the deletion of an extended attribute from a file.
- [var fsgetpath: es_event_fsgetpath_t](es_events_t/fsgetpath.md)
  Properties of an event that indicates the retrieval of a file-system path.
- [var getattrlist: es_event_getattrlist_t](es_events_t/getattrlist.md)
  Properties of an event that indicates the retrieval of attributes from a file.
- [var getextattr: es_event_getextattr_t](es_events_t/getextattr.md)
  Properties of an event that indicates the retrieval of an extended attribute from a file.
- [var listextattr: es_event_listextattr_t](es_events_t/listextattr.md)
  Properties of an event that indicates the retrieval of multiple extended attributes from a file.
- [var readdir: es_event_readdir_t](es_events_t/readdir.md)
  Properties of an event that indicates the reading of a file-system directory.
- [var setacl: es_event_setacl_t](es_events_t/setacl.md)
  Properties of an event that indicates the setting of a file’s access control list.
- [var setattrlist: es_event_setattrlist_t](es_events_t/setattrlist.md)
  Properties of an event that indicates the setting of an attribute of a file.
- [var setextattr: es_event_setextattr_t](es_events_t/setextattr.md)
  Properties of an event that indicates the setting of an extended attribute of a file.
- [var setflags: es_event_setflags_t](es_events_t/setflags.md)
  Properties of an event that indicates the setting of a file’s flags.
- [var setmode: es_event_setmode_t](es_events_t/setmode.md)
  Properties of an event that indicates the setting of a file’s mode.
- [var setowner: es_event_setowner_t](es_events_t/setowner.md)
  Properties of an event that indicates the setting of a file’s owner.
- [var stat: es_event_stat_t](es_events_t/stat.md)
  Properties of an event that indicates the retrieval of a file’s status.
- [var utimes: es_event_utimes_t](es_events_t/utimes.md)
  Properties of an event that indicates a change to a file’s access time or modification time.
### File Provider Events
- [var file_provider_materialize: es_event_file_provider_materialize_t](es_events_t/file_provider_materialize.md)
  Properties of an event that indicates the materialization of a file provider.
- [var file_provider_update: es_event_file_provider_update_t](es_events_t/file_provider_update.md)
  Properties of an event that indicates an update to a file provider.
### Symbolic Link Events
- [var link: es_event_link_t](es_events_t/link.md)
  Properties of an event that indicates the creation of a hard link.
- [var readlink: es_event_readlink_t](es_events_t/readlink.md)
  Properties of an event that indicates the reading of a symbolic link.
- [var unlink: es_event_unlink_t](es_events_t/unlink.md)
  Properties of an event that indicates the deletion of a file.
### File System Mounting Events
- [var mount: es_event_mount_t](es_events_t/mount.md)
  Properties of an event that indicates the mounting of a file system.
- [var unmount: es_event_unmount_t](es_events_t/unmount.md)
  Properties of an event that indicates the unmounting of a file system.
- [var remount: es_event_remount_t](es_events_t/remount.md)
  Properties of an event that indicates the remounting of a file system.
### Memory Mapping Events
- [var mmap: es_event_mmap_t](es_events_t/mmap.md)
  Properties of an event that indicates the mapping of memory to a file.
- [var mprotect: es_event_mprotect_t](es_events_t/mprotect.md)
  Properties of an event that indicates a change to protection of memory-mapped pages.
### Process Events
- [var chdir: es_event_chdir_t](es_events_t/chdir.md)
  Properties of an event that indicates a change to a process’s working directory.
- [var chroot: es_event_chroot_t](es_events_t/chroot.md)
  Properties of an event that indicates a change to a process’s root directory.
- [var exec: es_event_exec_t](es_events_t/exec.md)
  Properties of an event that indicates the execution of a process.
- [var fork: es_event_fork_t](es_events_t/fork.md)
  Properties of an event that indicates the forking of a process.
- [var proc_check: es_event_proc_check_t](es_events_t/proc_check.md)
  Properties of an event that indicate the retrieval of process information.
- [var signal: es_event_signal_t](es_events_t/signal.md)
  Properties of an event that indicates the sending of a signal to a process.
- [var exit: es_event_exit_t](es_events_t/exit.md)
  Properties of an event that indicates a process exiting.
### Interprocess Events
- [var proc_suspend_resume: es_event_proc_suspend_resume_t](es_events_t/proc_suspend_resume.md)
  Properties of an event that indicates a call to suspend, resume, or shut down sockets for a process.
- [var trace: es_event_trace_t](es_events_t/trace.md)
  Properties of an event that indicates an attempt by one process to attach to another.
- [var remote_thread_create: es_event_remote_thread_create_t](es_events_t/remote_thread_create.md)
  Properties of an event that indicates an attempt by one process to spawn a thread in another.
### Task Port Events
- [var get_task: es_event_get_task_t](es_events_t/get_task.md)
  Properties of an event that indicates the retrieval of a task’s control port.
- [var get_task_read: es_event_get_task_read_t](es_events_t/get_task_read.md)
  Properties of an event that indicates the retrieval of a task’s read port.
- [var get_task_inspect: es_event_get_task_inspect_t](es_events_t/get_task_inspect.md)
  Properties of an event that indicates the retrieval of a task’s inspect port.
- [var get_task_name: es_event_get_task_name_t](es_events_t/get_task_name.md)
  Properties of an event that indicates the retrieval of a task’s name port.
### User and Group ID Events
- [var setuid: es_event_setuid_t](es_events_t/setuid.md)
  Properties of an event that indicates a change to a process’s user ID.
- [var setgid: es_event_setgid_t](es_events_t/setgid.md)
  Properties of an event that indicates a change to a process’s group ID.
- [var seteuid: es_event_seteuid_t](es_events_t/seteuid.md)
  Properties of an event that indicates a change to a process’s effective user ID.
- [var setegid: es_event_setegid_t](es_events_t/setegid.md)
  Properties of an event that indicates a change to a process’s effective group ID.
- [var setreuid: es_event_setreuid_t](es_events_t/setreuid.md)
  Properties of an event that indicates a change to a process’s real and effective user IDs.
- [var setregid: es_event_setregid_t](es_events_t/setregid.md)
  Properties of an event that indicates a change to a process’s real and effective group IDs.
### Code Signing Events
- [var cs_invalidated: es_event_cs_invalidated_t](es_events_t/cs_invalidated.md)
  Properties of an event that indicates the invalidation of a process’s code signing status.
### Socket Events
- [var uipc_bind: es_event_uipc_bind_t](es_events_t/uipc_bind.md)
  Properties of an event that indicates the binding of a socket to a path.
- [var uipc_connect: es_event_uipc_connect_t](es_events_t/uipc_connect.md)
  Properties of an event that indicates the connection of a socket.
### Clock Events
- [var settime: es_event_settime_t](es_events_t/settime.md)
  Properties of an event that indicates the modification of the system time.
### Kernel Events
- [var iokit_open: es_event_iokit_open_t](es_events_t/iokit_open.md)
  Properties of an event that indicates the opening of an IOKit device.
- [var kextload: es_event_kextload_t](es_events_t/kextload.md)
  Properties of an event that indicates the loading of a Kernel Extension (KEXT).
- [var kextunload: es_event_kextunload_t](es_events_t/kextunload.md)
  Properties of an event that indicates the unloading of a Kernel Extension (KEXT).
### Pseudoterminal Events
- [var pty_close: es_event_pty_close_t](es_events_t/pty_close.md)
  Properties of the event that indicates the closing of a pseudoterminal device.
- [var pty_grant: es_event_pty_grant_t](es_events_t/pty_grant.md)
  Properties of the event that indicates the granting of a pseudoterminal device to a user.
### Initializers
- [init(access: es_event_access_t)](es_events_t/init(access:).md)
- [init(authentication: UnsafeMutablePointer<es_event_authentication_t>)](es_events_t/init(authentication:).md)
- [init(authorization_judgement: UnsafeMutablePointer<es_event_authorization_judgement_t>)](es_events_t/init(authorization_judgement:).md)
- [init(authorization_petition: UnsafeMutablePointer<es_event_authorization_petition_t>)](es_events_t/init(authorization_petition:).md)
- [init(btm_launch_item_add: UnsafeMutablePointer<es_event_btm_launch_item_add_t>)](es_events_t/init(btm_launch_item_add:).md)
- [init(btm_launch_item_remove: UnsafeMutablePointer<es_event_btm_launch_item_remove_t>)](es_events_t/init(btm_launch_item_remove:).md)
- [init(chdir: es_event_chdir_t)](es_events_t/init(chdir:).md)
- [init(chroot: es_event_chroot_t)](es_events_t/init(chroot:).md)
- [init(clone: es_event_clone_t)](es_events_t/init(clone:).md)
- [init(close: es_event_close_t)](es_events_t/init(close:).md)
- [init(copyfile: es_event_copyfile_t)](es_events_t/init(copyfile:).md)
- [init(create: es_event_create_t)](es_events_t/init(create:).md)
- [init(cs_invalidated: es_event_cs_invalidated_t)](es_events_t/init(cs_invalidated:).md)
- [init(deleteextattr: es_event_deleteextattr_t)](es_events_t/init(deleteextattr:).md)
- [init(dup: es_event_dup_t)](es_events_t/init(dup:).md)
- [init(exchangedata: es_event_exchangedata_t)](es_events_t/init(exchangedata:).md)
- [init(exec: es_event_exec_t)](es_events_t/init(exec:).md)
- [init(exit: es_event_exit_t)](es_events_t/init(exit:).md)
- [init(fcntl: es_event_fcntl_t)](es_events_t/init(fcntl:).md)
- [init(file_provider_materialize: es_event_file_provider_materialize_t)](es_events_t/init(file_provider_materialize:).md)
- [init(file_provider_update: es_event_file_provider_update_t)](es_events_t/init(file_provider_update:).md)
- [init(fork: es_event_fork_t)](es_events_t/init(fork:).md)
- [init(fsgetpath: es_event_fsgetpath_t)](es_events_t/init(fsgetpath:).md)
- [init(gatekeeper_user_override: UnsafeMutablePointer<es_event_gatekeeper_user_override_t>)](es_events_t/init(gatekeeper_user_override:).md)
- [init(get_task: es_event_get_task_t)](es_events_t/init(get_task:).md)
- [init(get_task_inspect: es_event_get_task_inspect_t)](es_events_t/init(get_task_inspect:).md)
- [init(get_task_name: es_event_get_task_name_t)](es_events_t/init(get_task_name:).md)
- [init(get_task_read: es_event_get_task_read_t)](es_events_t/init(get_task_read:).md)
- [init(getattrlist: es_event_getattrlist_t)](es_events_t/init(getattrlist:).md)
- [init(getextattr: es_event_getextattr_t)](es_events_t/init(getextattr:).md)
- [init(iokit_open: es_event_iokit_open_t)](es_events_t/init(iokit_open:).md)
- [init(kextload: es_event_kextload_t)](es_events_t/init(kextload:).md)
- [init(kextunload: es_event_kextunload_t)](es_events_t/init(kextunload:).md)
- [init(link: es_event_link_t)](es_events_t/init(link:).md)
- [init(listextattr: es_event_listextattr_t)](es_events_t/init(listextattr:).md)
- [init(login_login: UnsafeMutablePointer<es_event_login_login_t>)](es_events_t/init(login_login:).md)
- [init(login_logout: UnsafeMutablePointer<es_event_login_logout_t>)](es_events_t/init(login_logout:).md)
- [init(lookup: es_event_lookup_t)](es_events_t/init(lookup:).md)
- [init(lw_session_lock: UnsafeMutablePointer<es_event_lw_session_lock_t>)](es_events_t/init(lw_session_lock:).md)
- [init(lw_session_login: UnsafeMutablePointer<es_event_lw_session_login_t>)](es_events_t/init(lw_session_login:).md)
- [init(lw_session_logout: UnsafeMutablePointer<es_event_lw_session_logout_t>)](es_events_t/init(lw_session_logout:).md)
- [init(lw_session_unlock: UnsafeMutablePointer<es_event_lw_session_unlock_t>)](es_events_t/init(lw_session_unlock:).md)
- [init(mmap: es_event_mmap_t)](es_events_t/init(mmap:).md)
- [init(mount: es_event_mount_t)](es_events_t/init(mount:).md)
- [init(mprotect: es_event_mprotect_t)](es_events_t/init(mprotect:).md)
- [init(od_attribute_set: UnsafeMutablePointer<es_event_od_attribute_set_t>)](es_events_t/init(od_attribute_set:).md)
- [init(od_attribute_value_add: UnsafeMutablePointer<es_event_od_attribute_value_add_t>)](es_events_t/init(od_attribute_value_add:).md)
- [init(od_attribute_value_remove: UnsafeMutablePointer<es_event_od_attribute_value_remove_t>)](es_events_t/init(od_attribute_value_remove:).md)
- [init(od_create_group: UnsafeMutablePointer<es_event_od_create_group_t>)](es_events_t/init(od_create_group:).md)
- [init(od_create_user: UnsafeMutablePointer<es_event_od_create_user_t>)](es_events_t/init(od_create_user:).md)
- [init(od_delete_group: UnsafeMutablePointer<es_event_od_delete_group_t>)](es_events_t/init(od_delete_group:).md)
- [init(od_delete_user: UnsafeMutablePointer<es_event_od_delete_user_t>)](es_events_t/init(od_delete_user:).md)
- [init(od_disable_user: UnsafeMutablePointer<es_event_od_disable_user_t>)](es_events_t/init(od_disable_user:).md)
- [init(od_enable_user: UnsafeMutablePointer<es_event_od_enable_user_t>)](es_events_t/init(od_enable_user:).md)
- [init(od_group_add: UnsafeMutablePointer<es_event_od_group_add_t>)](es_events_t/init(od_group_add:).md)
- [init(od_group_remove: UnsafeMutablePointer<es_event_od_group_remove_t>)](es_events_t/init(od_group_remove:).md)
- [init(od_group_set: UnsafeMutablePointer<es_event_od_group_set_t>)](es_events_t/init(od_group_set:).md)
- [init(od_modify_password: UnsafeMutablePointer<es_event_od_modify_password_t>)](es_events_t/init(od_modify_password:).md)
- [init(open: es_event_open_t)](es_events_t/init(open:).md)
- [init(openssh_login: UnsafeMutablePointer<es_event_openssh_login_t>)](es_events_t/init(openssh_login:).md)
- [init(openssh_logout: UnsafeMutablePointer<es_event_openssh_logout_t>)](es_events_t/init(openssh_logout:).md)
- [init(proc_check: es_event_proc_check_t)](es_events_t/init(proc_check:).md)
- [init(proc_suspend_resume: es_event_proc_suspend_resume_t)](es_events_t/init(proc_suspend_resume:).md)
- [init(profile_add: UnsafeMutablePointer<es_event_profile_add_t>)](es_events_t/init(profile_add:).md)
- [init(profile_remove: UnsafeMutablePointer<es_event_profile_remove_t>)](es_events_t/init(profile_remove:).md)
- [init(pty_close: es_event_pty_close_t)](es_events_t/init(pty_close:).md)
- [init(pty_grant: es_event_pty_grant_t)](es_events_t/init(pty_grant:).md)
- [init(readdir: es_event_readdir_t)](es_events_t/init(readdir:).md)
- [init(readlink: es_event_readlink_t)](es_events_t/init(readlink:).md)
- [init(remote_thread_create: es_event_remote_thread_create_t)](es_events_t/init(remote_thread_create:).md)
- [init(remount: es_event_remount_t)](es_events_t/init(remount:).md)
- [init(rename: es_event_rename_t)](es_events_t/init(rename:).md)
- [init(screensharing_attach: UnsafeMutablePointer<es_event_screensharing_attach_t>)](es_events_t/init(screensharing_attach:).md)
- [init(screensharing_detach: UnsafeMutablePointer<es_event_screensharing_detach_t>)](es_events_t/init(screensharing_detach:).md)
- [init(searchfs: es_event_searchfs_t)](es_events_t/init(searchfs:).md)
- [init(setacl: es_event_setacl_t)](es_events_t/init(setacl:).md)
- [init(setattrlist: es_event_setattrlist_t)](es_events_t/init(setattrlist:).md)
- [init(setegid: es_event_setegid_t)](es_events_t/init(setegid:).md)
- [init(seteuid: es_event_seteuid_t)](es_events_t/init(seteuid:).md)
- [init(setextattr: es_event_setextattr_t)](es_events_t/init(setextattr:).md)
- [init(setflags: es_event_setflags_t)](es_events_t/init(setflags:).md)
- [init(setgid: es_event_setgid_t)](es_events_t/init(setgid:).md)
- [init(setmode: es_event_setmode_t)](es_events_t/init(setmode:).md)
- [init(setowner: es_event_setowner_t)](es_events_t/init(setowner:).md)
- [init(setregid: es_event_setregid_t)](es_events_t/init(setregid:).md)
- [init(setreuid: es_event_setreuid_t)](es_events_t/init(setreuid:).md)
- [init(settime: es_event_settime_t)](es_events_t/init(settime:).md)
- [init(setuid: es_event_setuid_t)](es_events_t/init(setuid:).md)
- [init(signal: es_event_signal_t)](es_events_t/init(signal:).md)
- [init(stat: es_event_stat_t)](es_events_t/init(stat:).md)
- [init(su: UnsafeMutablePointer<es_event_su_t>)](es_events_t/init(su:).md)
- [init(sudo: UnsafeMutablePointer<es_event_sudo_t>)](es_events_t/init(sudo:).md)
- [init(tcc_modify: UnsafeMutablePointer<es_event_tcc_modify_t>)](es_events_t/init(tcc_modify:).md)
- [init(trace: es_event_trace_t)](es_events_t/init(trace:).md)
- [init(truncate: es_event_truncate_t)](es_events_t/init(truncate:).md)
- [init(uipc_bind: es_event_uipc_bind_t)](es_events_t/init(uipc_bind:).md)
- [init(uipc_connect: es_event_uipc_connect_t)](es_events_t/init(uipc_connect:).md)
- [init(unlink: es_event_unlink_t)](es_events_t/init(unlink:).md)
- [init(unmount: es_event_unmount_t)](es_events_t/init(unmount:).md)
- [init(utimes: es_event_utimes_t)](es_events_t/init(utimes:).md)
- [init(write: es_event_write_t)](es_events_t/init(write:).md)
- [init(xp_malware_detected: UnsafeMutablePointer<es_event_xp_malware_detected_t>)](es_events_t/init(xp_malware_detected:).md)
- [init(xp_malware_remediated: UnsafeMutablePointer<es_event_xp_malware_remediated_t>)](es_events_t/init(xp_malware_remediated:).md)
- [init(xpc_connect: UnsafeMutablePointer<es_event_xpc_connect_t>)](es_events_t/init(xpc_connect:).md)
### Instance Properties
- [var authentication: UnsafeMutablePointer<es_event_authentication_t>](es_events_t/authentication.md)
- [var authorization_judgement: UnsafeMutablePointer<es_event_authorization_judgement_t>](es_events_t/authorization_judgement.md)
- [var authorization_petition: UnsafeMutablePointer<es_event_authorization_petition_t>](es_events_t/authorization_petition.md)
- [var btm_launch_item_add: UnsafeMutablePointer<es_event_btm_launch_item_add_t>](es_events_t/btm_launch_item_add.md)
- [var btm_launch_item_remove: UnsafeMutablePointer<es_event_btm_launch_item_remove_t>](es_events_t/btm_launch_item_remove.md)
- [var gatekeeper_user_override: UnsafeMutablePointer<es_event_gatekeeper_user_override_t>](es_events_t/gatekeeper_user_override.md)
- [var login_login: UnsafeMutablePointer<es_event_login_login_t>](es_events_t/login_login.md)
- [var login_logout: UnsafeMutablePointer<es_event_login_logout_t>](es_events_t/login_logout.md)
- [var lw_session_lock: UnsafeMutablePointer<es_event_lw_session_lock_t>](es_events_t/lw_session_lock.md)
- [var lw_session_login: UnsafeMutablePointer<es_event_lw_session_login_t>](es_events_t/lw_session_login.md)
- [var lw_session_logout: UnsafeMutablePointer<es_event_lw_session_logout_t>](es_events_t/lw_session_logout.md)
- [var lw_session_unlock: UnsafeMutablePointer<es_event_lw_session_unlock_t>](es_events_t/lw_session_unlock.md)
- [var od_attribute_set: UnsafeMutablePointer<es_event_od_attribute_set_t>](es_events_t/od_attribute_set.md)
- [var od_attribute_value_add: UnsafeMutablePointer<es_event_od_attribute_value_add_t>](es_events_t/od_attribute_value_add.md)
- [var od_attribute_value_remove: UnsafeMutablePointer<es_event_od_attribute_value_remove_t>](es_events_t/od_attribute_value_remove.md)
- [var od_create_group: UnsafeMutablePointer<es_event_od_create_group_t>](es_events_t/od_create_group.md)
- [var od_create_user: UnsafeMutablePointer<es_event_od_create_user_t>](es_events_t/od_create_user.md)
- [var od_delete_group: UnsafeMutablePointer<es_event_od_delete_group_t>](es_events_t/od_delete_group.md)
- [var od_delete_user: UnsafeMutablePointer<es_event_od_delete_user_t>](es_events_t/od_delete_user.md)
- [var od_disable_user: UnsafeMutablePointer<es_event_od_disable_user_t>](es_events_t/od_disable_user.md)
- [var od_enable_user: UnsafeMutablePointer<es_event_od_enable_user_t>](es_events_t/od_enable_user.md)
- [var od_group_add: UnsafeMutablePointer<es_event_od_group_add_t>](es_events_t/od_group_add.md)
- [var od_group_remove: UnsafeMutablePointer<es_event_od_group_remove_t>](es_events_t/od_group_remove.md)
- [var od_group_set: UnsafeMutablePointer<es_event_od_group_set_t>](es_events_t/od_group_set.md)
- [var od_modify_password: UnsafeMutablePointer<es_event_od_modify_password_t>](es_events_t/od_modify_password.md)
- [var openssh_login: UnsafeMutablePointer<es_event_openssh_login_t>](es_events_t/openssh_login.md)
- [var openssh_logout: UnsafeMutablePointer<es_event_openssh_logout_t>](es_events_t/openssh_logout.md)
- [var profile_add: UnsafeMutablePointer<es_event_profile_add_t>](es_events_t/profile_add.md)
- [var profile_remove: UnsafeMutablePointer<es_event_profile_remove_t>](es_events_t/profile_remove.md)
- [var screensharing_attach: UnsafeMutablePointer<es_event_screensharing_attach_t>](es_events_t/screensharing_attach.md)
- [var screensharing_detach: UnsafeMutablePointer<es_event_screensharing_detach_t>](es_events_t/screensharing_detach.md)
- [var su: UnsafeMutablePointer<es_event_su_t>](es_events_t/su.md)
- [var sudo: UnsafeMutablePointer<es_event_sudo_t>](es_events_t/sudo.md)
- [var tcc_modify: UnsafeMutablePointer<es_event_tcc_modify_t>](es_events_t/tcc_modify.md)
- [var xp_malware_detected: UnsafeMutablePointer<es_event_xp_malware_detected_t>](es_events_t/xp_malware_detected.md)
- [var xp_malware_remediated: UnsafeMutablePointer<es_event_xp_malware_remediated_t>](es_events_t/xp_malware_remediated.md)
- [var xpc_connect: UnsafeMutablePointer<es_event_xpc_connect_t>](es_events_t/xpc_connect.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [var event: es_events_t](es_message_t/event.md)
  The event that triggered this message.
- [var event_type: es_event_type_t](es_message_t/event_type.md)
  The type of the message’s event.
- [struct es_event_type_t](es_event_type_t.md)
  A type used to identify a message’s event type and subscribe to events of that type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_events_t)*