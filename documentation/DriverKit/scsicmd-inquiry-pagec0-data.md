# SCSICmd_INQUIRY_PageC0_Data

**Framework**: DriverKit  
**Kind**: struct

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef struct SCSICmd_INQUIRY_PageC0_Data { ... } SCSICmd_INQUIRY_PageC0_Data;
```

#### Overview

Disk Mode specification. This is a vendor specific data structure. This section contains all structures and definitions used by the INQUIRY command in response to a request for page C0h.

## Topics

### Instance Properties
- [fEncryptionType](scsicmd_inquiry_pagec0_data/fencryptiontype.md)
- [fFeatures](scsicmd_inquiry_pagec0_data/ffeatures.md)
- [fHeader](scsicmd_inquiry_pagec0_data/fheader.md)
- [fInstalledRAMSize](scsicmd_inquiry_pagec0_data/finstalledramsize.md)
- [fMacModelId](scsicmd_inquiry_pagec0_data/fmacmodelid.md)
- [fMaxReadSize](scsicmd_inquiry_pagec0_data/fmaxreadsize.md)
- [fMaxWriteSize](scsicmd_inquiry_pagec0_data/fmaxwritesize.md)
- [fNativeBlockSize](scsicmd_inquiry_pagec0_data/fnativeblocksize.md)
- [fPreferredIOSize](scsicmd_inquiry_pagec0_data/fpreferrediosize.md)
- [fReserved1](scsicmd_inquiry_pagec0_data/freserved1.md)
- [fReserved2](scsicmd_inquiry_pagec0_data/freserved2.md)
- [fReserved3](scsicmd_inquiry_pagec0_data/freserved3.md)
- [fSerialNumber](scsicmd_inquiry_pagec0_data/fserialnumber.md)
- [fTdmPageVersion](scsicmd_inquiry_pagec0_data/ftdmpageversion.md)
- [fTdmProtocolVersion](scsicmd_inquiry_pagec0_data/ftdmprotocolversion.md)
- [fWorkArounds](scsicmd_inquiry_pagec0_data/fworkarounds.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/scsicmd_inquiry_pagec0_data)*