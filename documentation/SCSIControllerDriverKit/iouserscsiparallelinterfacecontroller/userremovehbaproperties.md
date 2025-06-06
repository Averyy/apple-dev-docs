# UserRemoveHBAProperties

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Removes properties from a host bus adapter in response to a call from the framework.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserRemoveHBAProperties(OSArray * properties);
```

#### Return Value

A value that indicates the result of removing the properties. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

Your driver extension calls this method to remove properties from the HBA. The `properties` directory can contain the following keys:

- [`kIOPropertyVendorNameKey`](https://developer.apple.com/documentation/iokit/kiopropertyvendornamekey)
- [`kIOPropertyProductNameKey`](https://developer.apple.com/documentation/iokit/kiopropertyproductnamekey)
- [`kIOPropertyProductRevisionLevelKey`](https://developer.apple.com/documentation/iokit/kiopropertyproductrevisionlevelkey)
- [`kIOPropertyPortDescriptionKey`](https://developer.apple.com/documentation/kernel/kiopropertyportdescriptionkey)
- [`kIOPropertyPortSpeedKey`](https://developer.apple.com/documentation/kernel/kiopropertyportspeedkey)
- [`kIOPropertyPortTopologyKey`](https://developer.apple.com/documentation/kernel/kiopropertyporttopologykey)
- [`kIOPropertySCSIParallelSignalingTypeKey`](https://developer.apple.com/documentation/kernel/kiopropertyscsiparallelsignalingtypekey)
- [`kIOPropertyFibreChannelCableDescriptionKey`](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelcabledescriptionkey)
- [`kIOPropertyFibreChannelNodeWorldWideNameKey`](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelnodeworldwidenamekey)
- [`kIOPropertyFibreChannelPortWorldWideNameKey`](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelportworldwidenamekey)
- [`kIOPropertyFibreChannelAddressIdentifierKey`](https://developer.apple.com/documentation/kernel/kiopropertyfibrechanneladdressidentifierkey)
- [`kIOPropertyFibreChannelALPAKey`](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelalpakey)
- [`kIOPropertySASAddressKey`](https://developer.apple.com/documentation/kernel/kiopropertysasaddresskey)

## Parameters

- `properties`: An array containing keys of the properties to remove.

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
- [UserReportHBAConstraints](iouserscsiparallelinterfacecontroller/userreporthbaconstraints.md)
  Reports the I/O constraints for this controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userremovehbaproperties)*