# IOUSBHostCIControllerStateMachine

**Framework**: IOUSBHost  
**Kind**: class  
**Role**: Class

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostCIControllerStateMachine
```

```objc
@interface IOUSBHostCIControllerStateMachine : NSObject
```

## Topics

### Instance Properties
- [var controllerInterface: IOUSBHostControllerInterface](./iousbhostcicontrollerstatemachine/controllerinterface.md)
- [var controllerState: IOUSBHostCIControllerState](./iousbhostcicontrollerstatemachine/controllerstate.md)
### Instance Methods
- [func enqueueUpdatedFrame(UInt64, timestamp: UInt64) throws](./iousbhostcicontrollerstatemachine/enqueueupdatedframe%28_,timestamp%29.md)
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](./iousbhostcicontrollerstatemachine/inspectcommand%28_%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](./iousbhostcicontrollerstatemachine/respond%28tocommand,status%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, frame: UInt64, timestamp: UInt64) throws](./iousbhostcicontrollerstatemachine/respond%28tocommand,status,frame,timestamp%29.md)

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
- [class IOUSBHostCIDeviceStateMachine](./iousbhostcidevicestatemachine.md)
- [class IOUSBHostCIEndpointStateMachine](./iousbhostciendpointstatemachine.md)
- [class IOUSBHostCIPortStateMachine](./iousbhostciportstatemachine.md)
- [class IOUSBHostControllerInterface](./iousbhostcontrollerinterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcicontrollerstatemachine)*