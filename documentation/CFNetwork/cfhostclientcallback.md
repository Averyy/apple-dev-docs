# CFHostClientCallBack

**Framework**: CFNetwork  
**Kind**: typealias

Defines a pointer to the callback function that is called when an asynchronous resolution of a CFHost completes or an error occurs for an asynchronous CFHost resolution.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias CFHostClientCallBack = (CFHost, CFHostInfoType, UnsafePointer<CFStreamError>?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

If you name your callback `MyHostClientCallBack`, you would declare it like this:

##### Discussion

The callback function for a CFHost object is called one or more times when an asynchronous resolution completes for the specified host, when an asynchronous resolution is cancelled, or when an error occurs during an asynchronous resolution.

## Parameters

- `theHost`: The host for which an asynchronous resolution has been completed.
- `typeInfo`: Value of type   representing the type of information (addresses, names, or reachability information) obtained by the completed resolution. See   for possible values.
- `error`: If the resolution failed, contains a   structure whose   field contains an error code.
- `info`: User-defined context information. The value pointed to by   is the same as the value pointed to by the   field of the   structure that was provided when the host was associated with this callback function.

## See Also

- [typealias CFNetServiceBrowserClientCallBack](cfnetservicebrowserclientcallback.md)
  Defines a pointer to the callback function for a CFNetServiceBrowser.
- [typealias CFNetServiceClientCallBack](cfnetserviceclientcallback.md)
  Defines a pointer to the callback function for a CFNetService.
- [typealias CFNetServiceMonitorClientCallBack](cfnetservicemonitorclientcallback.md)
  Defines a pointer to the callback function that is to be called when a monitored record type changes.
- [typealias CFNetDiagnosticStatus](cfnetdiagnosticstatus.md)
  A CFIndex type that is used to return status values from `CFNetDiagnostic` status and diagnostic functions. For a list of possible values, see [`CFNetDiagnosticStatusValues`](cfnetdiagnosticstatusvalues.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhostclientcallback)*