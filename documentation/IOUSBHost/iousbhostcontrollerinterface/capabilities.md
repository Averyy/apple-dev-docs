# capabilities

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var capabilities: UnsafePointer<IOUSBHostCIMessage> { get }
```

```objc
@property (nonatomic, readonly) const IOUSBHostCIMessage * capabilities;
```

## See Also

### Instance Properties
- [var controllerStateMachine: IOUSBHostCIControllerStateMachine](./controllerstatemachine.md)
- [var interruptRateHz: Int](./interruptratehz.md)
- [var queue: dispatch_queue_t](./queue.md)
- [var uuid: UUID](./uuid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcontrollerinterface/capabilities)*