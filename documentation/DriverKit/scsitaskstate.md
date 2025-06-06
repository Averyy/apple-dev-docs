# SCSITaskState

**Framework**: DriverKit  
**Kind**: enum

Attributes for task state.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef enum SCSITaskState : unsigned int { ... } SCSITaskState;
```

#### Overview

The Task State represents the current state of the task. The state is set to NEW_TASK when the task is created. The SCSI Protocol Layer will then adjust the state as the task is queued and during execution. The SCSI Application Layer can examine the state to monitor the progress of a task. The Task State can only be modified by the SCSI Protocol Layer. The SCSI Application Layer can only read the state.

## Topics

### Constants
- [kSCSITaskState_NEW_TASK](scsitaskstate/kscsitaskstate_new_task.md)
- [kSCSITaskState_ENABLED](scsitaskstate/kscsitaskstate_enabled.md)
- [kSCSITaskState_BLOCKED](scsitaskstate/kscsitaskstate_blocked.md)
- [kSCSITaskState_DORMANT](scsitaskstate/kscsitaskstate_dormant.md)
- [kSCSITaskState_ENDED](scsitaskstate/kscsitaskstate_ended.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/scsitaskstate)*