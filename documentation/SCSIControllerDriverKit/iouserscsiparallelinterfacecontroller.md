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

The DriverKit framework starts the `Default` dispatch queue. The system expects your dext to create two additional dispatch queues, named `AuxiliaryQueue` and `InterruptQueue`. The [`UserCreateTargetForID`](iouserscsiparallelinterfacecontroller/usercreatetargetforid.md) method uses the `AuxiliaryQueue` to avoid deadlock during start and initialization.

The framework invokes the dext class’s [`Start`](https://developer.apple.com/documentation/driverkit/ioservice/start) and other methods to initialize the SCSI controller. Because these calls occur during DriverKit’s matching, it’s important to complete them quickly, to prevent keeping `IORegsitry` in a busy state for a long time. In some cases, probing the media may take a long time and delay the initialization, especially when working with HDDs. Defer these tasks if they take a long time to complete.

The framework provides the [`UserReportHBAConstraints`](iouserscsiparallelinterfacecontroller/userreporthbaconstraints.md) API to report controller I/O constraints. Make sure your dext reports these constraints accurately — particularly all mandatory keys — during initialization. This helps prevent intermittent failures, such as controller firmware buffer overflows.

#### Support Power Capabilities

IOUserSCSIParallelInterfaceController supports the following power capabilities:

- [`kIOServicePowerCapabilityOff`](https://developer.apple.com/documentation/driverkit/kioservicepowercapabilityoff)
- [`kIOServicePowerCapabilityOn`](https://developer.apple.com/documentation/driverkit/kioservicepowercapabilityon)
- [`kIOServicePowerCapabilityPause`](kioservicepowercapabilitypause.md)

Implement the [`SetPowerState`](https://developer.apple.com/documentation/driverkit/ioservice/setpowerstate) method in your service object and use it to put your driver in a safe state for the new power setting. Call `super` either as the last step in your implementation, or when the dext is ready to acknowledge the power state transition.

The following code example implements [`SetPowerState`](https://developer.apple.com/documentation/driverkit/ioservice/setpowerstate) by performing a check to see if the new state is [`kIOServicePowerCapabilityOn`](https://developer.apple.com/documentation/driverkit/kioservicepowercapabilityon). If it is, the implementation calls a private `IssueHardReset()` method.

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

The hypothetical driver in this example still needs to acknowledge the power state change when it’s appropriate. For example, it can ensure a rescan brought up all its targets, and then call `SetPowerState ( powerState, SUPERDISPATCH );`.

## Topics

### Managing controllers
- [UserInitializeController](iouserscsiparallelinterfacecontroller/userinitializecontroller.md)
  Initializes the controller in response to a call from the framework.
- [UserStartController](iouserscsiparallelinterfacecontroller/userstartcontroller.md)
  Starts the controller in response to a call from the framework.
### Managing tasks
- [UserProcessParallelTask](iouserscsiparallelinterfacecontroller/userprocessparalleltask.md)
  Processes a parallel task in response to a call from the framework.
- [SCSIUserParallelTask](scsiuserparalleltask.md)
  The properties of a parallel task to perform.
- [ParallelTaskCompletion](iouserscsiparallelinterfacecontroller/paralleltaskcompletion.md)
  Indicates to the system that the extension has completed an asynchronous request.
- [SCSIUserParallelResponse](scsiuserparallelresponse.md)
  The properties of a completed request.
### Managing bundled parallel tasks
- [UserProcessBundledParallelTasks](iouserscsiparallelinterfacecontroller/userprocessbundledparalleltasks.md)
  Processes one or more parallel tasks in response to a call from the framework.
- [UserMapBundledParallelTaskCommandAndResponseBuffers](iouserscsiparallelinterfacecontroller/usermapbundledparalleltaskcommandandresponsebuffers.md)
  Maps the shared command and response buffers in the dext address space in response to a call from the framework.
- [BundledParallelTaskCompletion](iouserscsiparallelinterfacecontroller/bundledparalleltaskcompletion.md)
  Indicates to the system that the extension completed a bundled asynchronous request.
- [kMaxBundledParallelTasks](kmaxbundledparalleltasks.md)
### Managing targets
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
### Performing SCSI standard task management
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
### Managing host bus adapters
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
### Managing direct memory access
- [UserGetDMASpecification](iouserscsiparallelinterfacecontroller/usergetdmaspecification.md)
  Gets the controller-specific direct memory access (DMA) specification in response to a call from the framework.
- [DMAOutputSegmentType](dmaoutputsegmenttype.md)
  The size and endianness that the system uses for direct memory access (DMA).
### Supporting SCSI power states
- [kIOServicePowerCapabilityPause](kioservicepowercapabilitypause.md)
  A PCIe-specific power state for halting transactions while reallocating resources.
### Handling media changes
- [UserCallMediaParametersHaveChanged](iouserscsiparallelinterfacecontroller/usercallmediaparametershavechanged.md)
  Indicates to the system that the media parameters changed.
### Accessing data buffers
- [UserGetDataBuffer](iouserscsiparallelinterfacecontroller/usergetdatabuffer.md)
  Gets the data buffer associated with a particular I/O request.

## Relationships

### Inherits From
- [IOService](../driverkit/ioservice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller)*