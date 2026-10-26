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
- [func enqueueTransferCompletion(for: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, transferLength: Int) throws](./enqueuetransfercompletion%28for,status,transferlength%29.md)
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](./inspectcommand%28_%29.md)
- [func processDoorbell(IOUSBHostCIDoorbell) throws](./processdoorbell%28_%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](./respond%28tocommand,status%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostciendpointstatemachine/initwithinterface:command:error:)*