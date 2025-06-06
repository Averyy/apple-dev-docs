# UserReportHBAConstraints

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Reports the I/O constraints for this controller.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserReportHBAConstraints(OSDictionary * constraints);
```

#### Return Value

A value that indicates the result of reporting the HBA constraints. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

The valid keys for the `constraints` dictionary are as follows:

| Key name | Required? |
| --- | --- |
| [`kIOMaximumSegmentCountReadKey`](https://developer.apple.com/documentation/iokit/kiomaximumsegmentcountreadkey) | Yes |
| [`kIOMaximumSegmentCountWriteKey`](https://developer.apple.com/documentation/iokit/kiomaximumsegmentcountwritekey) | Yes |
| [`kIOMaximumSegmentByteCountReadKey`](https://developer.apple.com/documentation/iokit/kiomaximumsegmentbytecountreadkey) | Yes |
| [`kIOMaximumSegmentByteCountWriteKey`](https://developer.apple.com/documentation/iokit/kiomaximumsegmentbytecountwritekey) | Yes |
| [`kIOMinimumSegmentAlignmentByteCountKey`](https://developer.apple.com/documentation/iokit/kiominimumsegmentalignmentbytecountkey) | Yes |
| [`kIOMaximumSegmentAddressableBitCountKey`](https://developer.apple.com/documentation/iokit/kiomaximumsegmentaddressablebitcountkey) | Yes |
| `kIOMinimumHBADataAlignmentMaskKey` | Yes |
| `kIOHierarchicalLogicalUnitSupportKey` | No |

Subclasses must call this method from the dext before [`UserInitializeController`](iouserscsiparallelinterfacecontroller/userinitializecontroller.md) returns.

## Parameters

- `constraints`: A dictionary containing I/O constraint keys, and Boolean values indicating that the device supports the constraint. See the discussion for valid and required keys.

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
- [UserDoesHBASupportMultiPathing](iouserscsiparallelinterfacecontroller/userdoeshbasupportmultipathing.md)
  Queries the HBA child class to determine if it supports multipathing in response to a call from the framework.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userreporthbaconstraints)*