# IOUSBHostCIControllerStateMachine

**Framework**: IOUSBHost  
**Kind**: class

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostCIControllerStateMachine
```

## Topics

### Instance Properties
- [var controllerInterface: IOUSBHostControllerInterface](iousbhostcicontrollerstatemachine/controllerinterface.md)
- [var controllerState: IOUSBHostCIControllerState](iousbhostcicontrollerstatemachine/controllerstate.md)
### Instance Methods
- [func enqueueUpdatedFrame(UInt64, timestamp: UInt64) throws](iousbhostcicontrollerstatemachine/enqueueupdatedframe(_:timestamp:).md)
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](iousbhostcicontrollerstatemachine/inspectcommand(_:).md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](iousbhostcicontrollerstatemachine/respond(tocommand:status:).md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, frame: UInt64, timestamp: UInt64) throws](iousbhostcicontrollerstatemachine/respond(tocommand:status:frame:timestamp:).md)

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

- [class IOUSBHostCIDeviceStateMachine](iousbhostcidevicestatemachine.md)
- [class IOUSBHostCIEndpointStateMachine](iousbhostciendpointstatemachine.md)
- [class IOUSBHostCIPortStateMachine](iousbhostciportstatemachine.md)
- [class IOUSBHostControllerInterface](iousbhostcontrollerinterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcicontrollerstatemachine)*