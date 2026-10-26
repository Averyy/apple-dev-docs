# CFNetServiceResolve

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

This function updates the specified CFNetService with the IP address or addresses associated with the service. Call [`CFNetServiceGetAddressing(_:)`](./cfnetservicegetaddressing%28_%29.md) to get the addresses.

**Availability**:
- macOS 10.2+ - Deprecated in 10.4

> **Deprecated**: Use [`CFNetServiceResolveWithTimeout(_:_:_:)`](./cfnetserviceresolvewithtimeout%28_,_,_%29.md) instead.

## Declaration

```c
extern Boolean CFNetServiceResolve(CFNetServiceRef theService, CFStreamError *error);
```

#### Return Value

`TRUE` if an asynchronous service resolution was started or if a synchronous service resolution updated the CFNetService; `FALSE` if an asynchronous or synchronous resolution failed or if a synchronous resolution was canceled.

#### Discussion

When resolving a service that runs in asynchronous mode, this function returns `TRUE` if the CFNetService has a domain, type, and name, and the underlying resolution process was started. Otherwise, this function returns `FALSE`. Once started, the resolution continues until it is canceled by calling [`CFNetServiceCancel(_:)`](./cfnetservicecancel%28_%29.md).

When resolving a service that runs in synchronous mode, this function blocks until the CFNetService is updated with at least one IP address, until an error occurs, or until [`CFNetServiceCancel(_:)`](./cfnetservicecancel%28_%29.md) is called.

##### Special Considerations

This function is thread safe.

If the service will be used in asynchronous mode, you must call [`CFNetServiceSetClient(_:_:_:)`](./cfnetservicesetclient%28_,_,_%29.md) before calling this function.

## Parameters

- `theService`: The CFNetService to resolve; cannot be `NULL`. The resolution will fail if the service doesn’t have a domain, a type, and a name.
- `error`: A pointer to a [`CFStreamError`](../CoreFoundation/cfstreamerror.md) structure that will be set to an error code and the error code’s domain if an error occurs; or `NULL` if you don’t want to receive the error code and its domain.

## See Also

### Network Services
- [class CFNetService](./cfnetservice.md)
  An opaque reference representing a CFNetService.
- [class CFNetServiceBrowser](./cfnetservicebrowser.md)
  An opaque reference representing a CFNetServiceBrowser.
- [struct CFNetServiceBrowserFlags](./cfnetservicebrowserflags.md)
  Flags that the system passes to net service browser callbacks.
- [class CFNetServiceMonitor](./cfnetservicemonitor.md)
  An opaque reference for a service monitor.
- [enum CFNetServiceMonitorType](./cfnetservicemonitortype.md)
  Record type specifier used to tell a service monitor the type of record changes to watch for.
- [struct CFNetServiceClientContext](./cfnetserviceclientcontext.md)
  A structure provided when a CFNetService is associated with a callback function or when a CFNetServiceBrowser is created.
- [struct CFNetServiceRegisterFlags](./cfnetserviceregisterflags.md)
  Options to use when registering a service on the network.
- [enum CFNetServicesError](./cfnetserviceserror.md)
  Error codes that may be returned by CFNetServices functions or passed to CFNetServices callback functions.
- [func CFNetServiceBrowserInvalidate(CFNetServiceBrowser)](./cfnetservicebrowserinvalidate%28_%29.md)
  Invalidates an instance of a Network Service browser object.
- [func CFNetServiceBrowserScheduleWithRunLoop(CFNetServiceBrowser, CFRunLoop, CFString)](./cfnetservicebrowserschedulewithrunloop%28_,_,_%29.md)
  Schedules a CFNetServiceBrowser on a run loop.
- [func CFNetServiceBrowserCreate(CFAllocator?, CFNetServiceBrowserClientCallBack, UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser>](./cfnetservicebrowsercreate%28_,_,_%29.md)
  Creates an instance of a Network Service browser object.
- [func CFNetServiceBrowserGetTypeID() -> CFTypeID](./cfnetservicebrowsergettypeid%28%29.md)
  Gets the Core Foundation type identifier for the Network Service browser object.
- [func CFNetServiceBrowserSearchForDomains(CFNetServiceBrowser, Bool, UnsafeMutablePointer<CFStreamError>?) -> Bool](./cfnetservicebrowsersearchfordomains%28_,_,_%29.md)
  Searches for domains.
- [func CFNetServiceBrowserSearchForServices(CFNetServiceBrowser, CFString, CFString, UnsafeMutablePointer<CFStreamError>?) -> Bool](./cfnetservicebrowsersearchforservices%28_,_,_,_%29.md)
  Searches a domain for services of a specified type.
- [func CFNetServiceBrowserStopSearch(CFNetServiceBrowser, UnsafeMutablePointer<CFStreamError>?)](./cfnetservicebrowserstopsearch%28_,_%29.md)
  Stops a search for domains or services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetserviceresolve)*