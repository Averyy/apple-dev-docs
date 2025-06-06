# UserInitializeController

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Initializes the controller in response to a call from the framework.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserInitializeController();
```

#### Return Value

A value that indicates the result of initialization. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

The first method in the dext that the framework calls is [`UserInitializeController`](iouserscsiparallelinterfacecontroller/userinitializecontroller.md), which it only calls once per instantiation. Use this method to perform all necessary initialization that the hardware requires before it can accept requests to execute. Make all necessary resource allocations during this method call.

##### Queuing Considerations

For best results, use a model with three dispatch queues. DriverKit creates a default queue for you, and you’ll also need to create interrupt auxiliary queues. Because DriverKit dispatch queues are serial, this arrangement prevents calls from DriverKit, interrupts, and I/O work from competing with one another on the same thread.

The following example shows how to implement [`UserInitializeController`](iouserscsiparallelinterfacecontroller/userinitializecontroller.md) to set up the queues. After opening the PCI device session, it creates the auxiliary and interrupt queues, and then uses the interrupt queue to register for interrupts.

```objc
IMPL ( ExampleSCSIDext, UserInitializeController )
{
    kern_return_t    ret;
    
    // Perform any needed initialization here

    // Open a new PCI session.
    ret = ivars->fPCIDevice->Open ( this, 0 );
    __Require ( ( kIOReturnSuccess == ret ), Exit );

    // Create and set dispatch queues.
    ret = SetDispatchQueue ( "AuxiliaryQueue", ivars->fAuxQueue );
    __Require ( ( kIOReturnSuccess == ret ), Exit );

    ret = SetDispatchQueue ( "InterruptQueue", ivars->fIntQueue );
    __Require ( ( kIOReturnSuccess == ret ), Exit );

    // Register for interrupts.
    ret = IOInterruptDispatchSource::Create ( ivars->fPCIDevice,
                                             index,
                                             ivars->fIntQueue,
                                             &ivars->fIntSource );
    __Require ( ( kIOReturnSuccess == ret ), Exit );

    ret = CreateActionInterruptOccurred ( sizeof ( void  * ),
                                          &ivars->fInterruptCompletion );
    __Require ( ( kIOReturnSuccess == ret ), Exit );
    
    ret = ivars->fIntSource->SetHandler ( ivars->fInterruptCompletion );
    __Require ( ( kIOReturnSuccess == ret ), Exit );

    // Perform any further initialization here.

}
```

## See Also

- [UserStartController](iouserscsiparallelinterfacecontroller/userstartcontroller.md)
  Starts the controller in response to a call from the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userinitializecontroller)*