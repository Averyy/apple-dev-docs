# mach_timebase_info

**Framework**: DriverKit  
**Kind**: struct

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
struct mach_timebase_info;
```

#### Overview

In general prefer to use the <time.h> API clock_gettime_nsec_np(3), which deals in the same clocks (and more) in ns units. Conversion of ns to (resp. from) tick units as returned by the mach time APIs is performed by division (resp. multiplication) with the fraction returned by mach_timebase_info().

## Topics

### Instance Properties
- [denom](mach_timebase_info-c.struct/denom.md)
- [numer](mach_timebase_info-c.struct/numer.md)

## See Also

- [IODMACommandSpecification](iodmacommandspecification.md)
- [IOHistogramReportValues](iohistogramreportvalues.md)
- [IOHistogramSegmentConfig](iohistogramsegmentconfig.md)
- [IONormDistReportValues](ionormdistreportvalues.md)
- [IORPCMessageErrorReturnContent](iorpcmessageerrorreturncontent.md)
- [IOReportChannel](ioreportchannel.md)
- [IOReportChannelList](ioreportchannellist.md)
- [IOReportChannelType](ioreportchanneltype.md)
- [IOReportElement](ioreportelement.md)
- [IOReportElementValues](ioreportelementvalues.md)
- [IOReportInterest](ioreportinterest.md)
- [IOReportInterestList](ioreportinterestlist.md)
- [IOSimpleArrayReportValues](iosimplearrayreportvalues.md)
- [IOSimpleReportValues](iosimplereportvalues.md)
- [IOStateReportValues](iostatereportvalues.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/mach_timebase_info-c.struct)*