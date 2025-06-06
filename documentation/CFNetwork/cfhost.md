# CFHost

**Framework**: CFNetwork  
**Kind**: class

An opaque reference representing an CFHost object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CFHost
```

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [enum CFHostInfoType](cfhostinfotype.md)
  Values indicating the type of data that is to be resolved or the type of data that was resolved.
- [struct CFHostClientContext](cfhostclientcontext.md)
  A structure containing user-defined data and callbacks for CFHost objects.
- [func CFHostCancelInfoResolution(CFHost, CFHostInfoType)](cfhostcancelinforesolution(_:_:).md)
  Cancels the resolution of a host.
- [func CFHostCreateCopy(CFAllocator?, CFHost) -> Unmanaged<CFHost>](cfhostcreatecopy(_:_:).md)
  Creates a new host object by copying.
- [func CFHostCreateWithAddress(CFAllocator?, CFData) -> Unmanaged<CFHost>](cfhostcreatewithaddress(_:_:).md)
  Uses an address to create an instance of a host object.
- [func CFHostCreateWithName(CFAllocator?, CFString) -> Unmanaged<CFHost>](cfhostcreatewithname(_:_:).md)
  Uses a name to create an instance of a host object.
- [func CFHostGetAddressing(CFHost, UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFArray>?](cfhostgetaddressing(_:_:).md)
  Gets the addresses from a host.
- [func CFHostGetNames(CFHost, UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFArray>?](cfhostgetnames(_:_:).md)
  Gets the names from a CFHost.
- [func CFHostGetReachability(CFHost, UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFData>?](cfhostgetreachability(_:_:).md)
  Gets reachability information from a host.
- [func CFHostGetTypeID() -> CFTypeID](cfhostgettypeid().md)
  Gets the Core Foundation type identifier for the CFHost opaque type.
- [func CFHostScheduleWithRunLoop(CFHost, CFRunLoop, CFString)](cfhostschedulewithrunloop(_:_:_:).md)
  Schedules a CFHost on a run loop.
- [func CFHostSetClient(CFHost, CFHostClientCallBack?, UnsafeMutablePointer<CFHostClientContext>?) -> Bool](cfhostsetclient(_:_:_:).md)
  Associates a client context and a callback function with a CFHost object or disassociates a client context and callback function that were previously set.
- [func CFHostStartInfoResolution(CFHost, CFHostInfoType, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfhoststartinforesolution(_:_:_:).md)
  Starts resolution for a host object.
- [func CFHostUnscheduleFromRunLoop(CFHost, CFRunLoop, CFString)](cfhostunschedulefromrunloop(_:_:_:).md)
  Unschedules a CFHost from a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhost)*