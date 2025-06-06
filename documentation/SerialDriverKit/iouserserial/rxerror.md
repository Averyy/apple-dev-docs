# RxError

**Framework**: SerialDriverKit  
**Kind**: method

Reports errors that occurred when receiving data from the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t RxError(bool overrun, bool gotBreak, bool framingError, bool parityError);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Call this method when you encounter an error getting data from the device.

## Parameters

- `overrun`: A Boolean value indicating whether a buffer overrun error occurred.
- `gotBreak`: A Boolean value indicating whether a break error occurred.
- `framingError`: A Boolean value indicating whether a framing error occurred.
- `parityError`: A Boolean value indicating whether a parity error occurred.

## See Also

- [RxDataAvailable](iouserserial/rxdataavailable.md)
  Notifies the system that data from the device is now available.
- [RxFreeSpaceAvailable](iouserserial/rxfreespaceavailable.md)
  Notifies your driver that buffer space is available for your device’s data.
- [TxDataAvailable](iouserserial/txdataavailable.md)
  Notifies your driver that the system has data for you to transmit to the device.
- [TxFreeSpaceAvailable](iouserserial/txfreespaceavailable.md)
  Notifies the system that the device is ready to accept more data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/rxerror)*