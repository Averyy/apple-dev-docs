# inspectCommand(_:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func inspectCommand(_ command: UnsafePointer<IOUSBHostCIMessage>) throws
```

```objc
- (BOOL) inspectCommand:(const IOUSBHostCIMessage *) command error:(NSError **) error;
```

## See Also

### Instance Methods
- [func enqueueUpdatedFrame(UInt64, timestamp: UInt64) throws](./enqueueupdatedframe%28_,timestamp%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](./respond%28tocommand,status%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, frame: UInt64, timestamp: UInt64) throws](./respond%28tocommand,status,frame,timestamp%29.md)
- [- initWithInterface:error:](./initwithinterface_error_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcicontrollerstatemachine/inspectcommand(_:))*