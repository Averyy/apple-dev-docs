# CFNetServiceBrowserSearchForDomains(_:_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Searches for domains.

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
func CFNetServiceBrowserSearchForDomains(_ browser: CFNetServiceBrowser, _ registrationDomains: Bool, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool
```

```c
extern Boolean CFNetServiceBrowserSearchForDomains(CFNetServiceBrowserRef browser, Boolean registrationDomains, CFStreamError *error);
```

## Return Value

`TRUE` if the search was started (asynchronous mode); `FALSE` if another search is already in progress for this CFNetServiceBrowser or if an error occurred.

## Discussion

This function uses a CFNetServiceBrowser to search for domains. The search continues until the search is canceled by calling [`CFNetServiceBrowserStopSearch(_:_:)`](./cfnetservicebrowserstopsearch%28_,_%29.md). If `registrationDomains` is `TRUE`, this function searches only for domains in which services can be registered. If `registrationDomains` is `FALSE`, this function searches for domains that can be browsed for services. When a domain is found, the callback function specified when the CFNetServiceBrowser was created is called and passed an instance of a CFStringRef containing the domain that was found.

In asynchronous mode, this function returns `TRUE` if the search was started. Otherwise, it returns `FALSE`.

In synchronous mode, this function blocks until the search is stopped by calling [`CFNetServiceBrowserStopSearch(_:_:)`](./cfnetservicebrowserstopsearch%28_,_%29.md) from another thread, in which case it returns `FALSE`, or until an error occurs.

### Special Considerations

This function is thread safe.

For any one CFNetServiceBrowser, only one domain search or one service search can be in progress at the same time.

## Parameters

- `browser`: The CFNetServiceBrowser, obtained by previously calling [`CFNetServiceBrowserCreate(_:_:_:)`](./cfnetservicebrowsercreate%28_,_,_%29.md), that is to perform the search; cannot be `NULL`.
- `registrationDomains`: `TRUE` to search for only registration domains; `FALSE` to search for domains that can be browsed for services. For this version of the CFNetServices API, the registration domain is the local domain maintained by the mDNS responder running on the same machine as the calling application.
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
- [func CFNetServiceBrowserSearchForServices(CFNetServiceBrowser, CFString, CFString, UnsafeMutablePointer<CFStreamError>?) -> Bool](./cfnetservicebrowsersearchforservices%28_,_,_,_%29.md)
  Searches a domain for services of a specified type.
- [func CFNetServiceBrowserStopSearch(CFNetServiceBrowser, UnsafeMutablePointer<CFStreamError>?)](./cfnetservicebrowserstopsearch%28_,_%29.md)
  Stops a search for domains or services.
- [func CFNetServiceBrowserUnscheduleFromRunLoop(CFNetServiceBrowser, CFRunLoop, CFString)](./cfnetservicebrowserunschedulefromrunloop%28_,_,_%29.md)
  Unschedules a CFNetServiceBrowser from a run loop and mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowsersearchfordomains(_:_:_:))*