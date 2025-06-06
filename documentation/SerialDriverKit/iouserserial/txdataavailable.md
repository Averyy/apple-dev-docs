# TxDataAvailable

**Framework**: SerialDriverKit  
**Kind**: method

Notifies your driver that the system has data for you to transmit to the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
void TxDataAvailable();
```

#### Discussion

The system calls this method to let you know that there is buffered data ready for you to transmit to the device. The default implementation of this method does nothing. Override it and use your implementation to transfer that data to your hardware.

## See Also

- [RxDataAvailable](iouserserial/rxdataavailable.md)
  Notifies the system that data from the device is now available.
- [RxFreeSpaceAvailable](iouserserial/rxfreespaceavailable.md)
  Notifies your driver that buffer space is available for your device’s data.
- [TxFreeSpaceAvailable](iouserserial/txfreespaceavailable.md)
  Notifies the system that the device is ready to accept more data.
- [RxError](iouserserial/rxerror.md)
  Reports errors that occurred when receiving data from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/txdataavailable)*