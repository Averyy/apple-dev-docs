# UserReportHighestSupportedDeviceID

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the highest supported SCSI device identifier in response to a call from the framework.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t UserReportHighestSupportedDeviceID(uint64_t *id);
```

## Return Value

A value that indicates the result of getting the identifier. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

## Discussion

The framework calls this method to determine the value of the highest SCSI device identifier that the HBA supports. The result of this call determines the last ID to process.

## Parameters

- `id`: A pointer to a device ID. On return, set this to the highest [`SCSIDeviceIdentifier`](../../iokit/scsideviceidentifier.md).

## See Also

### Managing host bus adapters
- [UserReportInitiatorIdentifier](./userreportinitiatoridentifier.md)
  Gets the SCSI device identifier for the host bus adapter (HBA) in response to a call from the framework.
- [UserReportMaximumTaskCount](./userreportmaximumtaskcount.md)
  Gets the maximum number of outstanding tasks the HBA can process in response to a call from the framework.
- [UserDoesHBAPerformDeviceManagement](./userdoeshbaperformdevicemanagement.md)
  Determines if the host bus adapter (HBA) manages devices in response to a call from the framework.
- [UserReportHBAHighestLogicalUnitNumber](./userreporthbahighestlogicalunitnumber.md)
  Gets the highest logical unit number (LUN) in response to a call from the framework.
- [UserDoesHBAPerformAutoSense](./userdoeshbaperformautosense.md)
  Determines if the driver extension class automatically performs autosense and provides autosense data for each I/O in response to a call from the framework.
- [UserDoesHBASupportMultiPathing](./userdoeshbasupportmultipathing.md)
  Queries the HBA child class to determine if it supports multipathing in response to a call from the framework.
- [UserDoesHBASupportSCSIParallelFeature](./userdoeshbasupportscsiparallelfeature.md)
  Determines whether the driver extension class supports a specific feature in response to a call from the framework.
- [SCSIParallelFeature](../scsiparallelfeature.md)
  A feature that the driver extension supports.
- [UserMapHBAData](./usermaphbadata.md)
  Maps any host bus adapter (HBA)-specific task data in response to a call from the framework.
- [UserSetHBAProperties](./usersethbaproperties.md)
  Sets multiple properties for a host bus adapter.
- [UserRemoveHBAProperties](./userremovehbaproperties.md)
  Removes properties from a host bus adapter in response to a call from the framework.
- [UserReportHBAConstraints](./userreporthbaconstraints.md)
  Reports the I/O constraints for this controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userreporthighestsupporteddeviceid)*