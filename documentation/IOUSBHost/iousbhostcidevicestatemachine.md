# IOUSBHostCIDeviceStateMachine

**Framework**: IOUSBHost  
**Kind**: class

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostCIDeviceStateMachine
```

## Topics

### Instance Properties
- [var completeRoute: Int](iousbhostcidevicestatemachine/completeroute.md)
- [var controllerInterface: IOUSBHostControllerInterface](iousbhostcidevicestatemachine/controllerinterface.md)
- [var deviceAddress: Int](iousbhostcidevicestatemachine/deviceaddress.md)
- [var deviceState: IOUSBHostCIDeviceState](iousbhostcidevicestatemachine/devicestate.md)
### Instance Methods
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](iousbhostcidevicestatemachine/inspectcommand(_:).md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](iousbhostcidevicestatemachine/respond(tocommand:status:).md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, deviceAddress: Int) throws](iousbhostcidevicestatemachine/respond(tocommand:status:deviceaddress:).md)

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
- [class IOUSBHostCIEndpointStateMachine](iousbhostciendpointstatemachine.md)
- [class IOUSBHostCIPortStateMachine](iousbhostciportstatemachine.md)
- [class IOUSBHostControllerInterface](iousbhostcontrollerinterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcidevicestatemachine)*