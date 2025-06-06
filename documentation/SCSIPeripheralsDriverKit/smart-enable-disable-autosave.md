# SMART_Enable_Disable_AutoSave

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: func

Fills a Command Descriptor Block (CDB) to perform a SMART SCSI Command to enable or disable the autosave feature.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
bool SMART_Enable_Disable_AutoSave(SCSIDeviceOutParameters * request, bool enable, SCSIDeviceInParameters * response, UInt64 senseBufAddr);
```

#### Return Value

`true` if the call successfully fills the CDB; `false`, otherwise.

#### Discussion

Use this method in your dext to prefill a 16-byte CDB for the standard SMART SCSI Command to enable or disable the autosave feature.

## Parameters

- `request`: An object that contains the request information.
- `enable`:   to enable the autosave feature;   to disable.
- `response`: An empty   object. On return, the framework populates this object with the response information.
- `senseBufAddr`: The address of the sense buffer.

## See Also

- [SMART_Enable_Disable_Operations](smart_enable_disable_operations.md)
  Fills a Command Descriptor Block (CDB) to perform a SMART SCSI Command to enable or disable operations.
- [SMART_Return_Status](smart_return_status.md)
  Fills a Command Descriptor Block (CDB) to perform a SMART SCSI Command to return status.
- [SMART_Execute_Offline_Immediate](smart_execute_offline_immediate.md)
  Fills a Command Descriptor Block (CDB) to perform a SMART SCSI Command to execute an immediate offline test.
- [SMART_Read_Data](smart_read_data.md)
  Fills a Command Descriptor Block (CDB) to perform a SMART SCSI Command to read data.
- [SMART_Read_Data_Thresholds](smart_read_data_thresholds.md)
  Fills a Command Descriptor Block (CDB) to perform a SMART SCSI Command to read data thresholds.
- [SMART_Read_Log_At_Address](smart_read_log_at_address.md)
  Fills a Command Descriptor Block (CDB) to perform a SMART SCSI Command to read log data from an address.
- [SMART_Write_Log_At_Address](smart_write_log_at_address.md)
  Fills a Command Descriptor Block (CDB) to perform a SMART SCSI Command to write log data at an address.
- [SMART_Get_Identify_Data](smart_get_identify_data.md)
  Fills a Command Descriptor Block (CDB) to perform a SMART SCSI Command to get identify data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/smart_enable_disable_autosave)*