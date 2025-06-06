# HwGetModemStatus

**Framework**: SerialDriverKit  
**Kind**: method

Gets the current status of the modem from the hardware.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t HwGetModemStatus(bool * cts, bool * dsr, bool * ri, bool * dcd);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Override this method and use it to retrieve the current modem status from your hardware. Set the values of each parameter to an appropriate value based on whether the indicated bit is set.

## Parameters

- `cts`: On return, a Boolean variable containing the state of the clear-to-send bit. Set this value to   when the bit is set.
- `dsr`: On return, a Boolean variable containing the state of the data-set-ready bit. Set this value to   when the bit is set.
- `ri`: On return, a Boolean variable containing the state of the ring-indicator bit. Set this value to   when the bit is set.
- `dcd`: On return, a Boolean variable containing the state of the data-carrier-detect bit. Set this value to   when the bit is set.

## See Also

- [SetModemStatus](iouserserial/setmodemstatus.md)
  Sets the modem status to the specified values.
- [HwResetFIFO](iouserserial/hwresetfifo.md)
  Sends a command to reset the specified device queues.
- [HwSendBreak](iouserserial/hwsendbreak.md)
  Sends a linebreak command to the device.
- [HwProgramBaudRate](iouserserial/hwprogrambaudrate.md)
  Sets the communication baud rate to the specified value.
- [HwProgramLatencyTimer](iouserserial/hwprogramlatencytimer.md)
  Sets the amount of time to wait before sending the current buffer to the device.
- [HwProgramMCR](iouserserial/hwprogrammcr.md)
  Configure the setings for the device’s modem control register (MCR).
- [HwProgramUART](iouserserial/hwprogramuart.md)
  Configure the settings for the device’s universal asynchronous receiver/transmitter (UART).
- [Hardware Constants](hardware-constants.md)
  Configure your device with the appropriate parity and flow-control options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/hwgetmodemstatus)*