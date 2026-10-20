# CFNetServiceBrowserStopSearch(_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Stops a search for domains or services.

**Availability**:
- iOS 2.0+ - Deprecated in 27.0
- iPadOS 2.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.2+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use nw_browser_t or nw_listener_t in Network framework instead

## Declaration

```swift
func CFNetServiceBrowserStopSearch(_ browser: CFNetServiceBrowser, _ error: UnsafeMutablePointer<CFStreamError>?)
```

```c
extern void CFNetServiceBrowserStopSearch(CFNetServiceBrowserRef browser, CFStreamError *error);
```

#### Discussion

This functions stops a search started by a previous call to [`CFNetServiceBrowserSearchForDomains(_:_:_:)`](./cfnetservicebrowsersearchfordomains%28_,_,_%29.md) or [`CFNetServiceBrowserSearchForServices(_:_:_:_:)`](./cfnetservicebrowsersearchforservices%28_,_,_,_%29.md). For asynchronous and synchronous searches, calling this function causes the callback function associated with the CFNetServiceBrowser to be called once for each domain or service found. If the search is asynchronous, `error` is passed to the callback function. If the search is synchronous, calling this function causes [`CFNetServiceBrowserSearchForDomains(_:_:_:)`](./cfnetservicebrowsersearchfordomains%28_,_,_%29.md) or [`CFNetServiceBrowserSearchForServices(_:_:_:_:)`](./cfnetservicebrowsersearchforservices%28_,_,_,_%29.md) to return `FALSE`. If the `error` parameter for either call pointed to a [`CFStreamError`](../CoreFoundation/cfstreamerror.md) structure, the [`CFStreamError`](../CoreFoundation/cfstreamerror.md) structure contains the error code and the error code’s domain as set when this function was called.

##### Special Considerations

This function is thread safe.

If you are stopping an asynchronous search, before calling this function, call [`CFNetServiceBrowserUnscheduleFromRunLoop(_:_:_:)`](./cfnetservicebrowserunschedulefromrunloop%28_,_,_%29.md), followed by [`CFNetServiceBrowserInvalidate(_:)`](./cfnetservicebrowserinvalidate%28_%29.md).

## Parameters

- `browser`: The CFNetServiceBrowser that was used to start the search; cannot be `NULL`.
- `error`: A pointer to a [`CFStreamError`](../CoreFoundation/cfstreamerror.md) structure that will be passed to the callback function associated with this CFNetServiceBrowser (if the search is being conducted in asynchronous mode) or that is pointed to by the `error` parameter when [`CFNetServiceBrowserSearchForDomains(_:_:_:)`](./cfnetservicebrowsersearchfordomains%28_,_,_%29.md) or [`CFNetServiceBrowserSearchForServices(_:_:_:_:)`](./cfnetservicebrowsersearchforservices%28_,_,_,_%29.md) returns (if the search is being conducted in synchronous mode). Set the `domain` field to `kCFStreamErrorDomainCustom` and the `error` field to an appropriate value.

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
- [func CFNetServiceBrowserUnscheduleFromRunLoop(CFNetServiceBrowser, CFRunLoop, CFString)](./cfnetservicebrowserunschedulefromrunloop%28_,_,_%29.md)
  Unschedules a CFNetServiceBrowser from a run loop and mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserstopsearch(_:_:))*