# SCSICmd_INQUIRY_StandardDataAll

**Framework**: DriverKit  
**Kind**: struct

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef struct SCSICmd_INQUIRY_StandardDataAll { ... } SCSICmd_INQUIRY_StandardDataAll;
```

#### Overview

This structure defines the all of the fields that can be returned in repsonse to the INQUIRy request for the standard data.  There is no requirement as to how much of the additional data must be returned by a device.

## Topics

### Instance Properties
- [ADDITIONAL_LENGTH](scsicmd_inquiry_standarddataall/additional_length.md)
- [PERIPHERAL_DEVICE_TYPE](scsicmd_inquiry_standarddataall/peripheral_device_type.md)
- [PRODUCT_IDENTIFICATION](scsicmd_inquiry_standarddataall/product_identification.md)
- [PRODUCT_REVISION_LEVEL](scsicmd_inquiry_standarddataall/product_revision_level.md)
- [RESPONSE_DATA_FORMAT](scsicmd_inquiry_standarddataall/response_data_format.md)
- [RMB](scsicmd_inquiry_standarddataall/rmb.md)
- [Reserved1](scsicmd_inquiry_standarddataall/reserved1.md)
- [Reserved2](scsicmd_inquiry_standarddataall/reserved2.md)
- [SCCSReserved](scsicmd_inquiry_standarddataall/sccsreserved.md)
- [VENDOR_IDENTIFICATION](scsicmd_inquiry_standarddataall/vendor_identification.md)
- [VERSION](scsicmd_inquiry_standarddataall/version.md)
- [VERSION_DESCRIPTOR](scsicmd_inquiry_standarddataall/version_descriptor.md)
- [VendorSpecific1](scsicmd_inquiry_standarddataall/vendorspecific1.md)
- [VendorSpecific2](scsicmd_inquiry_standarddataall/vendorspecific2.md)
- [flags1](scsicmd_inquiry_standarddataall/flags1.md)
- [flags2](scsicmd_inquiry_standarddataall/flags2.md)
- [flags3](scsicmd_inquiry_standarddataall/flags3.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/scsicmd_inquiry_standarddataall)*