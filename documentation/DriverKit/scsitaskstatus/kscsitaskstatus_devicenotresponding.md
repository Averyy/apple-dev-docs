# kSCSITaskStatus_DeviceNotResponding

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
kSCSITaskStatus_DeviceNotResponding
```

## Discussion

If a task is unable to be delivered due to a failure of the device not accepting the task or the device acknowledging the attempt to send it the device the task status shall be set to kSCSITaskStatus_DeviceNotResponding. This will allow the SCSI Application driver to perform the necessary steps to try to recover the device. This shall only be reported after the SCSI Protocol Layer driver has attempted all protocol specific attempts to recover the device.

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
- [kSCSITaskStatus_TaskTimeoutOccurred](./kscsitaskstatus_tasktimeoutoccurred.md)
- [kSCSITaskStatus_ProtocolTimeoutOccurred](./kscsitaskstatus_protocoltimeoutoccurred.md)
- [kSCSITaskStatus_DeviceNotPresent](./kscsitaskstatus_devicenotpresent.md)
- [kSCSITaskStatus_DeliveryFailure](./kscsitaskstatus_deliveryfailure.md)
- [kSCSITaskStatus_No_Status](./kscsitaskstatus_no_status.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/scsitaskstatus/kscsitaskstatus_devicenotresponding)*