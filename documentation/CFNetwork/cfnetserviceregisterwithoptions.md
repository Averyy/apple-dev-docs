# CFNetServiceRegisterWithOptions(_:_:_:)

**Framework**: CFNetwork  
**Kind**: func

Makes a CFNetService available on the network.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFNetServiceRegisterWithOptions(_ theService: CFNetService, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool
```

#### Return Value

`TRUE` if an asynchronous service registration was started; `FALSE` if an asynchronous or synchronous registration failed or if a synchronous registration was canceled.

#### Discussion

If the service is to run in asynchronous mode, you must call [`CFNetServiceSetClient(_:_:_:)`](cfnetservicesetclient(_:_:_:).md) to associate a callback function with this CFNetService before calling this function.

When registering a service that runs in asynchronous mode, this function returns `TRUE` if the service contains all of the required attributes and the registration process can start. If the registration process completes successfully, the service is available on the network until you shut down the service by calling [`CFNetServiceUnscheduleFromRunLoop(_:_:_:)`](cfnetserviceunschedulefromrunloop(_:_:_:).md), [`CFNetServiceSetClient(_:_:_:)`](cfnetservicesetclient(_:_:_:).md), and [`CFNetServiceCancel(_:)`](cfnetservicecancel(_:).md). If the service does not contain all of the required attributes or if the registration process does not complete successfully, this function returns `FALSE`.

When registering a service that runs in synchronous mode, this function blocks until an error occurs, in which case this function returns `FALSE`. Until this function returns `FALSE`, the service is available on the network. To force this function to return `FALSE`, thereby shutting down the service, call [`CFNetServiceCancel(_:)`](cfnetservicecancel(_:).md) from another thread.

The `options` parameter is a bit flag for specifying service registration options. Currently, `kCFNetServiceFlagNoAutoRename` is the only supported registration option. If this bit is set and a service of the same name is running, the registration will fail. If this bit is not set and a service of the same name is running, the service that is being registered will be renamed automatically by appending `(``)` to the service name, where  is a number that is incremented until the service can be registered with a unique name.

##### Special Considerations

This function is thread safe.

## Parameters

- `theService`: Network service to register; cannot be  . The registration will fail if the service doesn’t have a domain, a type, a name, and an IP address.
- `options`: Bit flags for specifying registration options. Currently, the only registration option is  . For details, see  .
- `error`: Pointer to a   structure that will be set to an error code and the error code’s domain if an error occurs; or   if you don’t want to receive the error code and its domain.

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

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetserviceregisterwithoptions(_:_:_:))*