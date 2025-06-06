# inspectCommand(_:)

**Framework**: IOUSBHost  
**Kind**: method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func inspectCommand(_ command: UnsafePointer<IOUSBHostCIMessage>) throws
```

## See Also

- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](iousbhostciportstatemachine/respond(tocommand:status:).md)
- [func updateLinkState(IOUSBHostCILinkState, speed: IOUSBHostCIDeviceSpeed, inhibitLinkStateChange: Bool) throws](iousbhostciportstatemachine/updatelinkstate(_:speed:inhibitlinkstatechange:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostciportstatemachine/inspectcommand(_:))*