# createLegend

**Framework**: DriverKit  
**Kind**: method

Create a legend entry represending this reporter’s channels.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
OSDictionary * createLegend();
```

#### Return Value

An [`IOReportLegendEntry`](ioreportlegendentry.md) object or `NULL` on failure.

#### Discussion

All channels added to the reporter will be represented in the resulting legend entry.

Legends must be published together as an array under the `kIOReportLegendKey` in the I/O Kit registry.  The [`IOReportLegend`](ioreportlegend.md) class can be used to properly combine legend entries from multiple reporters as well as to put channels into groups of interest to observers.  When published, individual legend entries share characteristics such as group and sub-group.  Multiple [`IOReporter`](ioreporter.md) instances are required to produce independent legend entries which can then be published with different characteristics.

Drivers wishing to publish legends should do so as part of their `::start()` routine.  As superclasses  have installed legend entries, any existing existing legend should be retrieved and IOReportLegend used to merge it with the new entries.

Recommendations for best practices are forthcoming.

Instead of calling createLegend on your reporter object and then appending it manually to IOReportLegend, one may prefer to call [`addReporterLegend`](ioreportlegend/addreporterlegend-c.method.md) which creates and appends a reporter’s [`IOReportLegendEntry`](ioreportlegendentry.md) in a single call.

Locking: same-instance concurrency SAFE, MAY BLOCK

## See Also

- [addChannel](ioreporter/addchannel.md)
  Add an additional, similar channel to the reporter.
- [configureReport](ioreporter/configurereport.md)
  Track IOService::configureReport(), provide sizing info
- [free](ioreporter/free.md)
- [updateReport](ioreporter/updatereport.md)
  Produce standard reply to IOService::updateReport()


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter/createlegend)*