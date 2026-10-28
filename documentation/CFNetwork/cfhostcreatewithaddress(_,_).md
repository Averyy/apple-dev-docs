# CFHostCreateWithAddress(_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Uses an address to create an instance of a host object.

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
func CFHostCreateWithAddress(_ allocator: CFAllocator?, _ addr: CFData) -> Unmanaged<CFHost>
```

```c
extern CFHostRefCFHostCreateWithAddress(CFAllocatorRef allocator, CFDataRef addr);
```

## Return Value

A valid CFHostRef object that can be resolved, or `NULL` if the host could not be created. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Call [`CFHostStartInfoResolution(_:_:_:)`](./cfhoststartinforesolution%28_,_,_%29.md) to resolve the return object’s name and reachability information.

### Special Considerations

This function is thread safe.

## Parameters

- `addr`: A CFDataRef object containing a `sockaddr` structure for the address of the host. This value must not be `NULL`.

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
- [func CFHostCreateWithName(CFAllocator?, CFString) -> Unmanaged<CFHost>](./cfhostcreatewithname%28_,_%29.md)
  Uses a name to create an instance of a host object.
- [func CFHostGetAddressing(CFHost, UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFArray>?](./cfhostgetaddressing%28_,_%29.md)
  Gets the addresses from a host.
- [func CFHostGetNames(CFHost, UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFArray>?](./cfhostgetnames%28_,_%29.md)
  Gets the names from a CFHost.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhostcreatewithaddress(_:_:))*