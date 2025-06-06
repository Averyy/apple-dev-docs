# writeSync(_:length:)

**Framework**: IOBluetooth  
**Kind**: method

Sends a block of data in the channel synchronously.

**Availability**:
- macOS ?+

## Declaration

```swift
func writeSync(_ data: UnsafeMutableRawPointer!, length: UInt16) -> IOReturn
```

#### Return Value

Returns kIOReturnSuccess if the data was written successfully.

#### Discussion

Sends data through the channel. The number of bytes to be sent must not exceed the channel MTU. If the return value is an error condition none of the data was sent. This method will block until the data has been successfully sent to the hardware for transmission (or until an error occurs).

NOTE: This method is only available in macOS 10.2.5 (Bluetooth v1.2) or later.

## Parameters

- `data`: A pointer to the data buffer to be sent.
- `length`: The length of the buffer to be sent (in bytes).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/writesync(_:length:))*