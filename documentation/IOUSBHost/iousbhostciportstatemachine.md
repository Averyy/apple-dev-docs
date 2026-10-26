# IOUSBHostCIPortStateMachine

**Framework**: IOUSBHost  
**Kind**: class  
**Role**: Class

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostCIPortStateMachine
```

```objc
@interface IOUSBHostCIPortStateMachine : NSObject
```

## Topics

### Instance Properties
- [var connected: Bool](./iousbhostciportstatemachine/connected.md)
- [var controllerInterface: IOUSBHostControllerInterface](./iousbhostciportstatemachine/controllerinterface.md)
- [var linkState: IOUSBHostCILinkState](./iousbhostciportstatemachine/linkstate.md)
- [var overcurrent: Bool](./iousbhostciportstatemachine/overcurrent.md)
- [var portNumber: Int](./iousbhostciportstatemachine/portnumber.md)
- [var portState: IOUSBHostCIPortState](./iousbhostciportstatemachine/portstate.md)
- [var portStatus: IOUSBHostCIPortStatus](./iousbhostciportstatemachine/portstatus.md)
- [var powered: Bool](./iousbhostciportstatemachine/powered.md)
- [var speed: IOUSBHostCIDeviceSpeed](./iousbhostciportstatemachine/speed.md)
### Instance Methods
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](./iousbhostciportstatemachine/inspectcommand%28_%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](./iousbhostciportstatemachine/respond%28tocommand,status%29.md)
- [func updateLinkState(IOUSBHostCILinkState, speed: IOUSBHostCIDeviceSpeed, inhibitLinkStateChange: Bool) throws](./iousbhostciportstatemachine/updatelinkstate%28_,speed,inhibitlinkstatechange%29.md)
- [- initWithInterface:portNumber:error:](./iousbhostciportstatemachine/initwithinterface_portnumber_error_.md)

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
- [class IOUSBHostCIDeviceStateMachine](./iousbhostcidevicestatemachine.md)
- [class IOUSBHostCIEndpointStateMachine](./iousbhostciendpointstatemachine.md)
- [class IOUSBHostControllerInterface](./iousbhostcontrollerinterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostciportstatemachine)*