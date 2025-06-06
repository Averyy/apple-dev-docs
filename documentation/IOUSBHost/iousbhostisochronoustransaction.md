# IOUSBHostIsochronousTransaction

**Framework**: IOUSBHost  
**Kind**: struct

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
struct IOUSBHostIsochronousTransaction
```

## Topics

### Initializers
- [init()](iousbhostisochronoustransaction/init.md)
- [init(status: IOReturn, requestCount: UInt32, offset: UInt32, completeCount: UInt32, timeStamp: IOUSBHostTime, options: IOUSBHostIsochronousTransactionOptions)](iousbhostisochronoustransaction/init(status:requestcount:offset:completecount:timestamp:options:).md)
### Instance Properties
- [var completeCount: UInt32](iousbhostisochronoustransaction/completecount.md)
- [var offset: UInt32](iousbhostisochronoustransaction/offset.md)
- [var options: IOUSBHostIsochronousTransactionOptions](iousbhostisochronoustransaction/options.md)
- [var requestCount: UInt32](iousbhostisochronoustransaction/requestcount.md)
- [var status: IOReturn](iousbhostisochronoustransaction/status.md)
- [var timeStamp: IOUSBHostTime](iousbhostisochronoustransaction/timestamp.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct IOUSBHostCIControllerState](iousbhostcicontrollerstate.md)
- [struct IOUSBHostCIDeviceSpeed](iousbhostcidevicespeed.md)
- [struct IOUSBHostCIDeviceState](iousbhostcidevicestate.md)
- [struct IOUSBHostCIEndpointState](iousbhostciendpointstate.md)
- [struct IOUSBHostCIExceptionType](iousbhostciexceptiontype.md)
- [struct IOUSBHostCILinkState](iousbhostcilinkstate.md)
- [struct IOUSBHostCIMessage](iousbhostcimessage.md)
- [struct IOUSBHostCIMessageStatus](iousbhostcimessagestatus.md)
- [struct IOUSBHostCIMessageType](iousbhostcimessagetype.md)
- [struct IOUSBHostCIPortState](iousbhostciportstate.md)
- [struct IOUSBHostCIUserClientVersion](iousbhostciuserclientversion.md)
- [struct IOUSBHostIsochronousTransactionOptions](iousbhostisochronoustransactionoptions.md)
- [struct IOUSBHostIsochronousTransferOptions](iousbhostisochronoustransferoptions.md)
- [struct IOUSBHostObjectDestroyOptions](iousbhostobjectdestroyoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostisochronoustransaction)*