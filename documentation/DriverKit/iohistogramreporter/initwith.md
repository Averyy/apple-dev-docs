# initWith

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
bool initWith(IOService *reportingService, IOReportCategories categories, uint64_t channelID, const char *channelName, IOReportUnit unit, int nSegments, IOHistogramSegmentConfig *config);
```

## See Also

### Instance Methods
- [addChannel](./addchannel.md)
- [overrideBucketValues](./overridebucketvalues.md)
- [tallyValue](./tallyvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iohistogramreporter/initwith)*