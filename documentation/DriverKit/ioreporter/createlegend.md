# createLegend

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Create a legend entry represending this reporter’s channels.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
OSDictionary * createLegend();
```

#### Return Value

An [`IOReportLegendEntry`](../ioreportlegendentry.md) object or `NULL` on failure.

#### Discussion

All channels added to the reporter will be represented in the resulting legend entry.

Legends must be published together as an array under the `kIOReportLegendKey` in the I/O Kit registry.  The [`IOReportLegend`](../ioreportlegend.md) class can be used to properly combine legend entries from multiple reporters as well as to put channels into groups of interest to observers.  When published, individual legend entries share characteristics such as group and sub-group.  Multiple [`IOReporter`](../ioreporter.md) instances are required to produce independent legend entries which can then be published with different characteristics.

Drivers wishing to publish legends should do so as part of their `::start()` routine.  As superclasses *may* have installed legend entries, any existing existing legend should be retrieved and IOReportLegend used to merge it with the new entries.

Recommendations for best practices are forthcoming.

Instead of calling createLegend on your reporter object and then appending it manually to IOReportLegend, one may prefer to call [`addReporterLegend`](../ioreportlegend/addreporterlegend-c.method.md) which creates and appends a reporter’s [`IOReportLegendEntry`](../ioreportlegendentry.md) in a single call.

Locking: same-instance concurrency SAFE, MAY BLOCK

## See Also

### Instance Methods
- [addChannel](./addchannel.md)
  Add an additional, similar channel to the reporter.
- [configureReport](./configurereport.md)
  Track IOService::configureReport(), provide sizing info
- [free](./free.md)
- [updateReport](./updatereport.md)
  Produce standard reply to IOService::updateReport()


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter/createlegend)*