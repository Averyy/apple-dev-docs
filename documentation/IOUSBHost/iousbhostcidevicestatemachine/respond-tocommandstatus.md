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

- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](iousbhostcidevicestatemachine/inspectcommand(_:).md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, deviceAddress: Int) throws](iousbhostcidevicestatemachine/respond(tocommand:status:deviceaddress:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcidevicestatemachine/respond(tocommand:status:))*