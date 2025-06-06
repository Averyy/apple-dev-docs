# respond(toCommand:status:)

**Framework**: IOUSBHost  
**Kind**: method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func respond(toCommand command: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws
```

## See Also

- [func enqueueTransferCompletion(for: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, transferLength: Int) throws](iousbhostciendpointstatemachine/enqueuetransfercompletion(for:status:transferlength:).md)
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](iousbhostciendpointstatemachine/inspectcommand(_:).md)
- [func processDoorbell(IOUSBHostCIDoorbell) throws](iousbhostciendpointstatemachine/processdoorbell(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostciendpointstatemachine/respond(tocommand:status:))*