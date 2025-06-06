# IOUSBHostCIPortStateMachine

**Framework**: IOUSBHost  
**Kind**: class

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostCIPortStateMachine
```

## Topics

### Instance Properties
- [var connected: Bool](iousbhostciportstatemachine/connected.md)
- [var controllerInterface: IOUSBHostControllerInterface](iousbhostciportstatemachine/controllerinterface.md)
- [var linkState: IOUSBHostCILinkState](iousbhostciportstatemachine/linkstate.md)
- [var overcurrent: Bool](iousbhostciportstatemachine/overcurrent.md)
- [var portNumber: Int](iousbhostciportstatemachine/portnumber.md)
- [var portState: IOUSBHostCIPortState](iousbhostciportstatemachine/portstate.md)
- [var portStatus: IOUSBHostCIPortStatus](iousbhostciportstatemachine/portstatus.md)
- [var powered: Bool](iousbhostciportstatemachine/powered.md)
- [var speed: IOUSBHostCIDeviceSpeed](iousbhostciportstatemachine/speed.md)
### Instance Methods
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](iousbhostciportstatemachine/inspectcommand(_:).md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](iousbhostciportstatemachine/respond(tocommand:status:).md)
- [func updateLinkState(IOUSBHostCILinkState, speed: IOUSBHostCIDeviceSpeed, inhibitLinkStateChange: Bool) throws](iousbhostciportstatemachine/updatelinkstate(_:speed:inhibitlinkstatechange:).md)

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
- [class IOUSBHostCIEndpointStateMachine](iousbhostciendpointstatemachine.md)
- [class IOUSBHostControllerInterface](iousbhostcontrollerinterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostciportstatemachine)*