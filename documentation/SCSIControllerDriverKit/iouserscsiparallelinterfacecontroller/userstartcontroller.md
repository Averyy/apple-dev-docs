# UserStartController

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Starts the controller in response to a call from the framework.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserStartController();
```

#### Return Value

A value that indicates the result of initialization. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

The framework always calls [`UserStartController`](iouserscsiparallelinterfacecontroller/userstartcontroller.md) before sending any requests to the driver for execution. The framework calls this method after [`UserInitializeController`](iouserscsiparallelinterfacecontroller/userinitializecontroller.md) to start the services that the specific host bus adapter (HBA) dext driver provides. After completing this call, all services provided by the HBA driver are available to the client.

The following sample implementation of [`UserStartController`](iouserscsiparallelinterfacecontroller/userstartcontroller.md) sets its local power state to [`kIOServicePowerCapabilityOn`](https://developer.apple.com/documentation/DriverKit/kIOServicePowerCapabilityOn), then calls a hypothetical `EnableReplyInterrupt()` convenience function. Next, it enables the interrupt dispatch source, and returns [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess). Signaling success like this indicates to the kernel that the dext is now up and ready to serve I/O.

```objc
kern_return_t
IMPL ( ExampleSCSIDext, UserStartController )
{
    
    kern_return_t ret = kIOReturnError;
    
    ivars->fCurrentPowerState = kIOServicePowerCapabilityOn;

    // Enable interrupts on the hardware
    EnableReplyInterrupt ( );
    
    // Enable interrupt event source
    ret = ivars->fIntSource->SetEnable ( true );
    __Require ( ( kIOReturnSuccess == ret ), Exit );

    …
}
```

## See Also

- [UserInitializeController](iouserscsiparallelinterfacecontroller/userinitializecontroller.md)
  Initializes the controller in response to a call from the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userstartcontroller)*