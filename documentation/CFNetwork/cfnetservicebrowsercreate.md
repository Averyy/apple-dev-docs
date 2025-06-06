# CFNetServiceBrowserCreate(_:_:_:)

**Framework**: CFNetwork  
**Kind**: func

Creates an instance of a Network Service browser object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFNetServiceBrowserCreate(_ alloc: CFAllocator?, _ clientCB: CFNetServiceBrowserClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser>
```

#### Return Value

A new browser object, or `NULL` if the instance could not be created. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function creates an instance of a Network Service browser object, called a CFNetServiceBrowser, that can be used to search for domains and for services.

To use the resulting CFNetServiceBrowser in asynchronous mode, call [`CFNetServiceBrowserScheduleWithRunLoop(_:_:_:)`](cfnetservicebrowserschedulewithrunloop(_:_:_:).md). Then call [`CFNetServiceBrowserSearchForDomains(_:_:_:)`](cfnetservicebrowsersearchfordomains(_:_:_:).md) and [`CFNetServiceBrowserSearchForServices(_:_:_:_:)`](cfnetservicebrowsersearchforservices(_:_:_:_:).md) to use the CFNetServiceBrowser to search for services and domains, respectively. The callback function specified by `clientCB` is called from a run loop to pass search results to your application. The search continues until you stop the search by calling [`CFNetServiceBrowserStopSearch(_:_:)`](cfnetservicebrowserstopsearch(_:_:).md).

If you do not call [`CFNetServiceBrowserScheduleWithRunLoop(_:_:_:)`](cfnetservicebrowserschedulewithrunloop(_:_:_:).md), searches with the resulting CFNetServiceBrowser are made in synchronous mode. Calls made to [`CFNetServiceBrowserSearchForDomains(_:_:_:)`](cfnetservicebrowsersearchfordomains(_:_:_:).md) and [`CFNetServiceBrowserSearchForServices(_:_:_:_:)`](cfnetservicebrowsersearchforservices(_:_:_:_:).md) block until there are search results, in which case the callback function specified by `clientCB` is called, until the search is are stopped by calling [`CFNetServiceBrowserStopSearch(_:_:)`](cfnetservicebrowserstopsearch(_:_:).md) from another thread, or an error occurs.

To shut down a CFNetServiceBrowser that is running in asynchronous mode, call [`CFNetServiceBrowserStopSearch(_:_:)`](cfnetservicebrowserstopsearch(_:_:).md), followed by [`CFNetServiceBrowserUnscheduleFromRunLoop(_:_:_:)`](cfnetservicebrowserunschedulefromrunloop(_:_:_:).md), and then [`CFNetServiceBrowserInvalidate(_:)`](cfnetservicebrowserinvalidate(_:).md).

##### Special Considerations

This function is thread safe.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `clientCB`: Callback function that is to be called when domains and services are found; cannot be  . For details, see  .
- `clientContext`: Context information to be used when   is called; cannot be  . For details, see  .

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
- [func CFNetServiceBrowserGetTypeID() -> CFTypeID](cfnetservicebrowsergettypeid().md)
  Gets the Core Foundation type identifier for the Network Service browser object.
- [func CFNetServiceBrowserSearchForDomains(CFNetServiceBrowser, Bool, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfnetservicebrowsersearchfordomains(_:_:_:).md)
  Searches for domains.
- [func CFNetServiceBrowserSearchForServices(CFNetServiceBrowser, CFString, CFString, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfnetservicebrowsersearchforservices(_:_:_:_:).md)
  Searches a domain for services of a specified type.
- [func CFNetServiceBrowserStopSearch(CFNetServiceBrowser, UnsafeMutablePointer<CFStreamError>?)](cfnetservicebrowserstopsearch(_:_:).md)
  Stops a search for domains or services.
- [func CFNetServiceBrowserUnscheduleFromRunLoop(CFNetServiceBrowser, CFRunLoop, CFString)](cfnetservicebrowserunschedulefromrunloop(_:_:_:).md)
  Unschedules a CFNetServiceBrowser from a run loop and mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowsercreate(_:_:_:))*