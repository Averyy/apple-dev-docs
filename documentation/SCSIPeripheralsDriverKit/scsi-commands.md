# SCSI commands

**Framework**: SCSIPeripheralsDriverKit

Call the framework’s free functions to populate Command Descriptor Blocks (CDBs) to send to your peripheral.

## Topics

### Creating common SCSI commands
- [TEST_UNIT_READY](test_unit_ready.md)
  Fills a Command Descriptor Block (CDB) to test whether the unit is ready.
- [INQUIRY](inquiry.md)
  Fills a Command Descriptor Block (CDB) to perform a SCSI inquiry.
- [REQUEST_SENSE](request_sense.md)
  Fills a Command Descriptor Block (CDB) to perform a SCSI sense-request command.
- [READ_10](read_10.md)
  Fills a Command Descriptor Block (CDB) to perform a SCSI read command.
- [WRITE_10](write_10.md)
  Fills a Command Descriptor Block (CDB) to perform a SCSI write command.
- [READ_CAPACITY](read_capacity.md)
  Fills a Command Descriptor Block (CDB) to perform a SCSI read-capacity command.
### Creating Self-Monitoring, Analysis and Reporting Technology (SMART) Commands
- [SMART_Enable_Disable_Operations](smart_enable_disable_operations.md)
  Fills a Command Descriptor Block (CDB) to perform a SMART SCSI Command to enable or disable operations.
- [SMART_Enable_Disable_AutoSave](smart_enable_disable_autosave.md)
  Fills a Command Descriptor Block (CDB) to perform a SMART SCSI Command to enable or disable the autosave feature.
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
### Creating arbitrary SCSI commands
- [SetCommandCDB](setcommandcdb.md)
  Fills a 16-byte Command Descriptor Block (CDB) with custom content.
### Supporting types
- [SCSIDeviceOutParameters](scsideviceoutparameters.md)
  A structure that contains parameters for an outbound request to a SCSI device.
- [SCSIDeviceInParameters](scsideviceinparameters.md)
  A structure that contains properties from an inbound response from a SCSI device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsi-commands)*