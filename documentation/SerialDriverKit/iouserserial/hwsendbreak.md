# HwSendBreak

**Framework**: SerialDriverKit  
**Kind**: method

Sends a linebreak command to the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t HwSendBreak(bool sendBreak);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Override this method and use it to set the break bit on the device.

## Parameters

- `sendBreak`: A Boolean indicating whether to send a break command.

## See Also

- [HwGetModemStatus](iouserserial/hwgetmodemstatus.md)
  Gets the current status of the modem from the hardware.
- [SetModemStatus](iouserserial/setmodemstatus.md)
  Sets the modem status to the specified values.
- [HwResetFIFO](iouserserial/hwresetfifo.md)
  Sends a command to reset the specified device queues.
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

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/hwsendbreak)*