# processDoorbell(_:)

**Framework**: IOUSBHost  
**Kind**: method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func processDoorbell(_ doorbell: IOUSBHostCIDoorbell) throws
```

## See Also

- [func enqueueTransferCompletion(for: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, transferLength: Int) throws](iousbhostciendpointstatemachine/enqueuetransfercompletion(for:status:transferlength:).md)
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](iousbhostciendpointstatemachine/inspectcommand(_:).md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](iousbhostciendpointstatemachine/respond(tocommand:status:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostciendpointstatemachine/processdoorbell(_:))*