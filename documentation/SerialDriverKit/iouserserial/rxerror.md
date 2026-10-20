# RxError

**Framework**: SerialDriverKit  
**Kind**: method  
**Role**: Instance Method

Reports errors that occurred when receiving data from the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t RxError(bool overrun, bool gotBreak, bool framingError, bool parityError);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

Call this method when you encounter an error getting data from the device.

## Parameters

- `overrun`: A Boolean value indicating whether a buffer overrun error occurred.
- `gotBreak`: A Boolean value indicating whether a break error occurred.
- `framingError`: A Boolean value indicating whether a framing error occurred.
- `parityError`: A Boolean value indicating whether a parity error occurred.

## See Also

### Transmitting and Receiving Data
- [RxDataAvailable](./rxdataavailable.md)
  Notifies the system that data from the device is now available.
- [RxFreeSpaceAvailable](./rxfreespaceavailable.md)
  Notifies your driver that buffer space is available for your device’s data.
- [TxDataAvailable](./txdataavailable.md)
  Notifies your driver that the system has data for you to transmit to the device.
- [TxFreeSpaceAvailable](./txfreespaceavailable.md)
  Notifies the system that the device is ready to accept more data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/rxerror)*