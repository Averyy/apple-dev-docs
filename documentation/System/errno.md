# Errno

**Framework**: System  
**Kind**: struct

An error number used by system calls to communicate what kind of error occurred.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@frozen
struct Errno
```

## Topics

### File and Directory Errors
- [static var attributeNotFound: Errno](errno/attributenotfound.md)
  Attribute not found.
- [static var badFileDescriptor: Errno](errno/badfiledescriptor.md)
  Bad file descriptor.
- [static var fileExists: Errno](errno/fileexists.md)
  File exists.
- [static var fileTooLarge: Errno](errno/filetoolarge.md)
  The file is too large.
- [static var improperLink: Errno](errno/improperlink.md)
  Improper link.
- [static var isDirectory: Errno](errno/isdirectory.md)
  Is a directory.
- [static var noLocks: Errno](errno/nolocks.md)
  No locks available.
- [static var noSuchFileOrDirectory: Errno](errno/nosuchfileordirectory.md)
  No such file or directory.
- [static var notDirectory: Errno](errno/notdirectory.md)
  Not a directory.
- [static var permissionDenied: Errno](errno/permissiondenied.md)
  Permission denied.
- [static var textFileBusy: Errno](errno/textfilebusy.md)
  Text file busy.
### File System Errors
- [static var badFileTypeOrFormat: Errno](errno/badfiletypeorformat.md)
  Inappropriate file type or format.
- [static var directoryNotEmpty: Errno](errno/directorynotempty.md)
  Directory not empty.
- [static var diskQuotaExceeded: Errno](errno/diskquotaexceeded.md)
  Disk quota exceeded.
- [static var noSpace: Errno](errno/nospace.md)
  Device out of space.
- [static var readOnlyFileSystem: Errno](errno/readonlyfilesystem.md)
  Read-only file system.
- [static var tooManyLinks: Errno](errno/toomanylinks.md)
  Too many links.
- [static var tooManyOpenFilesInSystem: Errno](errno/toomanyopenfilesinsystem.md)
  The system has too many open files.
- [static var tooManyOpenFiles: Errno](errno/toomanyopenfiles.md)
  This process has too many open files.
### NFS Errors
- [static var authenticationError: Errno](errno/authenticationerror.md)
  Authentication error.
- [static var needAuthenticator: Errno](errno/needauthenticator.md)
  Need authenticator.
- [static var staleNFSFileHandle: Errno](errno/stalenfsfilehandle.md)
  Stale NFS file handle.
### Device Errors
- [static var deviceError: Errno](errno/deviceerror.md)
  Device error.
- [static var devicePowerIsOff: Errno](errno/devicepowerisoff.md)
  Device power is off.
- [static var inappropriateIOCTLForDevice: Errno](errno/inappropriateioctlfordevice.md)
  Inappropriate control function.
- [static var ioError: Errno](errno/ioerror.md)
  Input/output error.
- [static var noSuchAddressOrDevice: Errno](errno/nosuchaddressordevice.md)
  No such device or address.
- [static var notBlockDevice: Errno](errno/notblockdevice.md)
  Not a block device.
- [static var operationNotSupportedByDevice: Errno](errno/operationnotsupportedbydevice.md)
  Operation not supported by device.
### Path Errors
- [static var fileNameTooLong: Errno](errno/filenametoolong.md)
  The file name is too long.
- [static var tooManyRemoteLevels: Errno](errno/toomanyremotelevels.md)
  Too many levels of remote in path.
- [static var tooManySymbolicLinkLevels: Errno](errno/toomanysymboliclinklevels.md)
  Too many levels of symbolic links.
### Pipe Errors
- [static var brokenPipe: Errno](errno/brokenpipe.md)
  Broken pipe.
- [static var illegalSeek: Errno](errno/illegalseek.md)
  Illegal seek.
### Runtime Errors
- [static var deadlock: Errno](errno/deadlock.md)
  Resource deadlock avoided.
- [static var noMemory: Errno](errno/nomemory.md)
  Can’t allocate memory.
- [static var wouldBlock: Errno](errno/wouldblock.md)
  Operation would block.
### Math Errors
- [static var outOfDomain: Errno](errno/outofdomain.md)
  Numerical argument out of domain.
- [static var outOfRange: Errno](errno/outofrange.md)
  Numerical result out of range.
- [static var overflow: Errno](errno/overflow.md)
  Value too large to be stored in data type.
### Executable File Errors
- [static var badCPUType: Errno](errno/badcputype.md)
  Bad CPU type in executable.
- [static var badExecutable: Errno](errno/badexecutable.md)
  Bad executable or shared library.
- [static var execFormatError: Errno](errno/execformaterror.md)
  Executable format error.
- [static var malformedMachO: Errno](errno/malformedmacho.md)
  Malformed Mach-O file.
- [static var sharedLibraryVersionMismatch: Errno](errno/sharedlibraryversionmismatch.md)
  Shared library version mismatch.
### Network Errors
- [static var connectionAbort: Errno](errno/connectionabort.md)
  Software caused a connection abort.
- [static var connectionRefused: Errno](errno/connectionrefused.md)
  Connection refused.
- [static var connectionReset: Errno](errno/connectionreset.md)
  Connection reset by peer.
- [static var hostIsDown: Errno](errno/hostisdown.md)
  The host is down.
- [static var messageTooLong: Errno](errno/messagetoolong.md)
  Message too long.
- [static var networkDown: Errno](errno/networkdown.md)
  Network is down.
- [static var networkReset: Errno](errno/networkreset.md)
  Network dropped connection on reset.
- [static var networkUnreachable: Errno](errno/networkunreachable.md)
  Network is unreachable.
- [static var noBufferSpace: Errno](errno/nobufferspace.md)
  No buffer space available.
- [static var noRouteToHost: Errno](errno/noroutetohost.md)
  No route to host.
- [static var notSupported: Errno](errno/notsupported.md)
  Not supported.
- [static var timedOut: Errno](errno/timedout.md)
  Operation timed out.
### Network Protocol Errors
- [static var protocolError: Errno](errno/protocolerror.md)
  Protocol error.
- [static var protocolFamilyNotSupported: Errno](errno/protocolfamilynotsupported.md)
  Protocol family not supported.
- [static var protocolNotAvailable: Errno](errno/protocolnotavailable.md)
  Protocol not available.
- [static var protocolNotSupported: Errno](errno/protocolnotsupported.md)
  Protocol not supported.
- [static var protocolWrongTypeForSocket: Errno](errno/protocolwrongtypeforsocket.md)
  Protocol wrong for socket type.
### Network Address Errors
- [static var addressFamilyNotSupported: Errno](errno/addressfamilynotsupported.md)
  The address family isn’t supported by the protocol family.
- [static var addressInUse: Errno](errno/addressinuse.md)
  Address already in use.
- [static var addressNotAvailable: Errno](errno/addressnotavailable.md)
  Can’t assign the requested address.
- [static var addressRequired: Errno](errno/addressrequired.md)
  Destination address required.
### Network Socket Errors
- [static var notSocket: Errno](errno/notsocket.md)
  A socket operation was performed on something that isn’t a socket.
- [static var notSupportedOnSocket: Errno](errno/notsupportedonsocket.md)
  Operation not supported on socket.
- [static var socketIsConnected: Errno](errno/socketisconnected.md)
  Socket is already connected.
- [static var socketNotConnected: Errno](errno/socketnotconnected.md)
  Socket is not connected.
- [static var socketShutdown: Errno](errno/socketshutdown.md)
  Can’t send after socket shutdown.
- [static var socketTypeNotSupported: Errno](errno/sockettypenotsupported.md)
  Socket type not supported.
### RPC Errors
- [static var rpcProcedureUnavailable: Errno](errno/rpcprocedureunavailable.md)
  Bad procedure for program.
- [static var rpcProgramUnavailable: Errno](errno/rpcprogramunavailable.md)
  The remote procedure call (RPC) program isn’t available.
- [static var rpcProgramVersionMismatch: Errno](errno/rpcprogramversionmismatch.md)
  The version of the remote procedure call (RPC) program is incorrect.
- [static var rpcUnsuccessful: Errno](errno/rpcunsuccessful.md)
  The structure of the remote procedure call (RPC) is bad.
- [static var rpcVersionMismatch: Errno](errno/rpcversionmismatch.md)
  The version of the remote procedure call (RPC) is incorrect.
### Process Errors
- [static var argListTooLong: Errno](errno/arglisttoolong.md)
  The argument list is too long.
- [static var identifierRemoved: Errno](errno/identifierremoved.md)
  Identifier removed.
- [static var noChildProcess: Errno](errno/nochildprocess.md)
  No child processes.
- [static var noSuchProcess: Errno](errno/nosuchprocess.md)
  No such process.
- [static var previousOwnerDied: Errno](errno/previousownerdied.md)
  Previous pthread mutex owner died.
- [static var tooManyProcesses: Errno](errno/toomanyprocesses.md)
  Too many processes.
### System Call Errors
- [static var alreadyInProcess: Errno](errno/alreadyinprocess.md)
  Operation already in progress.
- [static var badAddress: Errno](errno/badaddress.md)
  Bad address.
- [static var interrupted: Errno](errno/interrupted.md)
  Interrupted function call.
- [static var invalidArgument: Errno](errno/invalidargument.md)
  Invalid argument.
- [static var noFunction: Errno](errno/nofunction.md)
  Function not implemented.
- [static var nowInProgress: Errno](errno/nowinprogress.md)
  Operation now in progress.
- [static var resourceBusy: Errno](errno/resourcebusy.md)
  Resource busy.
- [static var resourceTemporarilyUnavailable: Errno](errno/resourcetemporarilyunavailable.md)
  Resource temporarily unavailable.
### General Errors
- [static var badMessage: Errno](errno/badmessage.md)
  Bad message.
- [static var canceled: Errno](errno/canceled.md)
  Operation canceled.
- [static var illegalByteSequence: Errno](errno/illegalbytesequence.md)
  Illegal byte sequence.
- [static var noData: Errno](errno/nodata.md)
  No message available.
- [static var noMessage: Errno](errno/nomessage.md)
  No message of desired type.
- [static var noSuchPolicy: Errno](errno/nosuchpolicy.md)
  No such policy registered.
- [static var notPermitted: Errno](errno/notpermitted.md)
  Operation not permitted.
- [static var notRecoverable: Errno](errno/notrecoverable.md)
  State not recoverable.
- [static var outputQueueFull: Errno](errno/outputqueuefull.md)
  Interface output queue is full.
- [static var tooManyReferences: Errno](errno/toomanyreferences.md)
  Too many references: can’t splice.
- [static var tooManyUsers: Errno](errno/toomanyusers.md)
  Too many users.
### Reserved
- [static var lastErrnoValue: Errno](errno/lasterrnovalue.md)
  The largest valid error.
- [static var multiHop: Errno](errno/multihop.md)
  Reserved.
- [static var noLink: Errno](errno/nolink.md)
  Reserved.
- [static var noStreamResources: Errno](errno/nostreamresources.md)
  Reserved.
- [static var notStream: Errno](errno/notstream.md)
  Reserved.
- [static var notUsed: Errno](errno/notused.md)
  Error. Not used.
- [static var timeout: Errno](errno/timeout.md)
  Reserved.
### Interacting with C APIs
- [init(rawValue: CInt)](errno/init(rawvalue:).md)
  Creates a strongly typed error number from a raw C error number.
- [let rawValue: CInt](errno/rawvalue-swift.property.md)
  The raw C error number.
- [typealias RawValue](errno/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Debugging
- [var description: String](errno/description.md)
  A textual representation of the most recent error returned by a system call.
- [var debugDescription: String](errno/debugdescription.md)
  A textual representation, suitable for debugging, of the most recent error returned by a system call.
### Encoding Errors
- [init(from: any Decoder) throws](errno/init(from:).md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int32`.
- [func encode(to: any Encoder) throws](errno/encode(to:).md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int32`.
### Comparing Errors
- [static func != (Self, Self) -> Bool](errno/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func ~= (Errno, any Error) -> Bool](errno/~=(_:_:).md)
- [func hash(into: inout Hasher)](errno/hash(into:).md)
- [var hashValue: Int](errno/hashvalue.md)
### Default Implementations
- [CustomDebugStringConvertible Implementations](errno/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](errno/customstringconvertible-implementations.md)
- [Equatable Implementations](errno/equatable-implementations.md)
- [RawRepresentable Implementations](errno/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno)*