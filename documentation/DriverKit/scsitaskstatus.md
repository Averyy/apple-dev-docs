# SCSITaskStatus

**Framework**: DriverKit  
**Kind**: enum

Attributes for task status.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef enum SCSITaskStatus : unsigned int { ... } SCSITaskStatus;
```

#### Overview

The Task Status represents the completion status of the task which provides the SCSI Application Layer with additional information about how to procede in handling a completed task.

The SCSI Architecture Model specification only defines task status values for when a task completes with a service response of either TASK_COMPLETED or LINK_COMMAND_COMPLETE.

Since additional information will aid in error recovery when a task fails to be completed by a device due to a service response of kSCSIServiceResponse_SERVICE_DELIVERY_OR_TARGET_FAILURE, additional values have been defined that can be returned by the SCSI Protocol Layer to inform the SCSI Application Layer of the cause of the delivery failure.

The Task Status can only be modified by the SCSI Protocol Layer. The SCSI Application Layer can only read the status

## Topics

### Constants
- [kSCSITaskStatus_GOOD](scsitaskstatus/kscsitaskstatus_good.md)
- [kSCSITaskStatus_CHECK_CONDITION](scsitaskstatus/kscsitaskstatus_check_condition.md)
- [kSCSITaskStatus_CONDITION_MET](scsitaskstatus/kscsitaskstatus_condition_met.md)
- [kSCSITaskStatus_BUSY](scsitaskstatus/kscsitaskstatus_busy.md)
- [kSCSITaskStatus_INTERMEDIATE](scsitaskstatus/kscsitaskstatus_intermediate.md)
- [kSCSITaskStatus_INTERMEDIATE_CONDITION_MET](scsitaskstatus/kscsitaskstatus_intermediate_condition_met.md)
- [kSCSITaskStatus_RESERVATION_CONFLICT](scsitaskstatus/kscsitaskstatus_reservation_conflict.md)
- [kSCSITaskStatus_TASK_SET_FULL](scsitaskstatus/kscsitaskstatus_task_set_full.md)
- [kSCSITaskStatus_ACA_ACTIVE](scsitaskstatus/kscsitaskstatus_aca_active.md)
- [kSCSITaskStatus_TaskTimeoutOccurred](scsitaskstatus/kscsitaskstatus_tasktimeoutoccurred.md)
- [kSCSITaskStatus_ProtocolTimeoutOccurred](scsitaskstatus/kscsitaskstatus_protocoltimeoutoccurred.md)
- [kSCSITaskStatus_DeviceNotResponding](scsitaskstatus/kscsitaskstatus_devicenotresponding.md)
- [kSCSITaskStatus_DeviceNotPresent](scsitaskstatus/kscsitaskstatus_devicenotpresent.md)
- [kSCSITaskStatus_DeliveryFailure](scsitaskstatus/kscsitaskstatus_deliveryfailure.md)
- [kSCSITaskStatus_No_Status](scsitaskstatus/kscsitaskstatus_no_status.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/scsitaskstatus)*