# CFNetServiceBrowserStopSearch(_:_:)

**Framework**: CFNetwork  
**Kind**: func

Stops a search for domains or services.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFNetServiceBrowserStopSearch(_ browser: CFNetServiceBrowser, _ error: UnsafeMutablePointer<CFStreamError>?)
```

#### Discussion

This functions stops a search started by a previous call to [`CFNetServiceBrowserSearchForDomains(_:_:_:)`](cfnetservicebrowsersearchfordomains(_:_:_:).md) or [`CFNetServiceBrowserSearchForServices(_:_:_:_:)`](cfnetservicebrowsersearchforservices(_:_:_:_:).md). For asynchronous and synchronous searches, calling this function causes the callback function associated with the CFNetServiceBrowser to be called once for each domain or service found. If the search is asynchronous, `error` is passed to the callback function. If the search is synchronous, calling this function causes [`CFNetServiceBrowserSearchForDomains(_:_:_:)`](cfnetservicebrowsersearchfordomains(_:_:_:).md) or [`CFNetServiceBrowserSearchForServices(_:_:_:_:)`](cfnetservicebrowsersearchforservices(_:_:_:_:).md) to return `FALSE`. If the `error` parameter for either call pointed to a [`CFStreamError`](https://developer.apple.com/documentation/CoreFoundation/CFStreamError) structure, the [`CFStreamError`](https://developer.apple.com/documentation/CoreFoundation/CFStreamError) structure contains the error code and the error code’s domain as set when this function was called.

##### Special Considerations

This function is thread safe.

If you are stopping an asynchronous search, before calling this function, call [`CFNetServiceBrowserUnscheduleFromRunLoop(_:_:_:)`](cfnetservicebrowserunschedulefromrunloop(_:_:_:).md), followed by [`CFNetServiceBrowserInvalidate(_:)`](cfnetservicebrowserinvalidate(_:).md).

## Parameters

- `browser`: The CFNetServiceBrowser that was used to start the search; cannot be  .
- `error`: A pointer to a   structure that will be passed to the callback function associated with this CFNetServiceBrowser (if the search is being conducted in asynchronous mode) or that is pointed to by the   parameter when   or   returns (if the search is being conducted in synchronous mode). Set the   field to   and the   field to an appropriate value.

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
- [func CFNetServiceBrowserUnscheduleFromRunLoop(CFNetServiceBrowser, CFRunLoop, CFString)](cfnetservicebrowserunschedulefromrunloop(_:_:_:).md)
  Unschedules a CFNetServiceBrowser from a run loop and mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserstopsearch(_:_:))*