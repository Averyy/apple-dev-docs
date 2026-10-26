# updateLinkState(_:speed:inhibitLinkStateChange:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func updateLinkState(_ linkState: IOUSBHostCILinkState, speed: IOUSBHostCIDeviceSpeed, inhibitLinkStateChange: Bool) throws
```

```objc
- (BOOL) updateLinkState:(const IOUSBHostCILinkState) linkState speed:(const IOUSBHostCIDeviceSpeed) speed inhibitLinkStateChange:(const BOOL) inhibitLinkStateChange error:(NSError **) error;
```

## See Also

### Instance Methods
- [func inspectCommand(UnsafePointer<IOUSBHostCIMessage>) throws](./inspectcommand%28_%29.md)
- [func respond(toCommand: UnsafePointer<IOUSBHostCIMessage>, status: IOUSBHostCIMessageStatus) throws](./respond%28tocommand,status%29.md)
- [- initWithInterface:portNumber:error:](./initwithinterface_portnumber_error_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostciportstatemachine/updatelinkstate(_:speed:inhibitlinkstatechange:))*