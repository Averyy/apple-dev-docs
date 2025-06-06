# HwProgramMCR

**Framework**: SerialDriverKit  
**Kind**: method

Configure the setings for the device’s modem control register (MCR).

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t HwProgramMCR(bool dtr, bool rts);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Override this method and use it to program your hardware with the specified information.

## Parameters

- `dtr`: A Boolean value indicating whether to set or clear the data-terminal-ready bit. If the value is  , set the bit; otherwise, clear it.
- `rts`: A Boolean value indicating whether to set or clear the request-to-send bit. If the value is  , set the bit; otherwise, clear it.

## See Also

- [HwGetModemStatus](iouserserial/hwgetmodemstatus.md)
  Gets the current status of the modem from the hardware.
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
- [HwProgramUART](iouserserial/hwprogramuart.md)
  Configure the settings for the device’s universal asynchronous receiver/transmitter (UART).
- [Hardware Constants](hardware-constants.md)
  Configure your device with the appropriate parity and flow-control options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/hwprogrammcr)*