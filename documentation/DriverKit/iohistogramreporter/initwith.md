# initWith

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool initWith(IOService * reportingService, IOReportCategories categories, uint64_t channelID, const char * channelName, IOReportUnit unit, int nSegments, IOHistogramSegmentConfig * config);
```

## See Also

- [addChannel](iohistogramreporter/addchannel.md)
- [overrideBucketValues](iohistogramreporter/overridebucketvalues.md)
- [tallyValue](iohistogramreporter/tallyvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iohistogramreporter/initwith)*