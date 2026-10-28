# HwGetModemStatus

**Framework**: SerialDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the current status of the modem from the hardware.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t HwGetModemStatus(bool *cts, bool *dsr, bool *ri, bool *dcd);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Discussion

Override this method and use it to retrieve the current modem status from your hardware. Set the values of each parameter to an appropriate value based on whether the indicated bit is set.

## Parameters

- `cts`: On return, a Boolean variable containing the state of the clear-to-send bit. Set this value to `YES` when the bit is set.
- `dsr`: On return, a Boolean variable containing the state of the data-set-ready bit. Set this value to `YES` when the bit is set.
- `ri`: On return, a Boolean variable containing the state of the ring-indicator bit. Set this value to `YES` when the bit is set.
- `dcd`: On return, a Boolean variable containing the state of the data-carrier-detect bit. Set this value to `YES` when the bit is set.

## See Also

### Programming the Modem
- [SetModemStatus](./setmodemstatus.md)
  Sets the modem status to the specified values.
- [HwResetFIFO](./hwresetfifo.md)
  Sends a command to reset the specified device queues.
- [HwSendBreak](./hwsendbreak.md)
  Sends a linebreak command to the device.
- [HwProgramBaudRate](./hwprogrambaudrate.md)
  Sets the communication baud rate to the specified value.
- [HwProgramLatencyTimer](./hwprogramlatencytimer.md)
  Sets the amount of time to wait before sending the current buffer to the device.
- [HwProgramMCR](./hwprogrammcr.md)
  Configure the setings for the device’s modem control register (MCR).
- [HwProgramUART](./hwprogramuart.md)
  Configure the settings for the device’s universal asynchronous receiver/transmitter (UART).
- [Hardware Constants](../hardware-constants.md)
  Configure your device with the appropriate parity and flow-control options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/hwgetmodemstatus)*