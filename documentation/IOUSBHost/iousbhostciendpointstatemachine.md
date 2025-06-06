# IOUSBHostCIEndpointStateMachine

**Framework**: IOUSBHost  
**Kind**: class

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostCIEndpointStateMachine
```

## Topics

### Instance Properties
- [var controllerInterface: IOUSBHostControllerInterface](iousbhostciendpointstatemachine/controllerinterface.md)
- [var currentTransferMessage: UnsafePointer<IOUSBHostCIMessage>](iousbhostciendpointstatemachine/currenttransfermessage.md)
- [var deviceAddress: Int](iousbhostciendpointstatemachine/deviceaddress.md)
- [var endpointAddress: Int](iousbhostciendpointstatemachine/endpointaddress.md)
- [var endpointState: IOUSBHostCIEndpointState](iousbhostciendpointstatemachine/endpointstate.md)
### Instance Methods
- [func enqueueTransferCompletion(for: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, transferLength: Int) throws](iousbhostciendpointstatemachine/enqueuetransfercompletion(for:status:transferlength:).md)
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](iousbhostciendpointstatemachine/inspectcommand(_:).md)
- [func processDoorbell(IOUSBHostCIDoorbell) throws](iousbhostciendpointstatemachine/processdoorbell(_:).md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](iousbhostciendpointstatemachine/respond(tocommand:status:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class IOUSBHostCIControllerStateMachine](iousbhostcicontrollerstatemachine.md)
- [class IOUSBHostCIDeviceStateMachine](iousbhostcidevicestatemachine.md)
- [class IOUSBHostCIPortStateMachine](iousbhostciportstatemachine.md)
- [class IOUSBHostControllerInterface](iousbhostcontrollerinterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostciendpointstatemachine)*