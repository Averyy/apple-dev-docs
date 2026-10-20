# CFHostGetNames(_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Gets the names from a CFHost.

**Availability**:
- iOS 2.0+ - Deprecated in 27.0
- iPadOS 2.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.3+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network framework instead, see deprecation notice in <CFNetwork/CFHost.h>

## Declaration

```swift
func CFHostGetNames(_ theHost: CFHost, _ hasBeenResolved: UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFArray>?
```

```c
extern CFArrayRefCFHostGetNames(CFHostRef theHost, Boolean *hasBeenResolved);
```

#### Return Value

An array containing the of names of `theHost`, or `NULL` if no names were available.

#### Discussion

This function gets the names in a thread-safe way, but the resulting data is not thread-safe. The data is returned as a “get” as opposed to a copy, so the data is not safe if the CFHost is altered from another thread.

## Parameters

- `theHost`: The host to examine. The host must have been previously resolved. (To resolve a host, call [`CFHostStartInfoResolution(_:_:_:)`](./cfhoststartinforesolution%28_,_,_%29.md).) This value must not be `NULL`.
- `hasBeenResolved`: On return, contains `TRUE` if names were available, otherwise `FALSE`. This value may be `NULL`.

## See Also

### Hosts
- [class CFHost](./cfhost.md)
  An opaque reference representing an CFHost object.
- [enum CFHostInfoType](./cfhostinfotype.md)
  Values indicating the type of data that is to be resolved or the type of data that was resolved.
- [struct CFHostClientContext](./cfhostclientcontext.md)
  A structure containing user-defined data and callbacks for CFHost objects.
- [func CFHostCancelInfoResolution(CFHost, CFHostInfoType)](./cfhostcancelinforesolution%28_,_%29.md)
  Cancels the resolution of a host.
- [func CFHostCreateCopy(CFAllocator?, CFHost) -> Unmanaged<CFHost>](./cfhostcreatecopy%28_,_%29.md)
  Creates a new host object by copying.
- [func CFHostCreateWithAddress(CFAllocator?, CFData) -> Unmanaged<CFHost>](./cfhostcreatewithaddress%28_,_%29.md)
  Uses an address to create an instance of a host object.
- [func CFHostCreateWithName(CFAllocator?, CFString) -> Unmanaged<CFHost>](./cfhostcreatewithname%28_,_%29.md)
  Uses a name to create an instance of a host object.
- [func CFHostGetAddressing(CFHost, UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFArray>?](./cfhostgetaddressing%28_,_%29.md)
  Gets the addresses from a host.
- [func CFHostGetReachability(CFHost, UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFData>?](./cfhostgetreachability%28_,_%29.md)
  Gets reachability information from a host.
- [func CFHostGetTypeID() -> CFTypeID](./cfhostgettypeid%28%29.md)
  Gets the Core Foundation type identifier for the CFHost opaque type.
- [func CFHostScheduleWithRunLoop(CFHost, CFRunLoop, CFString)](./cfhostschedulewithrunloop%28_,_,_%29.md)
  Schedules a CFHost on a run loop.
- [func CFHostSetClient(CFHost, CFHostClientCallBack?, UnsafeMutablePointer<CFHostClientContext>?) -> Bool](./cfhostsetclient%28_,_,_%29.md)
  Associates a client context and a callback function with a CFHost object or disassociates a client context and callback function that were previously set.
- [func CFHostStartInfoResolution(CFHost, CFHostInfoType, UnsafeMutablePointer<CFStreamError>?) -> Bool](./cfhoststartinforesolution%28_,_,_%29.md)
  Starts resolution for a host object.
- [func CFHostUnscheduleFromRunLoop(CFHost, CFRunLoop, CFString)](./cfhostunschedulefromrunloop%28_,_,_%29.md)
  Unschedules a CFHost from a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhostgetnames(_:_:))*