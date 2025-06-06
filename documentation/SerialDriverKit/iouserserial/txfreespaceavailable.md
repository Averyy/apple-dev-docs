# TxFreeSpaceAvailable

**Framework**: SerialDriverKit  
**Kind**: method

Notifies the system that the device is ready to accept more data.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
void TxFreeSpaceAvailable();
```

#### Discussion

Call this method after freeing up space in the memory buffer you use to transmit data. When more data is available, the system responds by adding that data to the buffer and calling the [`TxDataAvailable`](iouserserial/txdataavailable.md) method.

## See Also

- [RxDataAvailable](iouserserial/rxdataavailable.md)
  Notifies the system that data from the device is now available.
- [RxFreeSpaceAvailable](iouserserial/rxfreespaceavailable.md)
  Notifies your driver that buffer space is available for your device’s data.
- [TxDataAvailable](iouserserial/txdataavailable.md)
  Notifies your driver that the system has data for you to transmit to the device.
- [RxError](iouserserial/rxerror.md)
  Reports errors that occurred when receiving data from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/txfreespaceavailable)*