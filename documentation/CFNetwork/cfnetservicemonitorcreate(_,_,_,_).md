# CFNetServiceMonitorCreate(_:_:_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Creates an instance of a NetServiceMonitor object that watches for record changes.

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
func CFNetServiceMonitorCreate(_ alloc: CFAllocator?, _ theService: CFNetService, _ clientCB: CFNetServiceMonitorClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor>
```

```c
extern CFNetServiceMonitorRefCFNetServiceMonitorCreate(CFAllocatorRef alloc, CFNetServiceRef theService, CFNetServiceMonitorClientCallBack clientCB, CFNetServiceClientContext *clientContext);
```

## Return Value

A new instance of a CFNetServiceMonitor, or `NULL` if the monitor could not be created. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function creates a CFNetServiceMonitor that watches for changes in records associated with `theService`.

If the CFNetServiceMonitor is to run in asynchronous mode, call [`CFNetServiceMonitorScheduleWithRunLoop(_:_:_:)`](./cfnetservicemonitorschedulewithrunloop%28_,_,_%29.md) to schedule the monitor on a run loop. Then call [`CFNetServiceMonitorStart(_:_:_:)`](./cfnetservicemonitorstart%28_,_,_%29.md) to start monitoring. When a change occurs, the callback function specified by `clientCB` will be called. For details, see [`CFNetServiceMonitorClientCallBack`](./cfnetservicemonitorclientcallback.md).

If the CFNetServiceMonitor is to run in synchronous mode, call [`CFNetServiceMonitorStart(_:_:_:)`](./cfnetservicemonitorstart%28_,_,_%29.md).

To stop a monitor that is running in asynchronous mode, call [`CFNetServiceMonitorStop(_:_:)`](./cfnetservicemonitorstop%28_,_%29.md) and [`CFNetServiceMonitorUnscheduleFromRunLoop(_:_:_:)`](./cfnetservicemonitorunschedulefromrunloop%28_,_,_%29.md).

To stop a monitor that is running in synchronous mode, call [`CFNetServiceMonitorStop(_:_:)`](./cfnetservicemonitorstop%28_,_%29.md).

If you no longer need to monitor record changes, call [`CFNetServiceMonitorStop(_:_:)`](./cfnetservicemonitorstop%28_,_%29.md) to stop the monitor and then call [`CFNetServiceMonitorInvalidate(_:)`](./cfnetservicemonitorinvalidate%28_%29.md)to invalidate the monitor so it cannot be used again. Then call `CFRelease` to release the memory associated with CFNetServiceMonitorRef.

### Special Considerations

This function is thread safe.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass `NULL` or [`kCFAllocatorDefault`](../CoreFoundation/kcfallocatordefault.md) to use the current default allocator.
- `theService`: CFNetService to be monitored.
- `clientCB`: Pointer to callback function that is to be called when a record associated with `theService` changes; cannot be `NULL`.
- `clientContext`: Pointer to user-defined contextual information that is to be passed to the callback specified by `clientCB` when the callback is called; cannot be `NULL`. For details, see [`CFNetServiceClientContext`](./cfnetserviceclientcontext.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicemonitorcreate(_:_:_:_:))*