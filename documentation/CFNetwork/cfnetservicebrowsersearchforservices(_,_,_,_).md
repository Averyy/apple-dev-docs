# CFNetServiceBrowserSearchForServices(_:_:_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Searches a domain for services of a specified type.

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
func CFNetServiceBrowserSearchForServices(_ browser: CFNetServiceBrowser, _ domain: CFString, _ serviceType: CFString, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool
```

```c
extern Boolean CFNetServiceBrowserSearchForServices(CFNetServiceBrowserRef browser, CFStringRef domain, CFStringRef serviceType, CFStreamError *error);
```

## Return Value

`TRUE` if the search was started (asynchronous mode); `FALSE` if another search is already in progress for this CFNetServiceBrowser or if an error occurred.

## Discussion

This function searches the specified domain for services that match the specified service type. The search continues until the search is canceled by calling [`CFNetServiceBrowserStopSearch(_:_:)`](./cfnetservicebrowserstopsearch%28_,_%29.md). When a match is found, the callback function specified when the CFNetServiceBrowser was created is called and passed an instance of a CFNetService representing the service that was found.

In asynchronous mode, this function returns `TRUE` if the search was started. Otherwise, it returns `FALSE`.

In synchronous mode, this function blocks until the search is stopped by calling [`CFNetServiceBrowserStopSearch(_:_:)`](./cfnetservicebrowserstopsearch%28_,_%29.md) from another thread, in which case this function returns `FALSE`, or until an error occurs.

### Special Considerations

This function is thread safe.

For any one CFNetServiceBrowser, only one domain search or one service search can be in progress at the same time.

## Parameters

- `browser`: The CFNetServiceBrowser, obtained by previously calling [`CFNetServiceBrowserCreate(_:_:_:)`](./cfnetservicebrowsercreate%28_,_,_%29.md), that is to perform the search; cannot be `NULL`.
- `domain`: The domain to search for the service type; cannot be `NULL`. To get the domains that are available for searching, call [`CFNetServiceBrowserSearchForDomains(_:_:_:)`](./cfnetservicebrowsersearchfordomains%28_,_,_%29.md).
- `error`: A pointer to a [`CFStreamError`](../CoreFoundation/cfstreamerror.md) structure, that, if an error occurs, will be set to the error and the error’s domain and passed to your callback function. Pass `NULL` if you don’t want to receive the error that may occur as a result of this particular call.

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
- [func CFNetServiceBrowserStopSearch(CFNetServiceBrowser, UnsafeMutablePointer<CFStreamError>?)](./cfnetservicebrowserstopsearch%28_,_%29.md)
  Stops a search for domains or services.
- [func CFNetServiceBrowserUnscheduleFromRunLoop(CFNetServiceBrowser, CFRunLoop, CFString)](./cfnetservicebrowserunschedulefromrunloop%28_,_,_%29.md)
  Unschedules a CFNetServiceBrowser from a run loop and mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowsersearchforservices(_:_:_:_:))*