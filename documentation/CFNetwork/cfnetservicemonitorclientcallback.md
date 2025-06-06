# CFNetServiceMonitorClientCallBack

**Framework**: CFNetwork  
**Kind**: typealias

Defines a pointer to the callback function that is to be called when a monitored record type changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias CFNetServiceMonitorClientCallBack = (CFNetServiceMonitor, CFNetService?, CFNetServiceMonitorType, CFData?, UnsafeMutablePointer<CFStreamError>?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

If you name your callback `MyNetServiceMonitorClientCallBack`, you would declare it like this:

##### Discussion

The callback function will be called when the monitored record type changes or when the monitor is stopped by calling [`CFNetServiceMonitorStop(_:_:)`](cfnetservicemonitorstop(_:_:).md).

## Parameters

- `theMonitor`: CFNetServiceMonitor for which the callback is being called.
- `theService`: CFNetService for which the callback is being called.
- `typeInfo`: Type of record that changed. For possible values, see  .
- `rdata`: Contents of the record that changed.
- `error`: Pointer to   structure whose   field contains an error code if an error occurred.
- `info`: Arbitrary pointer to the user-defined data that was specified in the   field of the   structure when the monitor was created by  .

## See Also

- [typealias CFHostClientCallBack](cfhostclientcallback.md)
  Defines a pointer to the callback function that is called when an asynchronous resolution of a CFHost completes or an error occurs for an asynchronous CFHost resolution.
- [typealias CFNetServiceBrowserClientCallBack](cfnetservicebrowserclientcallback.md)
  Defines a pointer to the callback function for a CFNetServiceBrowser.
- [typealias CFNetServiceClientCallBack](cfnetserviceclientcallback.md)
  Defines a pointer to the callback function for a CFNetService.
- [typealias CFNetDiagnosticStatus](cfnetdiagnosticstatus.md)
  A CFIndex type that is used to return status values from `CFNetDiagnostic` status and diagnostic functions. For a list of possible values, see [`CFNetDiagnosticStatusValues`](cfnetdiagnosticstatusvalues.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicemonitorclientcallback)*