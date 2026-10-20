# IOUSBHostCIEndpointStateMachine

**Framework**: IOUSBHost  
**Kind**: class  
**Role**: Class

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostCIEndpointStateMachine
```

```objc
@interface IOUSBHostCIEndpointStateMachine : NSObject
```

## Topics

### Instance Properties
- [var controllerInterface: IOUSBHostControllerInterface](./iousbhostciendpointstatemachine/controllerinterface.md)
- [var currentTransferMessage: UnsafePointer<IOUSBHostCIMessage>](./iousbhostciendpointstatemachine/currenttransfermessage.md)
- [var deviceAddress: Int](./iousbhostciendpointstatemachine/deviceaddress.md)
- [var endpointAddress: Int](./iousbhostciendpointstatemachine/endpointaddress.md)
- [var endpointState: IOUSBHostCIEndpointState](./iousbhostciendpointstatemachine/endpointstate.md)
### Instance Methods
- [func enqueueTransferCompletion(for: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, transferLength: Int) throws](./iousbhostciendpointstatemachine/enqueuetransfercompletion%28for,status,transferlength%29.md)
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](./iousbhostciendpointstatemachine/inspectcommand%28_%29.md)
- [func processDoorbell(IOUSBHostCIDoorbell) throws](./iousbhostciendpointstatemachine/processdoorbell%28_%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](./iousbhostciendpointstatemachine/respond%28tocommand,status%29.md)

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
- [class IOUSBHostCIPortStateMachine](./iousbhostciportstatemachine.md)
- [class IOUSBHostControllerInterface](./iousbhostcontrollerinterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostciendpointstatemachine)*