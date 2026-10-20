# CFHostClientContext

**Framework**: CFNetwork  
**Kind**: struct  
**Role**: Structure

A structure containing user-defined data and callbacks for CFHost objects.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct CFHostClientContext
```

```c
struct CFHostClientContext;
```

## Topics

### Initializers
- [init()](./cfhostclientcontext/init%28%29.md)
  Initializes an object that contains user-defined data and callbacks for a network host.
- [init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: CFAllocatorRetainCallBack?, release: CFAllocatorReleaseCallBack?, copyDescription: CFAllocatorCopyDescriptionCallBack?)](./cfhostclientcontext/init%28version,info,retain,release,copydescription%29.md)
  Initializes an object that contains user-defined data and callbacks for a network host using the specified values.
### Instance Properties
- [var copyDescription: CFAllocatorCopyDescriptionCallBack?](./cfhostclientcontext/copydescription.md)
  The callback used to create a descriptive string representation of the info pointer (or the data pointed to by the info pointer) for debugging purposes. This callback is called by the [`CFCopyDescription(_:)`](../CoreFoundation/cfcopydescription%28_%29.md) function.
- [var info: UnsafeMutableRawPointer?](./cfhostclientcontext/info.md)
  An arbitrary pointer to allocated memory containing user-defined data that can be associated with the host and that is passed to the callbacks.
- [var release: CFAllocatorReleaseCallBack?](./cfhostclientcontext/release.md)
  The callback used to remove a retain previously added for the host on the info pointer.
- [var retain: CFAllocatorRetainCallBack?](./cfhostclientcontext/retain.md)
  The callback used to add a retain for the host on the info pointer for the life of the host, and may be used for temporary references the host needs to take. This callback returns the actual info pointer to store in the host, almost always just the pointer passed as the parameter.
- [var version: CFIndex](./cfhostclientcontext/version.md)
  The version number of the structure type passed as a parameter to the host client function. The only valid version number is `0`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Hosts
- [class CFHost](./cfhost.md)
  An opaque reference representing an CFHost object.
- [enum CFHostInfoType](./cfhostinfotype.md)
  Values indicating the type of data that is to be resolved or the type of data that was resolved.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhostclientcontext)*