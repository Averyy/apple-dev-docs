# configureReport

**Framework**: DriverKit  
**Kind**: method

Track IOService::configureReport(), provide sizing info

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
IOReturn configureReport(IOReportChannelList * channelList, IOReportConfigureAction action, uint32_t & elementCount);
```

#### Return Value

Appropriate `IOReturn` code.

#### Discussion

Any time a reporting driver’s ::configureReport method is invoked, this method should be invoked on each IOReporter that is being used by that driver to report channels in channelList.

Any channels in channelList which are not tracked by this reporter are ignored.  ::configureReport(kIOReportGetDimensions) expects the full size of all channels, including any reported by superclasses.  It is valid to call this routine on multiple reporter objects in succession and they will increment ‘result’ to provide the correct total.

The static IOReporter::configureAllReports() will call this method on multiple reporters grouped in an OSSet.

Locking: same-instance concurrency SAFE, MAY BLOCK

## Parameters

- `channelList`: Channels to configure.
- `action`: Enable/disable/size, etc (see  ).
- `elementCount`: Element count.

## See Also

- [addChannel](ioreporter/addchannel.md)
  Add an additional, similar channel to the reporter.
- [createLegend](ioreporter/createlegend.md)
  Create a legend entry represending this reporter’s channels.
- [free](ioreporter/free.md)
- [updateReport](ioreporter/updatereport.md)
  Produce standard reply to IOService::updateReport()


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter/configurereport)*