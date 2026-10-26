# getPortStateMachine(forPort:error:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func getPortStateMachine(forPort port: Int, error: NSErrorPointer) -> IOUSBHostCIPortStateMachine
```

```objc
- (IOUSBHostCIPortStateMachine *) getPortStateMachineForPort:(NSUInteger) port error:(NSError **) error;
```

## See Also

### Instance Methods
- [func capabilities(forPort: Int) -> UnsafePointer<IOUSBHostCIMessage>](./capabilities%28forport%29.md)
- [func description(for: UnsafePointer<IOUSBHostCIMessage>) -> String](./description%28for%29.md)
- [func destroy()](./destroy%28%29.md)
- [func enqueueInterrupt(UnsafePointer<IOUSBHostCIMessage>) throws](./enqueueinterrupt%28_%29.md)
- [func enqueueInterrupt(UnsafePointer<IOUSBHostCIMessage>, expedite: Bool) throws](./enqueueinterrupt%28_,expedite%29.md)
- [func enqueueInterrupts(UnsafePointer<IOUSBHostCIMessage>, count: Int) throws](./enqueueinterrupts%28_,count%29.md)
- [func enqueueInterrupts(UnsafePointer<IOUSBHostCIMessage>, count: Int, expedite: Bool) throws](./enqueueinterrupts%28_,count,expedite%29.md)
- [func getPortStateMachine(forCommand: UnsafePointer<IOUSBHostCIMessage>, error: NSErrorPointer) -> IOUSBHostCIPortStateMachine](./getportstatemachine%28forcommand,error%29.md)
- [- initWithCapabilities:queue:interruptRateHz:error:commandHandler:doorbellHandler:interestHandler:](./initwithcapabilities_queue_interruptratehz_error_commandhandler_doorbellhandler_interesthandler_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcontrollerinterface/getportstatemachine(forport:error:))*