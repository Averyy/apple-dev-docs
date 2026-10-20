# DisconnectQueues

**Framework**: SerialDriverKit  
**Kind**: method  
**Role**: Instance Method

Releases the buffers that manage data moving to and from the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t DisconnectQueues();
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

During the cleanup of your driver, call this method to disconnect the data queues you use to buffer data. If you provided the buffer objects at configuration time, the system releases its references to the objects you provided.

## See Also

### Configuring the Serial Data Queues
- [ConnectQueues](./connectqueues.md)
  Creates and configures the buffers that store the data moving to and from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/disconnectqueues)*