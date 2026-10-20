# enqueueTransferCompletion(for:status:transferLength:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func enqueueTransferCompletion(for message: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus, transferLength: Int) throws
```

```objc
- (BOOL) enqueueTransferCompletionForMessage:(const IOUSBHostCIMessage *) message status:(IOUSBHostCIMessageStatus) status transferLength:(NSUInteger) transferLength error:(NSError **) error;
```

## See Also

### Instance Methods
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](./inspectcommand%28_%29.md)
- [func processDoorbell(IOUSBHostCIDoorbell) throws](./processdoorbell%28_%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](./respond%28tocommand,status%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostciendpointstatemachine/enqueuetransfercompletion(for:status:transferlength:))*