# HwProgramUART

**Framework**: SerialDriverKit  
**Kind**: method

Configure the settings for the device’s universal asynchronous receiver/transmitter (UART).

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t HwProgramUART(uint32_t baudRate, uint8_t nDataBits, uint8_t nHalfStopBits, uint8_t parity);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Override this method and use it to program your hardware with the specified information.

## Parameters

- `baudRate`: The baud rate requested by the system.
- `nDataBits`: The number of data bits to transmit.
- `nHalfStopBits`: The number of half stop bits. For example, specify   to generate   stop bits.
- `parity`: The parity setting to use during communication. For a list of possible values, see Parity Options.

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
- [HwProgramMCR](iouserserial/hwprogrammcr.md)
  Configure the setings for the device’s modem control register (MCR).
- [Hardware Constants](hardware-constants.md)
  Configure your device with the appropriate parity and flow-control options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/hwprogramuart)*