# currentTransferMessage

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var currentTransferMessage: UnsafePointer<IOUSBHostCIMessage> { get }
```

```objc
@property (nonatomic, readonly) const IOUSBHostCIMessage * currentTransferMessage;
```

## See Also

### Instance Properties
- [var controllerInterface: IOUSBHostControllerInterface](./controllerinterface.md)
- [var deviceAddress: Int](./deviceaddress.md)
- [var endpointAddress: Int](./endpointaddress.md)
- [var endpointState: IOUSBHostCIEndpointState](./endpointstate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostciendpointstatemachine/currenttransfermessage)*