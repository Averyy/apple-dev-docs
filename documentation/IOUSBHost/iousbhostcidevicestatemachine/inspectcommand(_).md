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
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](./respond%28tocommand,status%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, deviceAddress: Int) throws](./respond%28tocommand,status,deviceaddress%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcidevicestatemachine/inspectcommand(_:))*