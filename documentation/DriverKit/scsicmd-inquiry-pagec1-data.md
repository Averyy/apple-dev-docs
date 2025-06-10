# SCSICmd_INQUIRY_PageC1_Data

**Framework**: DriverKit  
**Kind**: struct

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef struct SCSICmd_INQUIRY_PageC1_Data { ... } SCSICmd_INQUIRY_PageC1_Data;
```

#### Overview

INQUIRY Page C1h data as defined in Apple Target Disk Mode specification. This is a vendor specific data structure. This section contains all structures and definitions used by the INQUIRY command in response to a request for page C1h.

## Topics

### Instance Properties
- [fHeader](scsicmd_inquiry_pagec1_data/fheader.md)
- [fPowerRequired](scsicmd_inquiry_pagec1_data/fpowerrequired.md)
- [fReserved1](scsicmd_inquiry_pagec1_data/freserved1.md)
- [fReserved2](scsicmd_inquiry_pagec1_data/freserved2.md)
- [fTdmPowerRequirementsPageVersion](scsicmd_inquiry_pagec1_data/ftdmpowerrequirementspageversion.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/scsicmd_inquiry_pagec1_data)*