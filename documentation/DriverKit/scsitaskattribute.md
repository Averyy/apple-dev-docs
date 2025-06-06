# SCSITaskAttribute

**Framework**: DriverKit  
**Kind**: enum

Attributes for task delivery.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef enum SCSITaskAttribute : unsigned int { ... } SCSITaskAttribute;
```

#### Overview

The Task Attribute defines how this task should be managed when determing order for queueing and submission to the appropriate device server. The Task Attribute is set by the SCSI Application Layer and cannot be modified by the SCSI Protocol Layer.

## Topics

### Constants
- [kSCSITask_SIMPLE](scsitaskattribute/kscsitask_simple.md)
- [kSCSITask_ORDERED](scsitaskattribute/kscsitask_ordered.md)
- [kSCSITask_HEAD_OF_QUEUE](scsitaskattribute/kscsitask_head_of_queue.md)
- [kSCSITask_ACA](scsitaskattribute/kscsitask_aca.md)

## See Also

- [IOLockAssertState](iolockassertstate.md)
- [IORWLockAssertState](iorwlockassertstate.md)
- [kC0DataMaxStringLen](kc0datamaxstringlen.md)
- [kINQUIRY_ANSI_VERSION_Mask](kinquiry_ansi_version_mask.md)
- [kINQUIRY_ANSI_VERSION_NoClaimedConformance](kinquiry_ansi_version_noclaimedconformance.md)
- [kINQUIRY_ANSI_VERSION_SCSI_1_Compliant](kinquiry_ansi_version_scsi_1_compliant.md)
- [kINQUIRY_ANSI_VERSION_SCSI_2_Compliant](kinquiry_ansi_version_scsi_2_compliant.md)
- [kINQUIRY_ANSI_VERSION_SCSI_SPC_2_Compliant](kinquiry_ansi_version_scsi_spc_2_compliant.md)
- [kINQUIRY_ANSI_VERSION_SCSI_SPC_3_Compliant](kinquiry_ansi_version_scsi_spc_3_compliant.md)
- [kINQUIRY_ANSI_VERSION_SCSI_SPC_Compliant](kinquiry_ansi_version_scsi_spc_compliant.md)
- [kINQUIRY_Byte3_AERC_Bit](kinquiry_byte3_aerc_bit.md)
- [kINQUIRY_Byte3_AERC_Mask](kinquiry_byte3_aerc_mask.md)
- [kINQUIRY_Byte3_HISUP_Bit](kinquiry_byte3_hisup_bit.md)
- [kINQUIRY_Byte3_HISUP_Mask](kinquiry_byte3_hisup_mask.md)
- [kINQUIRY_Byte3_NORMACA_Bit](kinquiry_byte3_normaca_bit.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/scsitaskattribute)*