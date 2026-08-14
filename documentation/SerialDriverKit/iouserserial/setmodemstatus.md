# SetModemStatus

**Framework**: SerialDriverKit  
**Kind**: method

Sets the modem status to the specified values.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
virtual kern_return_t SetModemStatus(bool cts, bool dsr, bool ri, bool dcd);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes).

#### Discussion

Call this method to report the state of the device to the system.

## Parameters

- `cts`: A Boolean value indicating the state of the clear-to-send bit. Specify `YES` to set the bit or `NO` to clear it.
- `dsr`: A Boolean value indicating the state of the data-set-ready bit. Specify `YES` to set the bit or `NO` to clear it.
- `ri`: A Boolean value indicating the state of the ring-indicator bit. Specify `YES` to set the bit or `NO` to clear it.
- `dcd`: A Boolean value indicating the state of the data-carrier-detect bit. Specify `YES` to set the bit or `NO` to clear it.

## See Also

- [HwGetModemStatus](iouserserial/hwgetmodemstatus.md)
  Gets the current status of the modem from the hardware.
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

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/setmodemstatus)*