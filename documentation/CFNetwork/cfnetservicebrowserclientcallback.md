# CFNetServiceBrowserClientCallBack

**Framework**: CFNetwork  
**Kind**: typealias  
**Role**: Type Alias

Defines a pointer to the callback function for a CFNetServiceBrowser.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias CFNetServiceBrowserClientCallBack = (CFNetServiceBrowser, CFOptionFlags, CFTypeRef?, UnsafeMutablePointer<CFStreamError>?, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(struct __CFNetServiceBrowser *, unsigned long, const void *, CFStreamError *, void *) CFNetServiceBrowserClientCallBack;
```

## Discussion

If you name your callback `MyNetServiceBrowserClientCallBack`, you would declare it like this:

### Discussion

The callback function for a CFNetServiceBrowser is called one or more times when domains or services are found as the result of calling [`CFNetServiceBrowserSearchForDomains(_:_:_:)`](./cfnetservicebrowsersearchfordomains%28_,_,_%29.md) and [`CFNetServiceBrowserSearchForServices(_:_:_:_:)`](./cfnetservicebrowsersearchforservices%28_,_,_,_%29.md).

## Parameters

- `browser`: The CFNetServiceBrowser associated with this callback function.
- `flags`: Flags conveying additional information. The `kCFNetServiceFlagIsDomain` bit is set if `domainOrService` contains a domain; if this bit is not set, `domainOrService` contains a CFNetService instance. For additional bit values, see `CFNetServiceBrowserClientCallBack Bit Flags`.
- `domainOrService`: A string containing a domain name if this callback function is being called as a result of calling [`CFNetServiceBrowserSearchForDomains(_:_:_:)`](./cfnetservicebrowsersearchfordomains%28_,_,_%29.md), or a CFNetService instance if this callback function is being called as a result calling [`CFNetServiceBrowserSearchForServices(_:_:_:_:)`](./cfnetservicebrowsersearchforservices%28_,_,_,_%29.md).
- `error`: A pointer to a [`CFStreamError`](../CoreFoundation/cfstreamerror.md) structure whose `error` field may contain an error code.
- `info`: User-defined context information. The value of `info` is the same as the value of the `info` field of the [`CFNetServiceClientContext`](./cfnetserviceclientcontext.md) structure that was provided when [`CFNetServiceBrowserCreate(_:_:_:)`](./cfnetservicebrowsercreate%28_,_,_%29.md) was called to create the CFNetServiceBrowser associated with this callback function.

## See Also

### Data Types
- [typealias CFHostClientCallBack](./cfhostclientcallback.md)
  Defines a pointer to the callback function that is called when an asynchronous resolution of a CFHost completes or an error occurs for an asynchronous CFHost resolution.
- [typealias CFNetServiceClientCallBack](./cfnetserviceclientcallback.md)
  Defines a pointer to the callback function for a CFNetService.
- [typealias CFNetServiceMonitorClientCallBack](./cfnetservicemonitorclientcallback.md)
  Defines a pointer to the callback function that is to be called when a monitored record type changes.
- [typealias CFNetDiagnosticStatus](./cfnetdiagnosticstatus.md)
  A CFIndex type that is used to return status values from `CFNetDiagnostic` status and diagnostic functions. For a list of possible values, see [`CFNetDiagnosticStatusValues`](./cfnetdiagnosticstatusvalues.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserclientcallback)*