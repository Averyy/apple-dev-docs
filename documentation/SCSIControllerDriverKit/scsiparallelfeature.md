# SCSIParallelFeature

**Framework**: SCSIControllerDriverKit  
**Kind**: enum

A feature that the driver extension supports.

**Availability**:
- DriverKit ?+

## Declaration

```swift
typedef enum SCSIParallelFeature : unsigned int { ... } SCSIParallelFeature;
```

#### Overview

This enumeration defines feature selectors the framework uses to identify features of the SCSI parallel interface. The [`UserDoesHBASupportSCSIParallelFeature`](iouserscsiparallelinterfacecontroller/userdoeshbasupportscsiparallelfeature.md) function uses these to report whether the HBA supports a SCSI parallel interface feature. The framework also uses these to request negotiation and report negotiation results between the controller and the device.

## Topics

### Feature selectors
- [kSCSIParallelFeature_WideDataTransfer](scsiparallelfeature/kscsiparallelfeature_widedatatransfer.md)
  The selector for support of wide data transfers.
- [kSCSIParallelFeature_SynchronousDataTransfer](scsiparallelfeature/kscsiparallelfeature_synchronousdatatransfer.md)
  The selector for support of synchronous data transfers.
- [kSCSIParallelFeature_QuickArbitrationAndSelection](scsiparallelfeature/kscsiparallelfeature_quickarbitrationandselection.md)
  The selector for support of quick arbitration and selection (QAS).
- [kSCSIParallelFeature_DoubleTransitionDataTransfers](scsiparallelfeature/kscsiparallelfeature_doubletransitiondatatransfers.md)
  The selector for support of double transition (DT) data transfers.
- [kSCSIParallelFeature_InformationUnitTransfers](scsiparallelfeature/kscsiparallelfeature_informationunittransfers.md)
  The selector for SPI information unit (IU) transfers.
- [kSCSIParallelFeature_TotalFeatureCount](scsiparallelfeature/kscsiparallelfeature_totalfeaturecount.md)
  The total number of supported features.

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
- [UserMapHBAData](iouserscsiparallelinterfacecontroller/usermaphbadata.md)
  Maps any host bus adapter (HBA)-specific task data in response to a call from the framework.
- [UserSetHBAProperties](iouserscsiparallelinterfacecontroller/usersethbaproperties.md)
  Sets multiple properties for a host bus adapter.
- [UserRemoveHBAProperties](iouserscsiparallelinterfacecontroller/userremovehbaproperties.md)
  Removes properties from a host bus adapter in response to a call from the framework.
- [UserReportHBAConstraints](iouserscsiparallelinterfacecontroller/userreporthbaconstraints.md)
  Reports the I/O constraints for this controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/scsiparallelfeature)*