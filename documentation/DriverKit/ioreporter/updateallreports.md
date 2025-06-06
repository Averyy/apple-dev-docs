# updateAllReports

**Framework**: DriverKit  
**Kind**: method

Calls `updateReport()` on multiple IOReporter objects.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static IOReturn updateAllReports(OSCollection * reporters, OSData * channels, IOReportConfigureAction action, uint32_t * outElementCount, uint64_t offset, uint64_t capacity, IOMemoryDescriptor * buffer);
```

#### Return Value

`kIOReturnSuccess` if all objects successfully complete [`updateReport`](ioreporter/updatereport.md).

#### Discussion

The OSSet must only contain [`IOReporter`](ioreporter.md) instances.  The presence of non-`IOReporter` instances will cause this function to return [`kIOReturnBadArgument`](kioreturnbadargument.md).  If any reporter returns an error, the function will immediately return that error.

Per the [`configureReport`](ioreporter/configurereport.md) documentation, each reporter will search channelList for channels it is reporting and provide a partial response.

## Parameters

- `reporters`: An OSSet of IOReporter objects.
- `channels`: An OSData object containing the list of channels to update.
- `action`: The action to perform.
- `outElementCount`: The number of elements in the response.
- `offset`: The offset in the buffer.
- `capacity`: The capacity of the buffer.
- `buffer`: The buffer to write the response to.

## See Also

- [configureAllReports](ioreporter/configureallreports.md)
  Calls `configureReport()` on multiple `IOReporter` objects


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter/updateallreports)*