# UserDoesHBASupportMultiPathing

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Queries the HBA child class to determine if it supports multipathing in response to a call from the framework.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserDoesHBASupportMultiPathing(bool * result);
```

#### Return Value

A value that indicates the result of determining if the driver extension class supports multipathing. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

## Parameters

- `result`: A pointer to a Boolean value. On return, set this value to   if the HBA supports multipathing, and   if it doesn’t.

## See Also

- [UserReportInitiatorIdentifier](iouserscsiparallelinterfacecontroller/userreportinitiatoridentifier.md)
  Gets the SCSI device identifier for the host bus adapter (HBA) in response to a call from the framework.
- [UserReportHighestSupportedDeviceID](iouserscsiparallelinterfacecontroller/userreporthighestsupporteddeviceid.md)
  Gets the highest supported SCSI device identifier in response to a call from the framework.
- [UserReportMaximumTaskCount](iouserscsiparallelinterfacecontroller/userreportmaximumtaskcount.md)
  Gets the maximum number of outstanding tasks the HBA can process in response to a call from the framework.
- [UserDoesHBAPerformDeviceManagement](iouserscsiparallelinterfacecontroller/userdoeshbaperformdevicemanagement.md)
  Determines if the host bus adapter (HBA) manages devices in response to a call from the framework.
- [UserReportHBAHighestLogicalUnitNumber](iouserscsiparallelinterfacecontroller/userreporthbahighestlogicalunitnumber.md)
  Gets the highest logical unit number (LUN) in response to a call from the framework.
- [UserDoesHBAPerformAutoSense](iouserscsiparallelinterfacecontroller/userdoeshbaperformautosense.md)
  Determines if the driver extension class automatically performs autosense and provides autosense data for each I/O in response to a call from the framework.
- [UserDoesHBASupportSCSIParallelFeature](iouserscsiparallelinterfacecontroller/userdoeshbasupportscsiparallelfeature.md)
  Determines whether the driver extension class supports a specific feature in response to a call from the framework.
- [SCSIParallelFeature](scsiparallelfeature.md)
  A feature that the driver extension supports.
- [UserMapHBAData](iouserscsiparallelinterfacecontroller/usermaphbadata.md)
  Maps any host bus adapter (HBA)-specific task data in response to a call from the framework.
- [UserSetHBAProperties](iouserscsiparallelinterfacecontroller/usersethbaproperties.md)
  Sets multiple properties for a host bus adapter.
- [UserRemoveHBAProperties](iouserscsiparallelinterfacecontroller/userremovehbaproperties.md)
  Removes properties from a host bus adapter in response to a call from the framework.
- [UserReportHBAConstraints](iouserscsiparallelinterfacecontroller/userreporthbaconstraints.md)
  Reports the I/O constraints for this controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userdoeshbasupportmultipathing)*