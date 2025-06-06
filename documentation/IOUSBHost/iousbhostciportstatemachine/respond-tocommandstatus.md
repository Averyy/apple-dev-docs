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

- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](iousbhostciportstatemachine/inspectcommand(_:).md)
- [func updateLinkState(IOUSBHostCILinkState, speed: IOUSBHostCIDeviceSpeed, inhibitLinkStateChange: Bool) throws](iousbhostciportstatemachine/updatelinkstate(_:speed:inhibitlinkstatechange:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostciportstatemachine/respond(tocommand:status:))*