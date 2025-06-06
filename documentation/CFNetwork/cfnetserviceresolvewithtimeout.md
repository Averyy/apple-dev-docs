# CFNetServiceResolveWithTimeout(_:_:_:)

**Framework**: CFNetwork  
**Kind**: func

Gets the IP address or addresses for a CFNetService.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFNetServiceResolveWithTimeout(_ theService: CFNetService, _ timeout: CFTimeInterval, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool
```

#### Return Value

`TRUE` if an asynchronous service resolution was started or if a synchronous service resolution updated the CFNetService; `FALSE` if an asynchronous or synchronous resolution failed or timed out, or if a synchronous resolution was canceled.

#### Discussion

This function updates the specified CFNetService with the IP address or addresses associated with the service. Call [`CFNetServiceGetAddressing(_:)`](cfnetservicegetaddressing(_:).md) to get the addresses.

When resolving a service that runs in asynchronous mode, this function returns `TRUE` if the CFNetService has a domain, type, and name, and the underlying resolution process was started. Otherwise, this function returns `FALSE`. Once started, the resolution continues until it is canceled by calling [`CFNetServiceCancel(_:)`](cfnetservicecancel(_:).md).

When resolving a service that runs in synchronous mode, this function blocks until the CFNetService is updated with at least one IP address, until an error occurs, or until [`CFNetServiceCancel(_:)`](cfnetservicecancel(_:).md) is called.

##### Special Considerations

This function is thread safe.

If the service will be used in asynchronous mode, you must call [`CFNetServiceSetClient(_:_:_:)`](cfnetservicesetclient(_:_:_:).md) before calling this function.

## Parameters

- `theService`: The CFNetService to resolve; cannot be  . The resolution will fail if the service doesn’t have a domain, a type, and a name.
- `timeout`: Value of type   specifying the maximum amount of time allowed to perform the resolution. If the resolution is not performed within the specified amount of time, a timeout error will be returned. If   is less than or equal to zero, an infinite amount of time is allowed.
- `error`: Pointer to a   structure that will be set to an error code and the error code’s domain if an error occurs; or   if you don’t want to receive the error code and its domain.

## See Also

- [class CFNetService](cfnetservice.md)
  An opaque reference representing a CFNetService.
- [class CFNetServiceBrowser](cfnetservicebrowser.md)
  An opaque reference representing a CFNetServiceBrowser.
- [struct CFNetServiceBrowserFlags](cfnetservicebrowserflags.md)
  Flags that the system passes to net service browser callbacks.
- [class CFNetServiceMonitor](cfnetservicemonitor.md)
  An opaque reference for a service monitor.
- [enum CFNetServiceMonitorType](cfnetservicemonitortype.md)
  Record type specifier used to tell a service monitor the type of record changes to watch for.
- [struct CFNetServiceClientContext](cfnetserviceclientcontext.md)
  A structure provided when a CFNetService is associated with a callback function or when a CFNetServiceBrowser is created.
- [struct CFNetServiceRegisterFlags](cfnetserviceregisterflags.md)
  Options to use when registering a service on the network.
- [enum CFNetServicesError](cfnetserviceserror.md)
  Error codes that may be returned by CFNetServices functions or passed to CFNetServices callback functions.
- [func CFNetServiceBrowserInvalidate(CFNetServiceBrowser)](cfnetservicebrowserinvalidate(_:).md)
  Invalidates an instance of a Network Service browser object.
- [func CFNetServiceBrowserScheduleWithRunLoop(CFNetServiceBrowser, CFRunLoop, CFString)](cfnetservicebrowserschedulewithrunloop(_:_:_:).md)
  Schedules a CFNetServiceBrowser on a run loop.
- [func CFNetServiceBrowserCreate(CFAllocator?, CFNetServiceBrowserClientCallBack, UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser>](cfnetservicebrowsercreate(_:_:_:).md)
  Creates an instance of a Network Service browser object.
- [func CFNetServiceBrowserGetTypeID() -> CFTypeID](cfnetservicebrowsergettypeid().md)
  Gets the Core Foundation type identifier for the Network Service browser object.
- [func CFNetServiceBrowserSearchForDomains(CFNetServiceBrowser, Bool, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfnetservicebrowsersearchfordomains(_:_:_:).md)
  Searches for domains.
- [func CFNetServiceBrowserSearchForServices(CFNetServiceBrowser, CFString, CFString, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfnetservicebrowsersearchforservices(_:_:_:_:).md)
  Searches a domain for services of a specified type.
- [func CFNetServiceBrowserStopSearch(CFNetServiceBrowser, UnsafeMutablePointer<CFStreamError>?)](cfnetservicebrowserstopsearch(_:_:).md)
  Stops a search for domains or services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetserviceresolvewithtimeout(_:_:_:))*