# POSIXError

**Framework**: Foundation  
**Kind**: struct

Describes an error in the POSIX error domain.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct POSIXError
```

## Topics

### Type Aliases
- [POSIXError.Code](posixerror/code.md)
  The type of an error code.
### Type Properties
- [static var E2BIG: POSIXErrorCode](posixerror/e2big.md)
  Argument list too long.
- [static var EACCES: POSIXErrorCode](posixerror/eacces.md)
  Permission denied.
- [static var EADDRINUSE: POSIXErrorCode](posixerror/eaddrinuse.md)
  Address already in use.
- [static var EADDRNOTAVAIL: POSIXErrorCode](posixerror/eaddrnotavail.md)
  Can’t assign requested address.
- [static var EAFNOSUPPORT: POSIXErrorCode](posixerror/eafnosupport.md)
  Address family not supported by protocol family.
- [static var EAGAIN: POSIXErrorCode](posixerror/eagain.md)
  non-blocking and interrupt i/o. Resource temporarily unavailable.
- [static var EALREADY: POSIXErrorCode](posixerror/ealready.md)
  Operation already in progress.
- [static var EAUTH: POSIXErrorCode](posixerror/eauth.md)
  Authentication error.
- [static var EBADARCH: POSIXErrorCode](posixerror/ebadarch.md)
  Bad CPU type in executable.
- [static var EBADEXEC: POSIXErrorCode](posixerror/ebadexec.md)
  Program loading errors. Bad executable.
- [static var EBADF: POSIXErrorCode](posixerror/ebadf.md)
  Bad file descriptor.
- [static var EBADMACHO: POSIXErrorCode](posixerror/ebadmacho.md)
  Malformed Macho file.
- [static var EBADMSG: POSIXErrorCode](posixerror/ebadmsg.md)
  Bad message.
- [static var EBADRPC: POSIXErrorCode](posixerror/ebadrpc.md)
  RPC struct is bad.
- [static var EBUSY: POSIXErrorCode](posixerror/ebusy.md)
  Device / Resource busy.
- [static var ECANCELED: POSIXErrorCode](posixerror/ecanceled.md)
  Operation canceled.
- [static var ECHILD: POSIXErrorCode](posixerror/echild.md)
  No child processes.
- [static var ECONNABORTED: POSIXErrorCode](posixerror/econnaborted.md)
  Software caused connection abort.
- [static var ECONNREFUSED: POSIXErrorCode](posixerror/econnrefused.md)
  Connection refused.
- [static var ECONNRESET: POSIXErrorCode](posixerror/econnreset.md)
  Connection reset by peer.
- [static var EDEADLK: POSIXErrorCode](posixerror/edeadlk.md)
  Resource deadlock avoided.
- [static var EDESTADDRREQ: POSIXErrorCode](posixerror/edestaddrreq.md)
  Destination address required.
- [static var EDEVERR: POSIXErrorCode](posixerror/edeverr.md)
  Device error, for example paper out.
- [static var EDOM: POSIXErrorCode](posixerror/edom.md)
  math software. Numerical argument out of domain.
- [static var EDQUOT: POSIXErrorCode](posixerror/edquot.md)
  Disc quota exceeded.
- [static var EEXIST: POSIXErrorCode](posixerror/eexist.md)
  File exists.
- [static var EFAULT: POSIXErrorCode](posixerror/efault.md)
  Bad address.
- [static var EFBIG: POSIXErrorCode](posixerror/efbig.md)
  File too large.
- [static var EFTYPE: POSIXErrorCode](posixerror/eftype.md)
  Inappropriate file type or format.
- [static var EHOSTDOWN: POSIXErrorCode](posixerror/ehostdown.md)
  Host is down.
- [static var EHOSTUNREACH: POSIXErrorCode](posixerror/ehostunreach.md)
  No route to host.
- [static var EIDRM: POSIXErrorCode](posixerror/eidrm.md)
  Identifier removed.
- [static var EILSEQ: POSIXErrorCode](posixerror/eilseq.md)
  Illegal byte sequence.
- [static var EINPROGRESS: POSIXErrorCode](posixerror/einprogress.md)
  Operation now in progress.
- [static var EINTR: POSIXErrorCode](posixerror/eintr.md)
  Interrupted system call.
- [static var EINVAL: POSIXErrorCode](posixerror/einval.md)
  Invalid argument.
- [static var EIO: POSIXErrorCode](posixerror/eio.md)
  Input/output error.
- [static var EISCONN: POSIXErrorCode](posixerror/eisconn.md)
  Socket is already connected.
- [static var EISDIR: POSIXErrorCode](posixerror/eisdir.md)
  Is a directory.
- [static var ELOOP: POSIXErrorCode](posixerror/eloop.md)
  Too many levels of symbolic links.
- [static var EMFILE: POSIXErrorCode](posixerror/emfile.md)
  Too many open files.
- [static var EMLINK: POSIXErrorCode](posixerror/emlink.md)
  Too many links.
- [static var EMSGSIZE: POSIXErrorCode](posixerror/emsgsize.md)
  Message too long.
- [static var EMULTIHOP: POSIXErrorCode](posixerror/emultihop.md)
  Reserved.
- [static var ENAMETOOLONG: POSIXErrorCode](posixerror/enametoolong.md)
  File name too long.
- [static var ENEEDAUTH: POSIXErrorCode](posixerror/eneedauth.md)
  Need authenticator.
- [static var ENETDOWN: POSIXErrorCode](posixerror/enetdown.md)
  ipc/network software – operational errors Network is down.
- [static var ENETRESET: POSIXErrorCode](posixerror/enetreset.md)
  Network dropped connection on reset.
- [static var ENETUNREACH: POSIXErrorCode](posixerror/enetunreach.md)
  Network is unreachable.
- [static var ENFILE: POSIXErrorCode](posixerror/enfile.md)
  Too many open files in system.
- [static var ENOATTR: POSIXErrorCode](posixerror/enoattr.md)
  Attribute not found.
- [static var ENOBUFS: POSIXErrorCode](posixerror/enobufs.md)
  No buffer space available.
- [static var ENODATA: POSIXErrorCode](posixerror/enodata.md)
  No message available on STREAM.
- [static var ENODEV: POSIXErrorCode](posixerror/enodev.md)
  Operation not supported by device.
- [static var ENOENT: POSIXErrorCode](posixerror/enoent.md)
  No such file or directory.
- [static var ENOEXEC: POSIXErrorCode](posixerror/enoexec.md)
  Exec format error.
- [static var ENOLCK: POSIXErrorCode](posixerror/enolck.md)
  No locks available.
- [static var ENOLINK: POSIXErrorCode](posixerror/enolink.md)
  Reserved.
- [static var ENOMEM: POSIXErrorCode](posixerror/enomem.md)
  Cannot allocate memory.
- [static var ENOMSG: POSIXErrorCode](posixerror/enomsg.md)
  No message of desired type.
- [static var ENOPOLICY: POSIXErrorCode](posixerror/enopolicy.md)
  No such policy registered.
- [static var ENOPROTOOPT: POSIXErrorCode](posixerror/enoprotoopt.md)
  Protocol not available.
- [static var ENOSPC: POSIXErrorCode](posixerror/enospc.md)
  No space left on device.
- [static var ENOSR: POSIXErrorCode](posixerror/enosr.md)
  No STREAM resources.
- [static var ENOSTR: POSIXErrorCode](posixerror/enostr.md)
  Not a STREAM.
- [static var ENOSYS: POSIXErrorCode](posixerror/enosys.md)
  Function not implemented.
- [static var ENOTBLK: POSIXErrorCode](posixerror/enotblk.md)
  Block device required.
- [static var ENOTCONN: POSIXErrorCode](posixerror/enotconn.md)
  Socket is not connected.
- [static var ENOTDIR: POSIXErrorCode](posixerror/enotdir.md)
  Not a directory.
- [static var ENOTEMPTY: POSIXErrorCode](posixerror/enotempty.md)
  Directory not empty.
- [static var ENOTRECOVERABLE: POSIXErrorCode](posixerror/enotrecoverable.md)
  State not recoverable.
- [static var ENOTSOCK: POSIXErrorCode](posixerror/enotsock.md)
  ipc/network software – argument errors. Socket operation on non-socket.
- [static var ENOTSUP: POSIXErrorCode](posixerror/enotsup.md)
  Operation not supported.
- [static var ENOTTY: POSIXErrorCode](posixerror/enotty.md)
  Inappropriate ioctl for device.
- [static var ENXIO: POSIXErrorCode](posixerror/enxio.md)
  Device not configured.
- [static var EOVERFLOW: POSIXErrorCode](posixerror/eoverflow.md)
  Value too large to be stored in data type.
- [static var EOWNERDEAD: POSIXErrorCode](posixerror/eownerdead.md)
  Previous owner died.
- [static var EPERM: POSIXErrorCode](posixerror/eperm.md)
  Operation not permitted.
- [static var EPFNOSUPPORT: POSIXErrorCode](posixerror/epfnosupport.md)
  Protocol family not supported.
- [static var EPIPE: POSIXErrorCode](posixerror/epipe.md)
  Broken pipe.
- [static var EPROCLIM: POSIXErrorCode](posixerror/eproclim.md)
  quotas & mush. Too many processes.
- [static var EPROCUNAVAIL: POSIXErrorCode](posixerror/eprocunavail.md)
  Bad procedure for program.
- [static var EPROGMISMATCH: POSIXErrorCode](posixerror/eprogmismatch.md)
  Program version wrong.
- [static var EPROGUNAVAIL: POSIXErrorCode](posixerror/eprogunavail.md)
  RPC prog. not avail.
- [static var EPROTO: POSIXErrorCode](posixerror/eproto.md)
  Protocol error.
- [static var EPROTONOSUPPORT: POSIXErrorCode](posixerror/eprotonosupport.md)
  Protocol not supported.
- [static var EPROTOTYPE: POSIXErrorCode](posixerror/eprototype.md)
  Protocol wrong type for socket.
- [static var EPWROFF: POSIXErrorCode](posixerror/epwroff.md)
  Intelligent device errors. Device power is off.
- [static var EQFULL: POSIXErrorCode](posixerror/eqfull.md)
  Interface output queue is full.
- [static var ERANGE: POSIXErrorCode](posixerror/erange.md)
  Result too large.
- [static var EREMOTE: POSIXErrorCode](posixerror/eremote.md)
  Too many levels of remote in path.
- [static var EROFS: POSIXErrorCode](posixerror/erofs.md)
  Read-only file system.
- [static var ERPCMISMATCH: POSIXErrorCode](posixerror/erpcmismatch.md)
  RPC version wrong.
- [static var ESHLIBVERS: POSIXErrorCode](posixerror/eshlibvers.md)
  Shared library version mismatch.
- [static var ESHUTDOWN: POSIXErrorCode](posixerror/eshutdown.md)
  Can’t send after socket shutdown.
- [static var ESOCKTNOSUPPORT: POSIXErrorCode](posixerror/esocktnosupport.md)
  Socket type not supported.
- [static var ESPIPE: POSIXErrorCode](posixerror/espipe.md)
  Illegal seek.
- [static var ESRCH: POSIXErrorCode](posixerror/esrch.md)
  No such process.
- [static var ESTALE: POSIXErrorCode](posixerror/estale.md)
  Network File System. Stale NFS file handle.
- [static var ETIME: POSIXErrorCode](posixerror/etime.md)
  STREAM ioctl timeout.
- [static var ETIMEDOUT: POSIXErrorCode](posixerror/etimedout.md)
  Operation timed out.
- [static var ETOOMANYREFS: POSIXErrorCode](posixerror/etoomanyrefs.md)
  Too many references: can’t splice.
- [static var ETXTBSY: POSIXErrorCode](posixerror/etxtbsy.md)
  Text file busy.
- [static var EUSERS: POSIXErrorCode](posixerror/eusers.md)
  Too many users.
- [static var EWOULDBLOCK: POSIXErrorCode](posixerror/ewouldblock.md)
  Operation would block.
- [static var EXDEV: POSIXErrorCode](posixerror/exdev.md)
  Cross-device link.

## Relationships

### Conforms To
- [CustomNSError](customnserror.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CocoaError](cocoaerror.md)
  Describes errors within the Cocoa error domain.
- [struct MachError](macherror.md)
  Describes an error in the Mach error domain.
- [NSError Codes](1448136-nserror-codes.md)
  Error codes in the Cocoa error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/posixerror)*