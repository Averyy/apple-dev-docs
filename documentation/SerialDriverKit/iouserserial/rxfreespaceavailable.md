# RxFreeSpaceAvailable

**Framework**: SerialDriverKit  
**Kind**: method

Notifies your driver that buffer space is available for your device’s data.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
void RxFreeSpaceAvailable();
```

#### Discussion

Override this method and use it to read data asynchronously from the device’s serial port. When you finish reading the data, call the [`RxDataAvailable`](iouserserial/rxdataavailable.md) method to let the system know the data is ready.

## See Also

- [RxDataAvailable](iouserserial/rxdataavailable.md)
  Notifies the system that data from the device is now available.
- [TxDataAvailable](iouserserial/txdataavailable.md)
  Notifies your driver that the system has data for you to transmit to the device.
- [TxFreeSpaceAvailable](iouserserial/txfreespaceavailable.md)
  Notifies the system that the device is ready to accept more data.
- [RxError](iouserserial/rxerror.md)
  Reports errors that occurred when receiving data from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/rxfreespaceavailable)*