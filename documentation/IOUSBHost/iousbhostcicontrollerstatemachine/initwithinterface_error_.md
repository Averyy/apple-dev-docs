# initWithInterface:error:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (instancetype) initWithInterface:(IOUSBHostControllerInterface *) interface error:(NSError **) error;
```

## See Also

### Instance Methods
- [func enqueueUpdatedFrame(UInt64, timestamp: UInt64) throws](./enqueueupdatedframe%28_,timestamp%29.md)
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](./inspectcommand%28_%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](./respond%28tocommand,status%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, frame: UInt64, timestamp: UInt64) throws](./respond%28tocommand,status,frame,timestamp%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcicontrollerstatemachine/initwithinterface:error:)*