# SCSICmd_INQUIRY_PageB0_Data

**Framework**: DriverKit  
**Kind**: struct

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef struct SCSICmd_INQUIRY_PageB0_Data { ... } SCSICmd_INQUIRY_PageB0_Data;
```

#### Overview

INQUIRY Page B0h data as defined in the SBC specification. This section contains all structures and definitions used by the INQUIRY command in response to a request for page B0h - Block Limits VPD Page.

## Topics

### Instance Properties
- [ATOMIC_ALIGNMENT](scsicmd_inquiry_pageb0_data/atomic_alignment.md)
- [ATOMIC_TRANSFER_LENGTH_GRANULARITY](scsicmd_inquiry_pageb0_data/atomic_transfer_length_granularity.md)
- [MAXIMUM_ATOMIC_BOUNDARY_SIZE](scsicmd_inquiry_pageb0_data/maximum_atomic_boundary_size.md)
- [MAXIMUM_ATOMIC_TRANSFER_LENGTH](scsicmd_inquiry_pageb0_data/maximum_atomic_transfer_length.md)
- [MAXIMUM_ATOMIC_TRANSFER_LENGTH_WITH_ATOMIC_BOUNDARY](scsicmd_inquiry_pageb0_data/maximum_atomic_transfer_length_with_atomic_boundary.md)
- [MAXIMUM_COMPARE_AND_WRITE_LENGTH](scsicmd_inquiry_pageb0_data/maximum_compare_and_write_length.md)
- [MAXIMUM_PREFETCH_LENGTH](scsicmd_inquiry_pageb0_data/maximum_prefetch_length.md)
- [MAXIMUM_TRANSFER_LENGTH](scsicmd_inquiry_pageb0_data/maximum_transfer_length.md)
- [MAXIMUM_UNMAP_BLOCK_DESCRIPTOR_COUNT](scsicmd_inquiry_pageb0_data/maximum_unmap_block_descriptor_count.md)
- [MAXIMUM_UNMAP_LBA_COUNT](scsicmd_inquiry_pageb0_data/maximum_unmap_lba_count.md)
- [MAXIMUM_WRITE_SAME_LENGTH](scsicmd_inquiry_pageb0_data/maximum_write_same_length.md)
- [OPTIMAL_TRANSFER_LENGTH](scsicmd_inquiry_pageb0_data/optimal_transfer_length.md)
- [OPTIMAL_TRANSFER_LENGTH_GRANULARITY](scsicmd_inquiry_pageb0_data/optimal_transfer_length_granularity.md)
- [OPTIMAL_UNMAP_GRANULARITY](scsicmd_inquiry_pageb0_data/optimal_unmap_granularity.md)
- [PAGE_CODE](scsicmd_inquiry_pageb0_data/page_code.md)
- [PAGE_LENGTH](scsicmd_inquiry_pageb0_data/page_length.md)
- [PERIPHERAL_DEVICE_TYPE](scsicmd_inquiry_pageb0_data/peripheral_device_type.md)
- [UNMAP_GRANULARITY_ALIGNMENT](scsicmd_inquiry_pageb0_data/unmap_granularity_alignment.md)
- [WSNZ](scsicmd_inquiry_pageb0_data/wsnz.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/scsicmd_inquiry_pageb0_data)*