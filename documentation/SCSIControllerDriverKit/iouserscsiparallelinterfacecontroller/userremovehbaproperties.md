# UserRemoveHBAProperties

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Removes properties from a host bus adapter in response to a call from the framework.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t UserRemoveHBAProperties(OSArray *properties);
```

#### Return Value

A value that indicates the result of removing the properties. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

#### Discussion

Your driver extension calls this method to remove properties from the HBA. The `properties` directory can contain the following keys:

- [`kIOPropertyVendorNameKey`](../../iokit/kiopropertyvendornamekey.md)
- [`kIOPropertyProductNameKey`](../../iokit/kiopropertyproductnamekey.md)
- [`kIOPropertyProductRevisionLevelKey`](../../iokit/kiopropertyproductrevisionlevelkey.md)
- [`kIOPropertyPortDescriptionKey`](../../kernel/kiopropertyportdescriptionkey.md)
- [`kIOPropertyPortSpeedKey`](../../kernel/kiopropertyportspeedkey.md)
- [`kIOPropertyPortTopologyKey`](../../kernel/kiopropertyporttopologykey.md)
- [`kIOPropertySCSIParallelSignalingTypeKey`](../../kernel/kiopropertyscsiparallelsignalingtypekey.md)
- [`kIOPropertyFibreChannelCableDescriptionKey`](../../kernel/kiopropertyfibrechannelcabledescriptionkey.md)
- [`kIOPropertyFibreChannelNodeWorldWideNameKey`](../../kernel/kiopropertyfibrechannelnodeworldwidenamekey.md)
- [`kIOPropertyFibreChannelPortWorldWideNameKey`](../../kernel/kiopropertyfibrechannelportworldwidenamekey.md)
- [`kIOPropertyFibreChannelAddressIdentifierKey`](../../kernel/kiopropertyfibrechanneladdressidentifierkey.md)
- [`kIOPropertyFibreChannelALPAKey`](../../kernel/kiopropertyfibrechannelalpakey.md)
- [`kIOPropertySASAddressKey`](../../kernel/kiopropertysasaddresskey.md)

## Parameters

- `properties`: An array containing keys of the properties to remove.

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
- [UserReportHBAConstraints](./userreporthbaconstraints.md)
  Reports the I/O constraints for this controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userremovehbaproperties)*