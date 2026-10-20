# IOUSBHostControllerInterface

**Framework**: IOUSBHost  
**Kind**: class  
**Role**: Class

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostControllerInterface
```

```objc
@interface IOUSBHostControllerInterface : NSObject
```

## Topics

### Instance Properties
- [var capabilities: UnsafePointer<IOUSBHostCIMessage>](./iousbhostcontrollerinterface/capabilities.md)
- [var controllerStateMachine: IOUSBHostCIControllerStateMachine](./iousbhostcontrollerinterface/controllerstatemachine.md)
- [var interruptRateHz: Int](./iousbhostcontrollerinterface/interruptratehz.md)
- [var queue: dispatch_queue_t](./iousbhostcontrollerinterface/queue.md)
- [var uuid: UUID](./iousbhostcontrollerinterface/uuid.md)
### Instance Methods
- [func capabilities(forPort: Int) -> UnsafePointer<IOUSBHostCIMessage>](./iousbhostcontrollerinterface/capabilities%28forport%29.md)
- [func description(for: UnsafePointer<IOUSBHostCIMessage>) -> String](./iousbhostcontrollerinterface/description%28for%29.md)
- [func destroy()](./iousbhostcontrollerinterface/destroy%28%29.md)
- [func enqueueInterrupt(UnsafePointer<IOUSBHostCIMessage>) throws](./iousbhostcontrollerinterface/enqueueinterrupt%28_%29.md)
- [func enqueueInterrupt(UnsafePointer<IOUSBHostCIMessage>, expedite: Bool) throws](./iousbhostcontrollerinterface/enqueueinterrupt%28_,expedite%29.md)
- [func enqueueInterrupts(UnsafePointer<IOUSBHostCIMessage>, count: Int) throws](./iousbhostcontrollerinterface/enqueueinterrupts%28_,count%29.md)
- [func enqueueInterrupts(UnsafePointer<IOUSBHostCIMessage>, count: Int, expedite: Bool) throws](./iousbhostcontrollerinterface/enqueueinterrupts%28_,count,expedite%29.md)
- [func getPortStateMachine(forCommand: UnsafePointer<IOUSBHostCIMessage>, error: NSErrorPointer) -> IOUSBHostCIPortStateMachine](./iousbhostcontrollerinterface/getportstatemachine%28forcommand,error%29.md)
- [func getPortStateMachine(forPort: Int, error: NSErrorPointer) -> IOUSBHostCIPortStateMachine](./iousbhostcontrollerinterface/getportstatemachine%28forport,error%29.md)

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
- [class IOUSBHostCIPortStateMachine](./iousbhostciportstatemachine.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcontrollerinterface)*