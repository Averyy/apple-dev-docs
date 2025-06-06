# enqueueInterrupts(_:count:expedite:)

**Framework**: IOUSBHost  
**Kind**: method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func enqueueInterrupts(_ interrupts: UnsafePointer<IOUSBHostCIMessage>, count: Int, expedite: Bool) throws
```

## See Also

- [func capabilities(forPort: Int) -> UnsafePointer<IOUSBHostCIMessage>](iousbhostcontrollerinterface/capabilities(forport:).md)
- [func description(for: UnsafePointer<IOUSBHostCIMessage>) -> String](iousbhostcontrollerinterface/description(for:).md)
- [func destroy()](iousbhostcontrollerinterface/destroy.md)
- [func enqueueInterrupt(UnsafePointer<IOUSBHostCIMessage>) throws](iousbhostcontrollerinterface/enqueueinterrupt(_:).md)
- [func enqueueInterrupt(UnsafePointer<IOUSBHostCIMessage>, expedite: Bool) throws](iousbhostcontrollerinterface/enqueueinterrupt(_:expedite:).md)
- [func enqueueInterrupts(UnsafePointer<IOUSBHostCIMessage>, count: Int) throws](iousbhostcontrollerinterface/enqueueinterrupts(_:count:).md)
- [func getPortStateMachine(forCommand: UnsafePointer<IOUSBHostCIMessage>, error: NSErrorPointer) -> IOUSBHostCIPortStateMachine](iousbhostcontrollerinterface/getportstatemachine(forcommand:error:).md)
- [func getPortStateMachine(forPort: Int, error: NSErrorPointer) -> IOUSBHostCIPortStateMachine](iousbhostcontrollerinterface/getportstatemachine(forport:error:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcontrollerinterface/enqueueinterrupts(_:count:expedite:))*