# enqueueInterrupt(_:)

**Framework**: IOUSBHost  
**Kind**: method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func enqueueInterrupt(_ interrupt: UnsafePointer<IOUSBHostCIMessage>) throws
```

## See Also

- [func capabilities(forPort: Int) -> UnsafePointer<IOUSBHostCIMessage>](iousbhostcontrollerinterface/capabilities(forport:).md)
- [func description(for: UnsafePointer<IOUSBHostCIMessage>) -> String](iousbhostcontrollerinterface/description(for:).md)
- [func destroy()](iousbhostcontrollerinterface/destroy.md)
- [func enqueueInterrupt(UnsafePointer<IOUSBHostCIMessage>, expedite: Bool) throws](iousbhostcontrollerinterface/enqueueinterrupt(_:expedite:).md)
- [func enqueueInterrupts(UnsafePointer<IOUSBHostCIMessage>, count: Int) throws](iousbhostcontrollerinterface/enqueueinterrupts(_:count:).md)
- [func enqueueInterrupts(UnsafePointer<IOUSBHostCIMessage>, count: Int, expedite: Bool) throws](iousbhostcontrollerinterface/enqueueinterrupts(_:count:expedite:).md)
- [func getPortStateMachine(forCommand: UnsafePointer<IOUSBHostCIMessage>, error: NSErrorPointer) -> IOUSBHostCIPortStateMachine](iousbhostcontrollerinterface/getportstatemachine(forcommand:error:).md)
- [func getPortStateMachine(forPort: Int, error: NSErrorPointer) -> IOUSBHostCIPortStateMachine](iousbhostcontrollerinterface/getportstatemachine(forport:error:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcontrollerinterface/enqueueinterrupt(_:))*