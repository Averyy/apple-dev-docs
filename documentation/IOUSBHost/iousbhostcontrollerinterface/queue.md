# queue

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var queue: dispatch_queue_t { get }
```

```objc
@property (readonly) dispatch_queue_t queue;
```

## See Also

### Instance Properties
- [var capabilities: UnsafePointer<IOUSBHostCIMessage>](./capabilities.md)
- [var controllerStateMachine: IOUSBHostCIControllerStateMachine](./controllerstatemachine.md)
- [var interruptRateHz: Int](./interruptratehz.md)
- [var uuid: UUID](./uuid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcontrollerinterface/queue)*