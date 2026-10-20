# HwProgramLatencyTimer

**Framework**: SerialDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the amount of time to wait before sending the current buffer to the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t HwProgramLatencyTimer(uint32_t latency);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

Override this method and use it to configure a latency timer for the device. Rather than sending buffers only when they’re full, the latency timer ensures that the hardware sends any accumulated data at the specified interval.

## Parameters

- `latency`: The number of milliseconds for the device to wait before sending a partial buffer to the host.

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
- [HwProgramMCR](./hwprogrammcr.md)
  Configure the setings for the device’s modem control register (MCR).
- [HwProgramUART](./hwprogramuart.md)
  Configure the settings for the device’s universal asynchronous receiver/transmitter (UART).
- [Hardware Constants](../hardware-constants.md)
  Configure your device with the appropriate parity and flow-control options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/hwprogramlatencytimer)*