# CFNetServiceCreateTXTDataWithDictionary(_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Flattens a set of key/value pairs into a CFDataRef suitable for passing to [`CFNetServiceSetTXTData(_:_:)`](./cfnetservicesettxtdata%28_,_%29.md).

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
func CFNetServiceCreateTXTDataWithDictionary(_ alloc: CFAllocator?, _ keyValuePairs: CFDictionary) -> Unmanaged<CFData>?
```

```c
extern CFDataRefCFNetServiceCreateTXTDataWithDictionary(CFAllocatorRef alloc, CFDictionaryRef keyValuePairs);
```

## Return Value

A CFData object containing the flattened form of `keyValuePairs`, or `NULL` if the dictionary could not be flattened. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function flattens the key/value pairs in the dictionary specified by `keyValuePairs` into a CFDataRef suitable for passing to [`CFNetServiceSetTXTData(_:_:)`](./cfnetservicesettxtdata%28_,_%29.md). Note that this function is not a general purpose function for flattening CFDictionaryRefs.

The keys in the dictionary referenced by `keyValuePairs` must be CFStringRefs and the values must be CFDataRefs. Any values that are CFStringRefs are converted to CFDataRefs representing the flattened UTF-8 bytes of the string. The types of the values are not encoded in the CFDataRefs, so any CFStringRefs that are converted to CFDataRefs remain CFDataRefs when the CFDataRef produced by this function is processed by [`CFNetServiceCreateDictionaryWithTXTData(_:_:)`](./cfnetservicecreatedictionarywithtxtdata%28_,_%29.md).

### Special Considerations

This function is thread safe.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass `NULL` or [`kCFAllocatorDefault`](../CoreFoundation/kcfallocatordefault.md) to use the current default allocator.
- `keyValuePairs`: CFDictionaryRef containing the key/value pairs that are to be placed in a TXT record. Each key must be a CFStringRef and each value should be a CFDataRef or a CFStringRef. (See the discussion below for additional information about values that are CFStringRefs.) This function fails if any other data types are provided. The length of a key and its value should not exceed 255 bytes.

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

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicecreatetxtdatawithdictionary(_:_:))*