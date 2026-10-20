# UserSetHBAProperties

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets multiple properties for a host bus adapter.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t UserSetHBAProperties(OSDictionary *properties);
```

#### Return Value

A value that indicates the result of setting the properties. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

#### Discussion

Your driver extension calls this method to set properties on the HBA. The `properties` directory can contain the following keys:

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

The value of each property should be a pointer to a valid [`OSString`](../../DriverKit/osstring.md) object that represents the value for the property. The value must be of the proper type and size for the specified key.

## Parameters

- `properties`: A dictionary containing key-value pairs of properties.

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
- [UserRemoveHBAProperties](./userremovehbaproperties.md)
  Removes properties from a host bus adapter in response to a call from the framework.
- [UserReportHBAConstraints](./userreporthbaconstraints.md)
  Reports the I/O constraints for this controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usersethbaproperties)*