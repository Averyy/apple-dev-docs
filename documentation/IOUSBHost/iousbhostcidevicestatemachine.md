# IOUSBHostCIDeviceStateMachine

**Framework**: IOUSBHost  
**Kind**: class  
**Role**: Class

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostCIDeviceStateMachine
```

```objc
@interface IOUSBHostCIDeviceStateMachine : NSObject
```

## Topics

### Instance Properties
- [var completeRoute: Int](./iousbhostcidevicestatemachine/completeroute.md)
- [var controllerInterface: IOUSBHostControllerInterface](./iousbhostcidevicestatemachine/controllerinterface.md)
- [var deviceAddress: Int](./iousbhostcidevicestatemachine/deviceaddress.md)
- [var deviceState: IOUSBHostCIDeviceState](./iousbhostcidevicestatemachine/devicestate.md)
### Instance Methods
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](./iousbhostcidevicestatemachine/inspectcommand%28_%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](./iousbhostcidevicestatemachine/respond%28tocommand,status%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, deviceAddress: Int) throws](./iousbhostcidevicestatemachine/respond%28tocommand,status,deviceaddress%29.md)
- [- initWithInterface:command:error:](./iousbhostcidevicestatemachine/initwithinterface_command_error_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Classes
- [class IOUSBHostCIControllerStateMachine](./iousbhostcicontrollerstatemachine.md)
- [class IOUSBHostCIEndpointStateMachine](./iousbhostciendpointstatemachine.md)
- [class IOUSBHostCIPortStateMachine](./iousbhostciportstatemachine.md)
- [class IOUSBHostControllerInterface](./iousbhostcontrollerinterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcidevicestatemachine)*