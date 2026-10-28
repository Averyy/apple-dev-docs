# CFNetServiceCreate(_:_:_:_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Creates an instance of a Network Service object.

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
func CFNetServiceCreate(_ alloc: CFAllocator?, _ domain: CFString, _ serviceType: CFString, _ name: CFString, _ port: Int32) -> Unmanaged<CFNetService>
```

```c
extern CFNetServiceRefCFNetServiceCreate(CFAllocatorRef alloc, CFStringRef domain, CFStringRef serviceType, CFStringRef name, SInt32 port);
```

## Return Value

A new net service object, or `NULL` if the instance could not be created. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

If the service depends on information in DNS TXT records, call `CFNetServiceSetProtocolSpecificInformation`.

If the CFNetService is to run in asynchronous mode, call [`CFNetServiceSetClient(_:_:_:)`](./cfnetservicesetclient%28_,_,_%29.md) to prepare the service for running in asynchronous mode. Then call [`CFNetServiceScheduleWithRunLoop(_:_:_:)`](./cfnetserviceschedulewithrunloop%28_,_,_%29.md) to schedule the service on a run loop. Then call [`CFNetServiceRegister`](./cfnetserviceregister.md) to make the service available.

If the CFNetService is to run in synchronous mode, call [`CFNetServiceRegister`](./cfnetserviceregister.md).

To terminate a service that is running in asynchronous mode, call [`CFNetServiceCancel(_:)`](./cfnetservicecancel%28_%29.md) and [`CFNetServiceUnscheduleFromRunLoop(_:_:_:)`](./cfnetserviceunschedulefromrunloop%28_,_,_%29.md).

To terminate a service that is running in synchronous mode, call [`CFNetServiceCancel(_:)`](./cfnetservicecancel%28_%29.md).

### Special Considerations

This function is thread safe.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass `NULL` or [`kCFAllocatorDefault`](../CoreFoundation/kcfallocatordefault.md) to use the current default allocator.
- `domain`: The domain in which the CFNetService is to be registered; cannot be `NULL`. Call [`CFNetServiceBrowserCreate(_:_:_:)`](./cfnetservicebrowsercreate%28_,_,_%29.md) and [`CFNetServiceBrowserSearchForDomains(_:_:_:)`](./cfnetservicebrowsersearchfordomains%28_,_,_%29.md) to get the registration domain.
- `name`: A unique name if the instance will be used to register a service. The name will become part of the instance name in the DNS records that will be created when the service is registered. If the instance will be used to resolve a service, the name should be the name of the machine or service that will be resolved.
- `port`: Local IP port, in host byte order, on which this service accepts connections. Pass zero to get placeholder service. With a placeholder service, the service will not be discovered by browsing, but a name conflict will occur if another client tries to register the same name. Most applications do not need to use placeholder service.

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

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicecreate(_:_:_:_:_:))*