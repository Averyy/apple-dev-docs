# UserMapHBAData

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Maps any host bus adapter (HBA)-specific task data in response to a call from the framework.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserMapHBAData(uint32_t * uniqueTaskID);
```

#### Return Value

A value that indicates the result of memory-mapping the data. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

The driver extension class should override this function and memory-map and prepare any host bus adapter (HBA)-specific task data for direct memory access (DMA). The framework calls this method for every `SCSIParallelTask` immediately after creating the task in the kernel. The driver extension class should also set a unique task ID. The framework uses this ID to uniquely identify the corresponding `SCSIParallelTask` in the kernel.

The following listing shows an example of implementing [`UserMapHBAData`](iouserscsiparallelinterfacecontroller/usermaphbadata.md). It starts by creating an [`IOBufferMemoryDescriptor`](https://developer.apple.com/documentation/DriverKit/IOBufferMemoryDescriptor) for the controller’s specific data structure. It also maps memory to the dext’s memory space. Then the example adds the task to its own task data list, and sets the `uniqueTaskID` in-out variable to a newly-incremented unique ID. This allows the kernel to associate this task with its corresponding [`SCSIParallelTaskIdentifier`](https://developer.apple.com/documentation/kernel/scsiparalleltaskidentifier).

```objc
kern_return_t
IMPL ( ExampleSCSIDext, UserMapHBAData )
{
    …
    ret = IOBufferMemoryDescriptor::Create ( kIOMemoryDirectionOutIn, ivars->fTaskDataSize,        
                                             vm_page_size, &buffer );
    __Require ( ( kIOReturnSuccess == ret ), Exit );
    
    ret = buffer->CreateMapping ( 0, 0, 0, 0, 0, &memMap );
    __Require ( ( kIOReturnSuccess == ret ), Exit );
    taskData  =  ( typeof ( taskData ) ) memMap->GetAddress ( );

    ivars->fTaskID++;
    ivars->fTaskArray[ivars->fTaskID] = taskData;

    *uniqueTaskID = ivars->fTaskID;
   …
}
```

It’s important to perform preprocessing like memory mapping early — before serving I/O — because doing so on the I/O path can affect performance. For example, calling an API like [`CreateMapping`](https://developer.apple.com/documentation/DriverKit/IOMemoryDescriptor/CreateMapping) in the I/O path can cause additional RPC overhead.

## Parameters

- `uniqueTaskID`: The unique ID for this task.

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
- [UserSetHBAProperties](iouserscsiparallelinterfacecontroller/usersethbaproperties.md)
  Sets multiple properties for a host bus adapter.
- [UserRemoveHBAProperties](iouserscsiparallelinterfacecontroller/userremovehbaproperties.md)
  Removes properties from a host bus adapter in response to a call from the framework.
- [UserReportHBAConstraints](iouserscsiparallelinterfacecontroller/userreporthbaconstraints.md)
  Reports the I/O constraints for this controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usermaphbadata)*