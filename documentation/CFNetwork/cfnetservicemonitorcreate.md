# CFNetServiceMonitorCreate(_:_:_:_:)

**Framework**: CFNetwork  
**Kind**: func

Creates an instance of a NetServiceMonitor object that watches for record changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFNetServiceMonitorCreate(_ alloc: CFAllocator?, _ theService: CFNetService, _ clientCB: CFNetServiceMonitorClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor>
```

#### Return Value

A new instance of a CFNetServiceMonitor, or `NULL` if the monitor could not be created. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function creates a CFNetServiceMonitor that watches for changes in records associated with `theService`.

If the CFNetServiceMonitor is to run in asynchronous mode, call [`CFNetServiceMonitorScheduleWithRunLoop(_:_:_:)`](cfnetservicemonitorschedulewithrunloop(_:_:_:).md) to schedule the monitor on a run loop. Then call [`CFNetServiceMonitorStart(_:_:_:)`](cfnetservicemonitorstart(_:_:_:).md) to start monitoring. When a change occurs, the callback function specified by `clientCB` will be called. For details, see [`CFNetServiceMonitorClientCallBack`](cfnetservicemonitorclientcallback.md).

If the CFNetServiceMonitor is to run in synchronous mode, call [`CFNetServiceMonitorStart(_:_:_:)`](cfnetservicemonitorstart(_:_:_:).md).

To stop a monitor that is running in asynchronous mode, call [`CFNetServiceMonitorStop(_:_:)`](cfnetservicemonitorstop(_:_:).md) and [`CFNetServiceMonitorUnscheduleFromRunLoop(_:_:_:)`](cfnetservicemonitorunschedulefromrunloop(_:_:_:).md).

To stop a monitor that is running in synchronous mode, call [`CFNetServiceMonitorStop(_:_:)`](cfnetservicemonitorstop(_:_:).md).

If you no longer need to monitor record changes, call [`CFNetServiceMonitorStop(_:_:)`](cfnetservicemonitorstop(_:_:).md) to stop the monitor and then call [`CFNetServiceMonitorInvalidate(_:)`](cfnetservicemonitorinvalidate(_:).md)to invalidate the monitor so it cannot be used again. Then call `CFRelease` to release the memory associated with CFNetServiceMonitorRef.

##### Special Considerations

This function is thread safe.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `theService`: CFNetService to be monitored.
- `clientCB`: Pointer to callback function that is to be called when a record associated with   changes; cannot be  .
- `clientContext`: Pointer to user-defined contextual information that is to be passed to the callback specified by   when the callback is called; cannot be  . For details, see  .

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

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicemonitorcreate(_:_:_:_:))*