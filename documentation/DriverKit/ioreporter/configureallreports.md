# configureAllReports

**Framework**: DriverKit  
**Kind**: method

Calls `configureReport()` on multiple `IOReporter` objects

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static IOReturn configureAllReports(OSCollection * reporters, OSData * channels, IOReportConfigureAction action, uint32_t * outCount);
```

#### Return Value

`kIOReturnSuccess` if all objects successfully complete [`configureReport`](ioreporter/configurereport.md).

#### Discussion

The OSSet must only contain `IOReporter` instances.  The presence of non-`IOReporter` instances will cause this function to return `kIOReturnBadArgument`.  If any reporter returns an error, the function will immediately return that error.

Per the [`configureReport`](ioreporter/configurereport.md) documentation, each reporter will search channelList for channels it is reporting and provide a partial response.

## Parameters

- `reporters`: An   of   objects.
- `channels`: The full list of channels to configure.
- `action`: The action to perform.
- `outCount`: Count of updated reporters.

## See Also

- [updateAllReports](ioreporter/updateallreports.md)
  Calls `updateReport()` on multiple IOReporter objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter/configureallreports)*