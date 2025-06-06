# enqueueTransferCompletion(for:status:transferLength:)

**Framework**: IOUSBHost  
**Kind**: method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func enqueueTransferCompletion(for message: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, transferLength: Int) throws
```

## See Also

- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](iousbhostciendpointstatemachine/inspectcommand(_:).md)
- [func processDoorbell(IOUSBHostCIDoorbell) throws](iousbhostciendpointstatemachine/processdoorbell(_:).md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](iousbhostciendpointstatemachine/respond(tocommand:status:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostciendpointstatemachine/enqueuetransfercompletion(for:status:transferlength:))*