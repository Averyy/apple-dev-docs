# IOUSBHostControllerInterface

**Framework**: IOUSBHost  
**Kind**: class

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostControllerInterface
```

## Topics

### Instance Properties
- [var capabilities: UnsafePointer<IOUSBHostCIMessage>](iousbhostcontrollerinterface/capabilities.md)
- [var controllerStateMachine: IOUSBHostCIControllerStateMachine](iousbhostcontrollerinterface/controllerstatemachine.md)
- [var interruptRateHz: Int](iousbhostcontrollerinterface/interruptratehz.md)
- [var queue: dispatch_queue_t](iousbhostcontrollerinterface/queue.md)
- [var uuid: UUID](iousbhostcontrollerinterface/uuid.md)
### Instance Methods
- [func capabilities(forPort: Int) -> UnsafePointer<IOUSBHostCIMessage>](iousbhostcontrollerinterface/capabilities(forport:).md)
- [func description(for: UnsafePointer<IOUSBHostCIMessage>) -> String](iousbhostcontrollerinterface/description(for:).md)
- [func destroy()](iousbhostcontrollerinterface/destroy.md)
- [func enqueueInterrupt(UnsafePointer<IOUSBHostCIMessage>) throws](iousbhostcontrollerinterface/enqueueinterrupt(_:).md)
- [func enqueueInterrupt(UnsafePointer<IOUSBHostCIMessage>, expedite: Bool) throws](iousbhostcontrollerinterface/enqueueinterrupt(_:expedite:).md)
- [func enqueueInterrupts(UnsafePointer<IOUSBHostCIMessage>, count: Int) throws](iousbhostcontrollerinterface/enqueueinterrupts(_:count:).md)
- [func enqueueInterrupts(UnsafePointer<IOUSBHostCIMessage>, count: Int, expedite: Bool) throws](iousbhostcontrollerinterface/enqueueinterrupts(_:count:expedite:).md)
- [func getPortStateMachine(forCommand: UnsafePointer<IOUSBHostCIMessage>, error: NSErrorPointer) -> IOUSBHostCIPortStateMachine](iousbhostcontrollerinterface/getportstatemachine(forcommand:error:).md)
- [func getPortStateMachine(forPort: Int, error: NSErrorPointer) -> IOUSBHostCIPortStateMachine](iousbhostcontrollerinterface/getportstatemachine(forport:error:).md)

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
- [class IOUSBHostCIPortStateMachine](iousbhostciportstatemachine.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcontrollerinterface)*