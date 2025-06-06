# updateReport

**Framework**: DriverKit  
**Kind**: method

Produce standard reply to IOService::updateReport()

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
IOReturn updateReport(IOReportChannelList * channelList, IOReportConfigureAction action, uint32_t & elementCount, uint8_t * & buffer, size_t & capacity);
```

#### Return Value

Appropriate [`IOReturn`](ioreturn.md) code

#### Discussion

This method searches channelList for channels tracked by this reporter, writes the corresponding data into ‘destination’, and updates ‘result’.  It should be possible to pass a given set of [`UpdateReport`](ioservice/updatereport.md) arguments to any and all reporters as well as to `super::updateReport()` and get the right result.

The static ``IOReporter/updateAllReports` will call this method on an OSSet of reporters.

Locking: same-instance concurrency SAFE, WILL NOT BLOCK

## Parameters

- `channelList`: Channels to update
- `action`: Copy/trace data (see  )
- `elementCount`: Element count.
- `buffer`: Buffer.
- `capacity`: Capacity.

## See Also

- [addChannel](ioreporter/addchannel.md)
  Add an additional, similar channel to the reporter.
- [configureReport](ioreporter/configurereport.md)
  Track IOService::configureReport(), provide sizing info
- [createLegend](ioreporter/createlegend.md)
  Create a legend entry represending this reporter’s channels.
- [free](ioreporter/free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter/updatereport)*