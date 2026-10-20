# description(for:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func description(for message: UnsafePointer<IOUSBHostCIMessage>) -> String
```

```objc
- (NSString *) descriptionForMessage:(const IOUSBHostCIMessage *) message;
```

## See Also

### Instance Methods
- [func capabilities(forPort: Int) -> UnsafePointer<IOUSBHostCIMessage>](./capabilities%28forport%29.md)
- [func destroy()](./destroy%28%29.md)
- [func enqueueInterrupt(UnsafePointer<IOUSBHostCIMessage>) throws](./enqueueinterrupt%28_%29.md)
- [func enqueueInterrupt(UnsafePointer<IOUSBHostCIMessage>, expedite: Bool) throws](./enqueueinterrupt%28_,expedite%29.md)
- [func enqueueInterrupts(UnsafePointer<IOUSBHostCIMessage>, count: Int) throws](./enqueueinterrupts%28_,count%29.md)
- [func enqueueInterrupts(UnsafePointer<IOUSBHostCIMessage>, count: Int, expedite: Bool) throws](./enqueueinterrupts%28_,count,expedite%29.md)
- [func getPortStateMachine(forCommand: UnsafePointer<IOUSBHostCIMessage>, error: NSErrorPointer) -> IOUSBHostCIPortStateMachine](./getportstatemachine%28forcommand,error%29.md)
- [func getPortStateMachine(forPort: Int, error: NSErrorPointer) -> IOUSBHostCIPortStateMachine](./getportstatemachine%28forport,error%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcontrollerinterface/description(for:))*