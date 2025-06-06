# CFHostStartInfoResolution(_:_:_:)

**Framework**: CFNetwork  
**Kind**: func

Starts resolution for a host object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFHostStartInfoResolution(_ theHost: CFHost, _ info: CFHostInfoType, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool
```

#### Return Value

`TRUE` if the resolution was started (asynchronous mode); `FALSE` if another resolution is already in progress for `theHost` or if an error occurred.

#### Discussion

This function retrieves the information specified by `info` and stores it in the host.

In synchronous mode, this function blocks until the resolution has completed, in which case this function returns `TRUE`, until the resolution is stopped by calling [`CFHostCancelInfoResolution(_:_:)`](cfhostcancelinforesolution(_:_:).md) from another thread, in which case this function returns `FALSE`, or until an error occurs.

##### Special Considerations

This function is thread safe.

## Parameters

- `theHost`: The host, obtained by previously calling  ,  , or  , that is to be resolved. This value must not be  .
- `info`: A value of type   specifying the type of information that is to be retrieved. See   for possible values.
- `error`: A pointer to a   structure, that, if an error occurs, is set to the error and the error’s domain. In synchronous mode, the error indicates why resolution failed, and in asynchronous mode, the error indicates why resolution failed to start.

## See Also

- [class CFHost](cfhost.md)
  An opaque reference representing an CFHost object.
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
- [func CFHostUnscheduleFromRunLoop(CFHost, CFRunLoop, CFString)](cfhostunschedulefromrunloop(_:_:_:).md)
  Unschedules a CFHost from a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhoststartinforesolution(_:_:_:))*