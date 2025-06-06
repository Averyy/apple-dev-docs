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

- [func enqueueUpdatedFrame(UInt64, timestamp: UInt64) throws](iousbhostcicontrollerstatemachine/enqueueupdatedframe(_:timestamp:).md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](iousbhostcicontrollerstatemachine/respond(tocommand:status:).md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, frame: UInt64, timestamp: UInt64) throws](iousbhostcicontrollerstatemachine/respond(tocommand:status:frame:timestamp:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcicontrollerstatemachine/inspectcommand(_:))*