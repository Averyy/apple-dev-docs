# UserReportHBAConstraints

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Reports the I/O constraints for this controller.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t UserReportHBAConstraints(OSDictionary *constraints);
```

## Return Value

A value that indicates the result of reporting the HBA constraints. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

## Discussion

The valid keys for the `constraints` dictionary are as follows:

| Key name | Required? |
| --- | --- |
| [`kIOMaximumSegmentCountReadKey`](../../iokit/kiomaximumsegmentcountreadkey.md) | Yes |
| [`kIOMaximumSegmentCountWriteKey`](../../iokit/kiomaximumsegmentcountwritekey.md) | Yes |
| [`kIOMaximumSegmentByteCountReadKey`](../../iokit/kiomaximumsegmentbytecountreadkey.md) | Yes |
| [`kIOMaximumSegmentByteCountWriteKey`](../../iokit/kiomaximumsegmentbytecountwritekey.md) | Yes |
| [`kIOMinimumSegmentAlignmentByteCountKey`](../../iokit/kiominimumsegmentalignmentbytecountkey.md) | Yes |
| [`kIOMaximumSegmentAddressableBitCountKey`](../../iokit/kiomaximumsegmentaddressablebitcountkey.md) | Yes |
| `kIOMinimumHBADataAlignmentMaskKey` | Yes |
| `kIOHierarchicalLogicalUnitSupportKey` | No |

Make sure your dext reports these constraints accurately — particularly all mandatory keys — during initialization. This helps prevent intermittent failures, such as controller firmware buffer overflows.

Subclasses must call this method from the dext before [`UserInitializeController`](./userinitializecontroller.md) returns.

If the controller has global transfer limits, set the properties [`kIOMaximumByteCountReadKey`](../../DriverKit/kiomaximumbytecountreadkey.md) and [`kIOMaximumByteCountWriteKey`](../../DriverKit/kiomaximumbytecountwritekey.md) on the dext, using the [`SetProperties`](../../DriverKit/ioservice/setproperties.md) method inherited from [`IOService`](../../DriverKit/ioservice.md). The `UserReportHBAConstraints` method doesn’t currently support these properties.

## Parameters

- `constraints`: A dictionary containing I/O constraint keys, and Boolean values indicating that the device supports the constraint. See the discussion for valid and required keys.

## See Also

### Managing host bus adapters
- [UserReportInitiatorIdentifier](./userreportinitiatoridentifier.md)
  Gets the SCSI device identifier for the host bus adapter (HBA) in response to a call from the framework.
- [UserReportHighestSupportedDeviceID](./userreporthighestsupporteddeviceid.md)
  Gets the highest supported SCSI device identifier in response to a call from the framework.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userreporthbaconstraints)*