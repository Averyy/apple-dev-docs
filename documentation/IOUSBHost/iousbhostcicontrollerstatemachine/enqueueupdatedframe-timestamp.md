# enqueueUpdatedFrame(_:timestamp:)

**Framework**: IOUSBHost  
**Kind**: method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func enqueueUpdatedFrame(_ frame: UInt64, timestamp: UInt64) throws
```

## See Also

- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](iousbhostcicontrollerstatemachine/inspectcommand(_:).md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](iousbhostcicontrollerstatemachine/respond(tocommand:status:).md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, frame: UInt64, timestamp: UInt64) throws](iousbhostcicontrollerstatemachine/respond(tocommand:status:frame:timestamp:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcicontrollerstatemachine/enqueueupdatedframe(_:timestamp:))*