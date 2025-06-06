# RxDataAvailable

**Framework**: SerialDriverKit  
**Kind**: method

Notifies the system that data from the device is now available.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
void RxDataAvailable();
```

#### Discussion

After receiving data from the device and placing it in your data buffer, call this method to let the system know that the data is available.

## See Also

- [RxFreeSpaceAvailable](iouserserial/rxfreespaceavailable.md)
  Notifies your driver that buffer space is available for your device’s data.
- [TxDataAvailable](iouserserial/txdataavailable.md)
  Notifies your driver that the system has data for you to transmit to the device.
- [TxFreeSpaceAvailable](iouserserial/txfreespaceavailable.md)
  Notifies the system that the device is ready to accept more data.
- [RxError](iouserserial/rxerror.md)
  Reports errors that occurred when receiving data from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/rxdataavailable)*