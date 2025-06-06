# IOReporter

**Framework**: DriverKit  
**Kind**: class

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IOReporter;
```

## Topics

### Instance Methods
- [addChannel](ioreporter/addchannel.md)
  Add an additional, similar channel to the reporter.
- [configureReport](ioreporter/configurereport.md)
  Track IOService::configureReport(), provide sizing info
- [createLegend](ioreporter/createlegend.md)
  Create a legend entry represending this reporter’s channels.
- [free](ioreporter/free.md)
- [updateReport](ioreporter/updatereport.md)
  Produce standard reply to IOService::updateReport()
### Type Methods
- [configureAllReports](ioreporter/configureallreports.md)
  Calls `configureReport()` on multiple `IOReporter` objects
- [updateAllReports](ioreporter/updateallreports.md)
  Calls `updateReport()` on multiple IOReporter objects.

## Relationships

### Inherits From
- [OSObject](osobject.md)
### Inherited By
- [IOHistogramReporter](iohistogramreporter.md)
- [IOSimpleReporter](iosimplereporter.md)
- [IOStateReporter](iostatereporter.md)

## See Also

- [IOHistogramReporter](iohistogramreporter.md)
- [IOReportLegend](ioreportlegend.md)
- [IOServiceStateNotificationDispatchSource](ioservicestatenotificationdispatchsource.md)
- [IOSimpleReporter](iosimplereporter.md)
- [IOStateReporter](iostatereporter.md)
- [OSBundle](osbundle.md)
- [OSMappedFile](osmappedfile.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter)*