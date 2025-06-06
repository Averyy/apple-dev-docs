# kSCSITaskStatus_No_Status

**Framework**: DriverKit  
**Kind**: case

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kSCSITaskStatus_No_Status
```

#### Discussion

This status is not defined by the SCSI specifications, but is here to provide a status that can be returned in cases where there is not status available from the device or protocol, for example, when the service response is neither TASK_COMPLETED nor LINK_COMMAND_COMPLETE or when the service response is SERVICE_DELIVERY_OR_TARGET_FAILURE and the reason for failure could not be determined.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/scsitaskstatus/kscsitaskstatus_no_status)*