# initWithInterface:command:error:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (instancetype) initWithInterface:(IOUSBHostControllerInterface *) interface command:(const IOUSBHostCIMessage *) command error:(NSError **) error;
```

## See Also

### Instance Methods
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](./inspectcommand%28_%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](./respond%28tocommand,status%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, deviceAddress: Int) throws](./respond%28tocommand,status,deviceaddress%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcidevicestatemachine/initwithinterface:command:error:)*