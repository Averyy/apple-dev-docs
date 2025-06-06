# DisconnectQueues

**Framework**: SerialDriverKit  
**Kind**: method

Releases the buffers that manage data moving to and from the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t DisconnectQueues();
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

During the cleanup of your driver, call this method to disconnect the data queues you use to buffer data. If you provided the buffer objects at configuration time, the system releases its references to the objects you provided.

## See Also

- [ConnectQueues](iouserserial/connectqueues.md)
  Creates and configures the buffers that store the data moving to and from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/disconnectqueues)*