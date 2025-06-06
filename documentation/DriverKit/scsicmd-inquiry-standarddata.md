# SCSICmd_INQUIRY_StandardData

**Framework**: DriverKit  
**Kind**: struct

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef struct SCSICmd_INQUIRY_StandardData { ... } SCSICmd_INQUIRY_StandardData;
```

#### Overview

This structure defines the format of the required standard data that is returned for the INQUIRY command.  This is the data that is required to be returned from all devices.

## Topics

### Instance Properties
- [ADDITIONAL_LENGTH](scsicmd_inquiry_standarddata/additional_length.md)
- [PERIPHERAL_DEVICE_TYPE](scsicmd_inquiry_standarddata/peripheral_device_type.md)
- [PRODUCT_IDENTIFICATION](scsicmd_inquiry_standarddata/product_identification.md)
- [PRODUCT_REVISION_LEVEL](scsicmd_inquiry_standarddata/product_revision_level.md)
- [RESPONSE_DATA_FORMAT](scsicmd_inquiry_standarddata/response_data_format.md)
- [RMB](scsicmd_inquiry_standarddata/rmb.md)
- [SCCSReserved](scsicmd_inquiry_standarddata/sccsreserved.md)
- [VENDOR_IDENTIFICATION](scsicmd_inquiry_standarddata/vendor_identification.md)
- [VERSION](scsicmd_inquiry_standarddata/version.md)
- [flags1](scsicmd_inquiry_standarddata/flags1.md)
- [flags2](scsicmd_inquiry_standarddata/flags2.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/scsicmd_inquiry_standarddata)*