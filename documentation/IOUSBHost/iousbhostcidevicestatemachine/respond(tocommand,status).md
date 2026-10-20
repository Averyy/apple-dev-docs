# respond(toCommand:status:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func respond(toCommand command: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws
```

```objc
- (BOOL) respondToCommand:(const IOUSBHostCIMessage *) command status:(const IOUSBHostCIMessageStatus) status error:(NSError **) error;
```

## See Also

### Instance Methods
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](./inspectcommand%28_%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, deviceAddress: Int) throws](./respond%28tocommand,status,deviceaddress%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcidevicestatemachine/respond(tocommand:status:))*