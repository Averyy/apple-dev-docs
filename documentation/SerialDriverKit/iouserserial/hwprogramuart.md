# HwProgramUART

**Framework**: SerialDriverKit  
**Kind**: method  
**Role**: Instance Method

Configure the settings for the device’s universal asynchronous receiver/transmitter (UART).

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t HwProgramUART(uint32_t baudRate, uint8_t nDataBits, uint8_t nHalfStopBits, uint8_t parity);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Discussion

Override this method and use it to program your hardware with the specified information.

## Parameters

- `baudRate`: The baud rate requested by the system.
- `nDataBits`: The number of data bits to transmit.
- `nHalfStopBits`: The number of half stop bits. For example, specify `3` to generate `1.5` stop bits.
- `parity`: The parity setting to use during communication. For a list of possible values, see Parity Options.

## See Also

### Programming the Modem
- [HwGetModemStatus](./hwgetmodemstatus.md)
  Gets the current status of the modem from the hardware.
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
- [Hardware Constants](../hardware-constants.md)
  Configure your device with the appropriate parity and flow-control options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/hwprogramuart)*