# CFNetServiceMonitorStop(_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Stops a CFNetServiceMonitor.

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
func CFNetServiceMonitorStop(_ monitor: CFNetServiceMonitor, _ error: UnsafeMutablePointer<CFStreamError>?)
```

```c
extern void CFNetServiceMonitorStop(CFNetServiceMonitorRef monitor, CFStreamError *error);
```

## Discussion

This function stops the specified monitor. Call [`CFNetServiceMonitorStart(_:_:_:)`](./cfnetservicemonitorstart%28_,_,_%29.md) if you want to start monitoring again.

If you want to stop monitoring and no longer need to monitor record changes, call [`CFNetServiceMonitorInvalidate(_:)`](./cfnetservicemonitorinvalidate%28_%29.md) instead of this function.

### Special Considerations

This function is thread safe.

## Parameters

- `monitor`: CFNetServiceMonitor, started by calling [`CFNetServiceMonitorStart(_:_:_:)`](./cfnetservicemonitorstart%28_,_,_%29.md), that is to be stopped.
- `error`: Pointer to a [`CFStreamError`](../CoreFoundation/cfstreamerror.md) structure or `NULL`. For synchronous monitors, set the `error` field of this structure to the non-zero value you want to be set in the `CFStreamError` structure when [`CFNetServiceMonitorStart(_:_:_:)`](./cfnetservicemonitorstart%28_,_,_%29.md) returns. Note that when it returns, [`CFNetServiceMonitorStart(_:_:_:)`](./cfnetservicemonitorstart%28_,_,_%29.md) returns `FALSE.` If the monitor was started asynchronously, set the `error` field to the non-zero value you want the monitor’s callback to receive when it is called. If this parameter is `NULL`, default values for the `CFStreamError` structure are used: the domain is set to `kCFStreamErrorDomainNetServices` and the error code is set to `kCFNetServicesErrorCancel`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicemonitorstop(_:_:))*