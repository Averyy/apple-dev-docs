# kSCSITaskStatus_TaskTimeoutOccurred

**Framework**: DriverKit  
**Kind**: case  
**Role**: Enumeration Case

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
kSCSITaskStatus_TaskTimeoutOccurred
```

#### Discussion

If a task is aborted by the SCSI Protocol Layer due to it exceeding the timeout value specified by the task, the task status shall be set to kSCSITaskStatus_TaskTimeoutOccurred.

## See Also

### Constants
- [kSCSITaskStatus_GOOD](./kscsitaskstatus_good.md)
- [kSCSITaskStatus_CHECK_CONDITION](./kscsitaskstatus_check_condition.md)
- [kSCSITaskStatus_CONDITION_MET](./kscsitaskstatus_condition_met.md)
- [kSCSITaskStatus_BUSY](./kscsitaskstatus_busy.md)
- [kSCSITaskStatus_INTERMEDIATE](./kscsitaskstatus_intermediate.md)
- [kSCSITaskStatus_INTERMEDIATE_CONDITION_MET](./kscsitaskstatus_intermediate_condition_met.md)
- [kSCSITaskStatus_RESERVATION_CONFLICT](./kscsitaskstatus_reservation_conflict.md)
- [kSCSITaskStatus_TASK_SET_FULL](./kscsitaskstatus_task_set_full.md)
- [kSCSITaskStatus_ACA_ACTIVE](./kscsitaskstatus_aca_active.md)
- [kSCSITaskStatus_ProtocolTimeoutOccurred](./kscsitaskstatus_protocoltimeoutoccurred.md)
- [kSCSITaskStatus_DeviceNotResponding](./kscsitaskstatus_devicenotresponding.md)
- [kSCSITaskStatus_DeviceNotPresent](./kscsitaskstatus_devicenotpresent.md)
- [kSCSITaskStatus_DeliveryFailure](./kscsitaskstatus_deliveryfailure.md)
- [kSCSITaskStatus_No_Status](./kscsitaskstatus_no_status.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/scsitaskstatus/kscsitaskstatus_tasktimeoutoccurred)*