# sendL2CAPEchoRequest(_:length:)

**Framework**: IOBluetooth  
**Kind**: method

Send an echo request over the L2CAP connection to a remote device.

**Availability**:
- macOS ?+

## Declaration

```swift
func sendL2CAPEchoRequest(_ data: UnsafeMutableRawPointer!, length: UInt16) -> IOReturn
```

#### Return Value

Returns kIOReturnSuccess if the echo request was able to be sent.

#### Discussion

The current implementation returns when the request has been sent, but does not indicate when a response is received. Also, the baseband connection must be up for the echo request to be sent. In the future, this method will also open the connection if necessary. The API will be updated to allow the client to be informed when the echo response has been received (both synchronously and asynchronously).

## Parameters

- `data`: (Void *) - Pointer to buffer to send.
- `length`: (UInt16) - Length of the buffer to send


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/sendl2capechorequest(_:length:))*