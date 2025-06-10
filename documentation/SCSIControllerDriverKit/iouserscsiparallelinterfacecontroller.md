# IOUserSCSIParallelInterfaceController

**Framework**: SCSIControllerDriverKit  
**Kind**: class

A DriverKit provider object that manages communications with SCSI-based devices.

**Availability**:
- DriverKit ?+

## Declaration

```swift
class IOUserSCSIParallelInterfaceController;
```

#### Overview

Implement your driver by subclassing this class and overriding all pure virtual methods.

##### Specifying the Drivers Personality Information

When you subclass `IOUserSCSIParallelInterfaceController`, update the [`IOKitPersonalities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/IOKitPersonalities) key of your driver extension’s `Info.plist` file with information to match your driver to appropriate hardware. For this class, always include the keys and values in the following table:

| Key | Value |
| --- | --- |
| IOClass | `IOUserSCSIParallelInterfaceController` |
| IOUserClass | The name of your custom dext class. |
| IOProviderClass | `IOPCIDevice` |
| CFBundleIdentifierKernel | `com.apple.iokit.IOSCSIParallelFamily` |

##### Supporting Power Capabilities

IOUserSCSIParallelInterfaceController supports the following power capabilities:

- [`kIOServicePowerCapabilityOff`](https://developer.apple.com/documentation/DriverKit/kIOServicePowerCapabilityOff)
- [`kIOServicePowerCapabilityOn`](https://developer.apple.com/documentation/DriverKit/kIOServicePowerCapabilityOn)
- [`kIOServicePowerCapabilityPause`](kioservicepowercapabilitypause.md)

Implement the [`SetPowerState`](https://developer.apple.com/documentation/DriverKit/IOService/SetPowerState) method in your service object and use it to put your driver in a safe state for the new power setting. Call `super` either as the last step in your implementation, or when the dext is ready to acknowledge the power state transition.

The following code example implements [`SetPowerState`](https://developer.apple.com/documentation/DriverKit/IOService/SetPowerState) by performing a check to see if the new state is [`kIOServicePowerCapabilityOn`](https://developer.apple.com/documentation/DriverKit/kIOServicePowerCapabilityOn). If it is, the implementation calls a private `IssueHardReset()` method.

```objc
kern_return_t
IMPL ( ExampleSCSIDext, SetPowerState )
{
    
    kern_return_t ret = kIOReturnError;

    …

    if ( powerState == kIOServicePowerCapabilityOn )
    {
        ret = IssueHardReset ( );
 
        ivars->fCurrentPowerState = kIOServicePowerCapabilityOn;
    }

    return ret;

}
```

The hypothetical driver in this example still needs to acknowledge the power state change when it’s appropriate. For example, it could ensure a rescan has brought up all its targets, and then call `SetPowerState ( powerState, SUPERDISPATCH );`.

## Topics

### Managing Controllers
- [UserInitializeController](iouserscsiparallelinterfacecontroller/userinitializecontroller.md)
  Initializes the controller in response to a call from the framework.
- [UserStartController](iouserscsiparallelinterfacecontroller/userstartcontroller.md)
  Starts the controller in response to a call from the framework.
### Managing Tasks
- [UserProcessParallelTask](iouserscsiparallelinterfacecontroller/userprocessparalleltask.md)
  Processes a parallel task in response to a call from the framework.
- [SCSIUserParallelTask](scsiuserparalleltask.md)
  The properties of a parallel task to perform.
- [ParallelTaskCompletion](iouserscsiparallelinterfacecontroller/paralleltaskcompletion.md)
  Indicates to the system that the extension has completed an asynchronous request.
- [SCSIUserParallelResponse](scsiuserparallelresponse.md)
  The properties of a completed request.
### Managing Bundled Parallel Tasks
- [UserProcessBundledParallelTasks](iouserscsiparallelinterfacecontroller/userprocessbundledparalleltasks.md)
  Processes one or more parallel tasks in response to a call from the framework.
- [UserMapBundledParallelTaskCommandAndResponseBuffers](iouserscsiparallelinterfacecontroller/usermapbundledparalleltaskcommandandresponsebuffers.md)
  Maps the shared command and response buffers in the dext address space in response to a call from the framework.
- [BundledParallelTaskCompletion](iouserscsiparallelinterfacecontroller/bundledparalleltaskcompletion.md)
  Indicates to the system that the extension completed a bundled asynchronous request.
### Managing Targets
- [UserInitializeTargetForID](iouserscsiparallelinterfacecontroller/userinitializetargetforid.md)
  Initializes a target device in response to a call from the framework.
- [UserCreateTargetForID](iouserscsiparallelinterfacecontroller/usercreatetargetforid.md)
  Creates the specified target.
- [UserDestroyTargetForID](iouserscsiparallelinterfacecontroller/userdestroytargetforid.md)
  Destroys the specified target.
- [UserTargetPresentForID](iouserscsiparallelinterfacecontroller/usertargetpresentforid.md)
  Checks if a specific target is present.
- [UserSetTargetProperties](iouserscsiparallelinterfacecontroller/usersettargetproperties.md)
  Sets properties on the target.
- [UserRemoveTargetProperties](iouserscsiparallelinterfacecontroller/userremovetargetproperties.md)
  Removes properties from a target.
### Performing SCSI Standard Task Management
- [UserAbortTaskRequest](iouserscsiparallelinterfacecontroller/useraborttaskrequest.md)
  Aborts a single task.
- [UserAbortTaskSetRequest](iouserscsiparallelinterfacecontroller/useraborttasksetrequest.md)
  Aborts all tasks in a logical unit.
- [UserClearACARequest](iouserscsiparallelinterfacecontroller/userclearacarequest.md)
  Removes an autocontingent allegiance (ACA) attribute from a logical unit’s task set.
- [UserClearTaskSetRequest](iouserscsiparallelinterfacecontroller/usercleartasksetrequest.md)
  Aborts all tasks in a logical unit and clears their data.
- [UserLogicalUnitResetRequest](iouserscsiparallelinterfacecontroller/userlogicalunitresetrequest.md)
  Resets a logical unit.
- [UserTargetResetRequest](iouserscsiparallelinterfacecontroller/usertargetresetrequest.md)
  Resets a target.
### Managing Host Bus Adapters
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
- [UserReportHBAConstraints](iouserscsiparallelinterfacecontroller/userreporthbaconstraints.md)
  Reports the I/O constraints for this controller.
### Managing Direct Memory Access
- [UserGetDMASpecification](iouserscsiparallelinterfacecontroller/usergetdmaspecification.md)
  Gets the controller-specific direct memory access (DMA) specification in response to a call from the framework.
- [DMAOutputSegmentType](dmaoutputsegmenttype.md)
  The size and endianness that the system uses for direct memory access (DMA).
### Supporting SCSI Power States
- [kIOServicePowerCapabilityPause](kioservicepowercapabilitypause.md)
  A PCIe-specific power state for halting transactions while reallocating resources.
### Instance Methods
- [UserCallMediaParametersHaveChanged](iouserscsiparallelinterfacecontroller/usercallmediaparametershavechanged.md)
- [UserGetDataBuffer](iouserscsiparallelinterfacecontroller/usergetdatabuffer.md)

## Relationships

### Inherits From
- [IOService](../DriverKit/IOService.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller)*