# CFNetServiceMonitorStart(_:_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Starts monitoring.

**Availability**:
- iOS 2.0+ - Deprecated in 27.0
- iPadOS 2.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.4+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use nw_browser_t or nw_listener_t in Network framework instead

## Declaration

```swift
func CFNetServiceMonitorStart(_ monitor: CFNetServiceMonitor, _ recordType: CFNetServiceMonitorType, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool
```

```c
extern Boolean CFNetServiceMonitorStart(CFNetServiceMonitorRef monitor, CFNetServiceMonitorType recordType, CFStreamError *error);
```

## Return Value

`TRUE` if an asynchronous monitor was started successfully. `FALSE` if an error occurred when starting an asynchronous or synchronous monitor, or if [`CFNetServiceMonitorStop(_:_:)`](./cfnetservicemonitorstop%28_,_%29.md) was called for an synchronous monitor.

## Discussion

This function starts monitoring for changes to records of the type specified by `recordType`. If a monitor is already running for the service associated with the specified CFNetServiceMonitorRef, this function returns `FALSE`.

For synchronous monitors, this function blocks until the monitor is stopped by calling [`CFNetServiceMonitorStop(_:_:)`](./cfnetservicemonitorstop%28_,_%29.md), in which case, this function returns `FALSE`.

For asynchronous monitors, this function returns `TRUE` or `FALSE`, depending on whether monitoring starts successfully.

### Special Considerations

This function is thread safe.

## Parameters

- `monitor`: CFNetServiceMonitor, created by calling [`CFNetServiceMonitorCreate(_:_:_:_:)`](./cfnetservicemonitorcreate%28_,_,_,_%29.md), that is to be started.
- `recordType`: CFNetServiceMonitorType that specified the type of record to monitor. For possible values, see [`CFNetServiceMonitorType`](./cfnetservicemonitortype.md).
- `error`: Pointer to a [`CFStreamError`](../CoreFoundation/cfstreamerror.md) structure. If an error occurs, on output, the structure’s `domain` field will be set to the error code’s domain and the `error` field will be set to an appropriate error code. Set this parameter to `NULL` if you don’t want to receive the error code and its domain.

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

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicemonitorstart(_:_:_:))*