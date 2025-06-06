# CFNetServiceClientContext

**Framework**: CFNetwork  
**Kind**: struct

A structure provided when a CFNetService is associated with a callback function or when a CFNetServiceBrowser is created.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct CFNetServiceClientContext
```

## Topics

### Initializers
- [init()](cfnetserviceclientcontext/init.md)
  Creates an object that contains user-defined data and callbacks for net service browsers.
- [init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: CFAllocatorRetainCallBack?, release: CFAllocatorReleaseCallBack?, copyDescription: CFAllocatorCopyDescriptionCallBack?)](cfnetserviceclientcontext/init(version:info:retain:release:copydescription:).md)
  Creates an object that contains user-defined data and callbacks for net service browsers using the specified values.
### Instance Properties
- [var copyDescription: CFAllocatorCopyDescriptionCallBack?](cfnetserviceclientcontext/copydescription.md)
  Callback used to create a descriptive string representation of the data pointed to by `info`. In implementing this function, return a reference to a CFString object that describes your allocator and some characteristics of your user-defined data, which is used by `CFCopyDescription()`. You can set this field to `NULL`, in which case Core Foundation will provide a rudimentary description.
- [var info: UnsafeMutableRawPointer?](cfnetserviceclientcontext/info.md)
  Arbitrary pointer to user-allocated memory containing user-defined data that is associated with the service, browser, or monitor and is passed to their respective callback functions. The data must be valid for as long as the CFNetService, CFNetServiceBrowser, or CFNetServiceMonitor is valid. Set this field to `NULL` if your callback function doesn’t want to receive user-defined data.
- [var release: CFAllocatorReleaseCallBack?](cfnetserviceclientcontext/release.md)
  Callback that removes a retain previously added for the service or browser on the `info` pointer. This field can be `NULL`, but setting this field to `NULL` may result in memory leaks.
- [var retain: CFAllocatorRetainCallBack?](cfnetserviceclientcontext/retain.md)
  The callback used to add a retain for the service or browser using `info` for the life of the service or browser. This callback may be used for temporary references the service or browser needs to take. This callback returns the actual `info` pointer so it can be stored in the service or browser. This field can be `NULL`.
- [var version: CFIndex](cfnetserviceclientcontext/version.md)
  Version number for this structure. Currently the only valid value is zero.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

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
- [func CFNetServiceBrowserUnscheduleFromRunLoop(CFNetServiceBrowser, CFRunLoop, CFString)](cfnetservicebrowserunschedulefromrunloop(_:_:_:).md)
  Unschedules a CFNetServiceBrowser from a run loop and mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetserviceclientcontext)*